import json

json_name = "datasetA-1000.json"

data = {}
data["name"] = "p1"
data["param"] = {
    "dataset": "../data/DataSetC/DataSetC-10.dat",           # name: nx / type: int / range(30 ~ 128)/
    "order_hyperplane": "1",
    "lb_bound": "-1e19",
    "ub_bound": "1e19",
    "update_upper_lower": "0",
    "optimize_direction": "minimize",
    "initialze_solution_filename": "solution.lp",
    "solution_filename": "solution.result"

}
with open(json_name, "w") as outfile:
    json.dump(data, outfile)