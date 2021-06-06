import json
import numpy as np
from opt_hyperplane.io.dataset import Data
from opt_hyperplane.visualize import Visualize
from opt_hyperplane.solver.optimizer import SetSimplex
from opt_hyperplane.io.parsing import (load_params_from_json, 
                                    load_name_from_json, 
                                    load_json)
from opt_hyperplane.solver.optimizer_tools import (make_decision_variable_label, 
                                                    make_fare_rhs_constraint, 
                                                    make_constraint_label, 
                                                    make_all_inequality_list,
                                                    make_norder_constraint_coeff_lhs_problem2,
                                                    make_boundary_list, make_demand_bound)



class HyperPlaneOptimizer(object):
    def __init__(self, filename):
        self.filename = filename
        self.read_parameters()
        self.initialize()

    def read_parameters(self):
        self.params = load_params_from_json(self.filename)
        self.name = load_name_from_json(self.filename)
    
    def initialize(self):
        self.order = self.params["order_hyperplane"]
        self.nofvar = self.order + 2
        self.dataset_name = self.params["dataset"]
        self.data = Data(self.dataset_name)
        self.data.read()
        self.output_expression = self.params["initialze_solution_filename"]
        self.output_file = self.params["solution_filename"]
        if self.params["update_upper_lower"] == 1:
            print(self.params["update_upper_lower"])
            self.data.update_upper_lower()
        
    def initialize_optimization_variables(self):
        self.d_var = make_decision_variable_label(self.nofvar)
        self.object_coeff = [0]* self.order + [1, 0]
        
        self.ub_bound = make_demand_bound(self.nofvar, self.params["ub_bound"])
        self.lb_bound = make_demand_bound(self.nofvar, self.params["lb_bound"])
        
        rhs_fare0 = make_fare_rhs_constraint(np.size(self.data.dataset[0], 0), 1.0)
        rhs_fare1 = make_fare_rhs_constraint(np.size(self.data.dataset[1], 0), -1.0)
        self.rhs_fare = np.append(rhs_fare0, rhs_fare1, axis=0)
        self.c_label = make_constraint_label(np.size(self.rhs_fare))
        senses0 = make_all_inequality_list(np.size(rhs_fare0), "G")
        senses1 = make_all_inequality_list(np.size(rhs_fare1), "L")
        self.senses = senses0 + senses1
        self.lhs_constraint = make_norder_constraint_coeff_lhs_problem2(self.data, self.nofvar, self.order)
    
    def solve(self):
        self.solver = SetSimplex()
        self.solver.set_bound_ub(self.ub_bound)
        self.solver.set_bound_lb(self.lb_bound)
        self.solver.set_constraint_inequality(self.senses)
        self.solver.set_constraint_label(self.c_label)
        self.solver.set_constraint_rhs(self.rhs_fare)
        self.solver.set_decision_variable(self.d_var)
        self.solver.set_lhs_coeff(self.lhs_constraint)
        self.solver.set_object_coeff(self.object_coeff)

        self.solver.set_cplex
        self.solver.initialize_simplex(self.params["optimize_direction"])
        self.solver.solve(self.params["initialze_solution_filename"])
        self.solver.visualize_solution
        self.save_solution()
        self.save_detail_solution()

    def visualize_solution(self):
        visual = Visualize(self.data)
        visual.set_order(self.order)
        visual.set_coefficient(self.solver.get_value())
        visual.set_scatter()
        visual.set_title(self.dataset_name)
        visual.set_plot()
        visual.show_plot()
        
    def optimize(self):
        self.initialize_optimization_variables()
        self.solve()
        self.visualize_solution()
    
    def get_delta(self):
        coeff = self.solver.get_value()
        all_dataset = self.data.attach_dataset()
        for count, var in enumerate(all_dataset):
            x = var[0]
            y = var[1]
            tmp_solution = 0
            for order in range(self.order):
                tmp_solution = tmp_solution - coeff[order] * x ** (order+1)
            tmp_solution = tmp_solution - coeff[order+2]
            tmp_solution = tmp_solution / coeff[order+1]
            tmp_delta = np.abs(y - tmp_solution)
            if count == 0:
                solution = tmp_delta
            else:
                solution = min(solution, tmp_delta)
        return solution
    
    def save_solution(self):
        """Save the solution as the format which is defined by mid-term exam document(Q2.3)

        Args:
            filename (str): The filename
        """
        object_value = self.solver.cplex.solution.get_objective_value()
        num_solution = self.solver.cplex.variables.get_num()
        solution_value = self.solver.cplex.solution.get_values()
        delta_value = self.get_delta()
        with open(self.params["solution_filename"], "w+") as f:
            f.write("Optimal solution::" + str(object_value) + "\n")
            f.write("Number of design variables::" + str(num_solution) + str("\n"))
            f.write("Delta value::" + str(delta_value) + "\n")
            for count, id in enumerate(self.solver.decision_var):
                f.write(str(id) + "     " + str(solution_value[count]) + "\n")
    
    
    def save_detail_solution(self):
        numrows = self.solver.cplex.linear_constraints.get_num()
        numcols = self.solver.cplex.variables.get_num()

        with open("detail_"+self.params["solution_filename"], "w+") as f:
            # solution.get_status() returns an integer code
            f.write("Solution status::" + str(self.solver.cplex.solution.get_status()) + "\n")
            # the following line prints the corresponding string
            f.write("type::"+str(self.solver.cplex.solution.status[self.solver.cplex.solution.get_status()]) + "\n")
            f.write("Solution value::" + str(self.solver.cplex.solution.get_objective_value())+ "\n")
            slack = self.solver.cplex.solution.get_linear_slacks()
            pi = self.solver.cplex.solution.get_dual_values()
            x = self.solver.cplex.solution.get_values()
            dj = self.solver.cplex.solution.get_reduced_costs()
            for i in range(numrows):
                f.write("Row" + str(i)+ "::Slack  =" + str(slack[i]) + " Pi = " + str(pi[i]) + "\n")
            for j in range(numcols):
                f.write("Column" + str(j) + "::Value =" + str(x[j]) + " Reduced cost = " + str(dj[j]) + "\n")