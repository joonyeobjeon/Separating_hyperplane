import json

json_name = "datasetB-5000.json"

data = {}
data["name"] = "datasetB-5000"
data["param"] = {
    "dataset": "../../data/DataSetB/DataSetB-5000.dat",           # name: nx / type: int / range(30 ~ 128)/
    "order_hyperplane": "3",
    "lb_bound": "-1e19",
    "ub_bound": "1e19",
    "update_upper_lower": "1",
    "optimize_direction": "minimize",
    "initialze_solution_filename": "solution.lp",
    "solution_filename": "solution.result"

}
with open(json_name, "w") as outfile:
    json.dump(data, outfile)