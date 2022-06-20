from steps import ds_functions
from dataUtils.dataHandler import DataHandler
from datetime import datetime
class DataSplit():
    split_id: str
    features_dh: DataHandler
    target_dh: DataHandler
    split_path: str
    X_train_dh: DataHandler
    X_test_dh: DataHandler
    y_train_dh: DataHandler
    y_test_dh: DataHandler

    def set_train_test_df(self,X_train, X_test, y_train, y_test):
        self.X_train_dh = DataHandler(
           df = X_train,
           path = "/".join([self.split_path,
                            "X_train.csv"])
        )
        self.X_test_dh = DataHandler(
           df = X_test,
           path = "/".join([self.split_path,
                            "X_test.csv"])
        )
        self.y_train_dh = DataHandler(
           df = y_train,
           path = "/".join([self.split_path,
                            "y_train.csv"])
        )
        self.y_test_dh = DataHandler(
           df = y_test,
           path = "/".join([self.split_path,
                            "y_test.csv"])
        )

    def apply_split(self,split_args: dict):
        X = self.features_dh.get_df()
        if X.empty:
            raise Exception("Null X DataFrame")
        target = self.target_dh.get_df()
        if target.empty:
            raise Exception("Null target DataFrame")
        
        _lib = split_args["lib"]
        _function = split_args["function"]
        _fn_args = dict(split_args["args"])
        _fn_name = "_".join([_lib,_function])
        _fn = ds_functions.fn_dict[_fn_name]
        
        X_train, X_test, y_train, y_test = \
            _fn(X=X,
                target=target,
                args=_fn_args)
        
        self.set_train_test_df(X_train, X_test, y_train, y_test)
        
    def __init__(self, args = dict()) -> None:
        self.args = args
        self.split_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.target_path = args["target_path"]
        self.features_path = args["features_path"]
        self.split_path = "/".join([
                                    str(args["split_path"]),
                                    self.split_id])
        self.target_dh = DataHandler(
            path = self.target_path,
            args = self.args["DataHandler"],
        )
        self.features_dh = DataHandler(
            path = self.features_path,
            args = self.args["DataHandler"],
        )
        self.apply_split(dict(self.args["split_fn"]))
        self.dump()


    def dump(self, out_path: str = None):
       self.X_train_dh.dump(out_path)
       self.X_test_dh.dump(out_path)
       self.y_train_dh.dump(out_path)
       self.y_test_dh.dump(out_path)