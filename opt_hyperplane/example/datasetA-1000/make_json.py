import json

json_name = "datasetA-1000.json"

data = {}
data["name"] = "datasetA-1000"
data["param"] = {
    "dataset": "../../data/DataSetA/DataSetA-1000.dat", # filepath of dataset
    "order_hyperplane": "1",    # order of equation (ex. a*x+b*y+c=0 : 1st order, a*x^2+b*x+c*x+d=0 : 2nd order)
    "lb_bound": "-1e19",    # low boundary of design variable
    "ub_bound": "1e19",     # upper boundary of design variable
    "update_upper_lower": "1",  # if you choose it as 1, The upper dummy is changed to `0`label and the lower dummy is changed to `0` label. 
                                # else, the 0 label is upper dummy, the `1 label` is lower dummy
    "optimize_direction": "minimize",   # optimization type
    "initialze_solution_filename": "solution.lp",   # Output for optimization generalization
    "solution_filename": "solution.result"  # Result of optimization

}
with open(json_name, "w") as outfile:
    json.dump(data, outfile)