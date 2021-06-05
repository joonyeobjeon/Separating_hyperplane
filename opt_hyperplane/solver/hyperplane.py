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
    def __init__(self, filename, output_solution, output_file):
        self.filename = filename
        self.output_expression = output_solution
        self.output_file = output_file
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
        self.solver.save_solution(self.params["solution_filename"])

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
