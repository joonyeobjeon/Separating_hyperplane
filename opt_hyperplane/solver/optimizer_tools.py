import numpy as np
from opt_hyperplane.io.dataset import Data


def make_decision_variable_label(nofdecision: int):
    var_label = []
    for id in range(nofdecision):
        var_label.append("x"+str(id))
    return var_label

def make_fare_rhs_constraint(nofconstraint: int, value: float):
    rhs_list = []
    for _ in range(nofconstraint):
        rhs_list.append(value)
    return rhs_list

def make_constraint_label(nofconstraint: int):
    constraint_label = []
    for count in range(nofconstraint):
        constraint_label.append("c"+str(count))
    return constraint_label

def make_all_inequality_list(nofconstraint, inequal: str):
    inequality = ""
    for _ in range(nofconstraint):
        inequality = inequality + (inequal)
    return inequality

def make_constraint_coeff_lhs_problem1(dataset: Data, num_var: int):
    num_dataset = np.size(dataset.dataset[0], 0) + np.size(dataset.dataset[1], 0)
    lhs = np.zeros([num_dataset, num_var])
    data = dataset.attach_dataset()
    for num in range(num_dataset):
        lhs[num, 0] = data[num, 0]
        lhs[num, 1] = data[num, 1]
        lhs[num, 2] = 1
    return lhs

def make_demand_bound(nofbounds: int, value: float):
    ub = []
    for _ in range(nofbounds):
        ub.append(value)
    return ub

def make_boundary_list(values: list):
    return values

def make_norder_constraint_coeff_lhs_problem2(dataset: Data, num_var, orders: int):
    num_dataset = np.size(dataset.dataset[0], 0) + np.size(dataset.dataset[1], 0)
    lhs = np.zeros([num_dataset, num_var])
    data = dataset.attach_dataset()
    for num in range(num_dataset):
        for order in range(orders):
            lhs[num, order] = data[num, 0] ** (order+1)
    
        lhs[num, order+1] = data[num, 1]
        lhs[num, order+2] = 1

    return lhs