import json


INT_KEYS = {"order_hyperplane", "update_upper_lower"}

FLOAT_KEYS = {"ub_bound",
              "lb_bound"}

def load_params_from_json(json_fname: str, correct_format: bool = True):
    json_dict = load_json(json_fname)

    params = json_dict["param"]

    if correct_format:
        for key in params:
            if key in INT_KEYS:
                params[key] = int(params[key])
            elif key in FLOAT_KEYS:
                params[key] = float(params[key])
    return params


def load_name_from_json(json_fname: str):
    json_dict = load_json(json_fname)

    return json_dict["name"]


def load_json(json_fname: str):
    with open(json_fname) as f:
        json_dict = json.load(f)

    return json_dict