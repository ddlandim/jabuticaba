# #### Python Libraries #### #
import argparse
import logging
import json
# #### Project Libraries #### #
from runUtils.logger import MyLogger
import variables
# #### End Libraries #### #

# #### Init Vars #### #
logging.basicConfig(level=logging.INFO)
steps_objs = list()
logger = MyLogger()
# #### Init Functions #### #


def exit(code: int, msg: str):
    variables.logging_codes.get(code,0)(msg,exc_info=True)
    return code


def run_steps(steps_json: dict):
    _steps = steps_json.keys()
    for _step in _steps:
        _msg = "".join([
            "running step : ",_step
        ])
        logger.info(_msg)
        __step = _step.split("_")[0]
        _step_json = dict(steps_json[_step])
        __step_obj = variables.steps_dict[__step](_step_json)
        steps_objs.append(__step_obj)


def run():
    # Input arguments startup
    parser = argparse.ArgumentParser()
    parser.add_argument("".join(["--", "conf"]), type=str,
                        required=False, default=".\confs\default.json")
    args = parser.parse_args()
    args_dict = vars(args)
    _conf_path = str(args_dict["conf"])
    try:
        f = open(_conf_path)
        conf = json.load(f)
        f.close()
        logger.info(str(conf["msg"]))
    except Exception as e:
        _msg = "".join([
            "Json conf and default conf file not loaded, check ./confs folder"
        ])
        exit(0,_msg)
    
    try:
        run_steps(conf["steps"])
    except Exception as e:
        _msg = "".join([
            "run_steps fail"
        ])
        exit(0,_msg)

if __name__ == "__main__":
    run()
# #### End Functions #### #
