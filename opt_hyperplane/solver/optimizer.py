import cplex
from cplex.exceptions import CplexError 
import numpy as np


class SetSimplex(object):
    """Set the parameters for Simplex method.
    Solve the system

    Args:
        object : Object
    """
    def __init__(self):
        """Initialize the SetSimplex object
        """
        self.object_coeff = []
        self.bound_ub = []
        self.bound_lb = []
        self.decision_var = []
        self.constraint_rhs = []
        self.constraint_label = []
        self.constraint_inequality = ""
    

    def set_object_coeff(self, obj_list: list):
        """Set the object coefficient
        The object coefficient means the factor of design variable(decision variable) of objective function
        The instance `object_coeff` has the N number of object coefficient accorinding to decision variable

        Args:
            obj_list (list): The list of object coefficients
        """
        self.object_coeff = obj_list
    

    def set_bound_ub(self, ub_bound: list):
        """Set the upper boundary of the decision variable

        Args:
            ub_bound (list): The list of upper boundary of decision variable
        """
        self.bound_ub = ub_bound

    def set_bound_lb(self, lb_bound:list):
        self.bound_lb =lb_bound

    def set_decision_variable(self, decision_var: list):
        """Set the name of decision variable 

        Args:
            decision_var (list): The list of name of decision variable
        """
        self.decision_var = decision_var
    

    def set_constraint_rhs(self, rhs: list):
        """Set the list of rhs constraint 

        Args:
            rhs (list): The list of rhs constraint 
        """
        self.constraint_rhs = rhs
    

    def set_constraint_label(self, label: list):
        """Set the constraint label 

        Args:
            label (list): The list of constraint label
        """
        self.constraint_label = label
    

    def set_constraint_inequality(self, inequal_list: str):
        """Set the constraint inequality.
        By the Cplex reference, G means the greater, L means the lower
        E means the equality. And the list of the constraint inequality is 
        the string sequence of inequality characters which is defined by Cplex library

        Args:
            inequal_list (str): String sequence of inequality
        """
        self.constraint_inequality = inequal_list
        
    @property
    def set_cplex(self):
        """Set the cplex object as cplex instance
        """
        self.cplex = cplex.Cplex()
        

    def set_lhs_coeff(self, lhs_coeff: np.array):
        """Set the list of lhs constraint

        Args:
            lhs_coeff (np.array): numpy array of the lhs constraint
        """
        self.lhs_coeff = lhs_coeff
    
    def initialize_simplex(self, direction_solution: str):
        """Set the direction of objective function

        Args:
            direction_solution (str): User can decide "maximize" or "minimize"

        Raises:
            ValueError: The direction_solution is not "maximize" or "minimize"
        """
        if direction_solution == "minimize":
            self.direction_solution = self.cplex.objective.sense.minimize
        elif direction_solution == "maximize":
            self.direction_solution = self.cplex.objective.sense.maximize
        else:
            raise ValueError('Direction of the solution solution must be "minimize" or "maximize"') 
    
    @property
    def set_cplex_constraint(self):
        """Set the cplex constraint with SetSimplex instance
        The constraint set with rows method.
        """
        self.cplex.objective.set_sense(self.direction_solution)
        self.cplex.variables.add(obj=self.object_coeff, ub=self.bound_ub, lb=self.bound_lb, names=self.decision_var)
        rows = self.get_row_lhs()
        self.cplex.linear_constraints.add(lin_expr=rows, senses=self.constraint_inequality, rhs=self.constraint_rhs, names = self.constraint_label)
        
    def solve(self, filename: str = "solution.lp"):
        """Solve the problem and save the Linear programming model on filename

        Args:
            filename (str, optional): The filename to save the LP model. 
            Defaults to "solution.lp".
        """
        self.set_cplex_constraint
        self.cplex.write(filename)
        self.cplex.solve()
        
    
    def get_row_lhs(self):
        """Get the lhs constraint formated by rows method
        For example, The decision variable is ["x1","x2"."x3"]
        and the coefficient of lhs constraint is [[1,2,3], [4,5,6]]
        Return [
            [["x1","x2"."x3"], [1,2,3]],
            [["x1","x2"."x3"], [4,5,6]]
        ]

        Returns:
            list: lhs coeffcient formatted by rows method
        """
        global_mat = []
        local_mat = []
        for rows in self.lhs_coeff:
            local_mat.append(self.decision_var)
            local_mat.append(rows.tolist())
            global_mat.append(local_mat)
            local_mat = []
        return global_mat
        
    @property
    def visualize_solution(self):
        """Visualize the solution.
        The format refer to HW#2
        """
        numrows = self.cplex.linear_constraints.get_num()
        numcols = self.cplex.variables.get_num()

        print()
        # solution.get_status() returns an integer code
        print("Solution status = ", self.cplex.solution.get_status(), ":", end=' ')
        # the following line prints the corresponding string
        print(self.cplex.solution.status[self.cplex.solution.get_status()])
        print("Solution value  = ", self.cplex.solution.get_objective_value())
        slack = self.cplex.solution.get_linear_slacks()
        pi = self.cplex.solution.get_dual_values()
        x = self.cplex.solution.get_values()
        dj = self.cplex.solution.get_reduced_costs()
        for i in range(numrows):
            print("Row %d:  Slack  = %10f  Pi = %10f" % (i, slack[i], pi[i]))
        for j in range(numcols):
            print("Column %d:  Value = %10f Reduced cost = %10f" %
                (j, x[j], dj[j]))

    def get_value(self):
        return self.cplex.solution.get_values()

    def save_solution(self, filename: str):
        """Save the solution as the format which is defined by mid-term exam document(Q2.3)

        Args:
            filename (str): The filename
        """
        object_value = self.cplex.solution.get_objective_value()
        num_solution = self.cplex.variables.get_num()
        solution_value = self.cplex.solution.get_values()
        with open(filename, "w+") as f:
            f.write(str(object_value) + "\n")
            f.write(str(num_solution) + str("\n"))
            for count, id in enumerate(self.decision_var):
                f.write(str(id) + "     " + str(solution_value[count]) + "\n")
                