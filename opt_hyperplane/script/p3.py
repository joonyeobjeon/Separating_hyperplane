from opt_hyperplane.io.dataset import Data
from opt_hyperplane.solver.optimizer import SetSimplex
from opt_hyperplane.visualize import Visualize
from opt_hyperplane.solver.optimizer_tools import (make_decision_variable_label, 
                                                          make_fare_rhs_constraint, 
                                                          make_constraint_label, 
                                                          make_all_inequality_list,
                                                          make_norder_constraint_coeff_lhs_problem2,
                                                          make_boundary_list, make_demand_bound)
import numpy as np
order = 5
nofvar = order + 2
dataset_name = "../data/DataSetC/DataSetC-10.dat"

dataset = Data(dataset_name)
dataset.read()
# dataset.update_upper_lower()
visual = Visualize(dataset)

d_var = make_decision_variable_label(nofvar)
object_coeff = [0]*order + [1, 0]

ub_bound = make_demand_bound(nofvar, 1e19)
lb_bound = make_demand_bound(nofvar, -1e19)

rhs_fare0 = make_fare_rhs_constraint(np.size(dataset.dataset[0], 0), 1.0)
rhs_fare1 = make_fare_rhs_constraint(np.size(dataset.dataset[1], 0), -1.0)
rhs_fare = np.append(rhs_fare0, rhs_fare1, axis=0)
c_label = make_constraint_label(np.size(rhs_fare))
senses0 = make_all_inequality_list(np.size(rhs_fare0), "G")
senses1 = make_all_inequality_list(np.size(rhs_fare1), "L")
senses = senses0 + senses1
lhs_constraint = make_norder_constraint_coeff_lhs_problem2(dataset, nofvar, order)

solver = SetSimplex()

solver.set_bound_ub(ub_bound)
solver.set_bound_lb(lb_bound)
solver.set_constraint_inequality(senses)
solver.set_constraint_label(c_label)
solver.set_constraint_rhs(rhs_fare)
solver.set_decision_variable(d_var)
solver.set_lhs_coeff(lhs_constraint)
solver.set_object_coeff(object_coeff)

solver.set_cplex
solver.initialize_simplex("minimize")
solver.solve("solution.lp")
solver.visualize_solution
solver.save_solution("solution_result.txt")

visual.set_order(order)
visual.set_coefficient(solver.get_value())
visual.set_scatter()
visual.set_title(dataset_name)
visual.set_plot()
visual.show_plot()