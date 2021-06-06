import json

json_name = "datasetC-xor.json"

data = {}
data["name"] = "datasetC-xor"
data["param"] = {
    "dataset": "../../data/DataSetC/DataSetC-xor.dat",           # name: nx / type: int / range(30 ~ 128)/
    "order_hyperplane": "6",
    "lb_bound": "-1e19",
    "ub_bound": "1e19",
    "update_upper_lower": "1",
    "optimize_direction": "minimize",
    "initialze_solution_filename": "solution.lp",
    "solution_filename": "solution.result"

}
with open(json_name, "w") as outfile:
    json.dump(data, outfile)