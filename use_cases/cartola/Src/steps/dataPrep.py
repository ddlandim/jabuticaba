from dataUtils.dataHandler import DataHandler
from steps import dp_functions
from runUtils.logger import MyLogger
class DataPrep():
    args: dict
    input_path: str
    target_path: str
    target_column: str
    feature_path: str
    ft_drop_columns_l: list
    in_dh: DataHandler
    features_dh: DataHandler
    target_dh: DataHandler
    logger = MyLogger()
    def apply_functions(self,app_fn_dict: dict):
        _call_list = app_fn_dict.keys()
        for _call in _call_list:
            self.logger.info(_call)
            _call_obj = dict(app_fn_dict[_call])
            _columns = list(_call_obj["columns"])
            fn_name = str(_call_obj["function"])
            fn = dp_functions.functions_dict[fn_name]
            for _column in _columns:
                new_column = dp_functions.functions_cl_name.get(fn_name)
                if new_column.endswith("_"):
                    new_column = new_column + _column
                self.logger.info(f" Applying {fn_name} to column {_column} as {new_column}")
                df = self.features_dh.get_df()
                df[new_column] = df[_column].apply(fn)
                self.features_dh.set_df(df)
            self.ft_drop_columns_l += _columns


    def __init__(self, args: dict) -> None:
        self.args = args
        self.input_path = args["input_path"]
        self.target_column = args["target_column"]
        self.target_path = args["target_path"]
        self.features_path = args["features_path"]
        self.in_dh = DataHandler(
            path = self.input_path,
            args = self.args["DataHandler"],
        )
        _list = [self.target_column]
        self.target_dh = DataHandler(
            df=self.in_dh.get_subset_cp(_list),
            path=self.target_path
        )
        self.features_dh = DataHandler(
            df=self.in_dh.get_df().copy(),
            path=self.features_path
        )
        self.ft_drop_columns_l = list()
        self.ft_drop_columns_l.append(self.target_column)
        self.apply_functions(args["apply_functions"])
        self.features_dh.drop_df_columns(self.ft_drop_columns_l)
        self.dump()


    def dump(self):
        self.target_dh.dump()
        self.features_dh.dump()
    
    def get_df(self):
        return self.df
