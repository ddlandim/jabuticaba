import pandas as pd
from pandas import DataFrame
from runUtils.logger import MyLogger
from pathlib import Path
import glob
class DataHandler():
    path: str
    df: DataFrame
    logger = MyLogger()
    def init_pd(self, path:str, delimiter=None, header="infer", index_col=None):
        df = pd.read_csv(path,
                         delimiter=delimiter,
                         header=header,
                         index_col=index_col)
        self.df = df

    def __init__(self, path = None, df: DataFrame = None, args = dict()) -> None:
        if df is None:
            self.path = path
            pd_args = args.get("pandas",None)
            if pd_args is not None:
                self.init_pd(
                    self.path,
                    delimiter = pd_args["delimiter"],
                    header = pd_args["header"],
                    index_col = pd_args["index_col"]
                )
        else:
            self.df = df
            self.path = path
    

    def dump(self, out_path: str = None):
        _path = out_path or self.path
        _df = self.df
        _df_name = _path.split(".csv")[0].split("/")[-1]
        __path = _path.split(_df_name)[-1]
        self.logger.info("".join([
            "Exporting ",_path,
            "\n"
        ]))
        print(self.df.head(5))
        output_file = Path(_path)
        output_file.parent.mkdir(exist_ok=True, parents=True)
        _df.to_csv(_path)
    

    def get_df(self):
        return self.df


    def set_df(self,df):
        self.df = df


    def get_subset_cp(self,_columns: list):
        return self.df[_columns].copy()
    

    def drop_df_columns(self, _columns: list):
        print(str(_columns))
        self.df = self.df.drop(_columns,axis=1)
    