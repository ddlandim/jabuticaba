import argparse
from datetime import datetime
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import PowerTransformer
from sklearn.linear_model import SGDClassifier
import joblib
import pandas as pd


class SklModel():
    path: str
    train_history = None
    pipe: Pipeline
    X_train = None
    X_test = None
    y_train = None
    y_test = None
    score = None
    scallers = list()
    out_path: str
    filename = "sklModelObj.joblib"
    X_predict = None
    y_predicted = None

    def __init__(self,
                 path=None,
                 args=None) -> None:
        self.pipe = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('center', PowerTransformer(standardize=True)),
            ('sgd', SGDClassifier(loss='log', verbose=5, early_stopping=True, validation_fraction=0.3))
        ])
        if path is not None:
            self.path = path
            self.load(path)

    def load(self, path):
        if path.endswith(".joblib"):
            obj = joblib.load(path, mmap_mode=None)
            _filename = path.split("\\")[-1]
            self.filename = _filename
            self.path = path.split(_filename)[0]
            if type(obj) == type(self):
                self.pipe = obj
                self.X_train = obj.X_train
                self.X_test = obj.X_test
                self.y_train = obj.y_train
                self.y_test = obj.y_test
            else:
                self.pipe = obj
                print("PIPE LOADED")
                print(self.pipe)


    def dump(self):
        _now = datetime.now().strftime("%Y%m%d%H%M%S")
        obj_path = self.path + _now + "_" + self.filename
        pipe_path = self.path + _now + "_pipeModel.joblib"
        print(f"\nSaving sklModel object {obj_path}\n")
        joblib.dump(self, obj_path)
        print(f"\nSaving sckitlearn Pipe object {pipe_path}\n")
        joblib.dump(self, pipe_path)
        if self.y_predicted is not None:
            _path_predicted = self.out_path
            print(f" Saving predicted DF to {_path_predicted}")
            self.y_predicted.to_csv(_path_predicted)

    def init_train_data(self, data_path: str):
        self.X_train = pd.read_csv(
            data_path + "X_train.csv",
            index_col="GLOBO_ID"
        )
        self.X_test = pd.read_csv(
            data_path + "X_test.csv",
            index_col="GLOBO_ID"
        )
        self.y_train = pd.read_csv(
            data_path + "y_train.csv",
            index_col="GLOBO_ID"
        )
        self.y_test = pd.read_csv(
            data_path + "y_test.csv",
            index_col="GLOBO_ID"
        )

    def set_score(self):
        self.score = \
            self.pipe.score(
                self.X_test,
                self.y_test)

    def fit(self):
        self.train_history = self.pipe.fit(
            self.X_train,
            self.y_train
        )
        self.set_score()
        _msg = f"\nSCORE : {str(self.score)}\n"
        print(_msg)

    def init_predict_data(self, predict_path: str):
        if predict_path is not None:
            self.X_predict = pd.read_csv(
                predict_path,
                index_col="GLOBO_ID"
            )
            print("X DataFrame Loaded")
            print(self.X_predict.head())
            self.out_path = predict_path.replace(".csv", "_y_predicted.csv")
        else:
            return None

    def predict(self, x_predict=None, threshold=None):
        _theshold = threshold or 0.5
        _x_predict = self.init_predict_data(x_predict) or self.X_test
        _predicted = self.pipe.predict_proba(self.X_predict)
        s = pd.DataFrame(data=_predicted[:, 1], columns=["target_pro_proba"])
        s["threshold"] = _theshold
        s["target_pro"] = s["target_pro_proba"] > s["threshold"]
        self.y_predicted = s
        print("Predicted head")
        print(s.head())


if __name__ == "__main__":

    # Input arguments startup
    parser = argparse.ArgumentParser()
    parser.add_argument("".join(["--", "path"]), type=str,
                        required=True)
    parser.add_argument("".join(["--", "train"]), type=str,
                        required=False, default=None)
    parser.add_argument("".join(["--", "predict"]), type=str,
                        required=False, default=None)
    parser.add_argument("".join(["--", "threshold"]), type=float,
                        required=False, default=0.5)
    args = parser.parse_args()
    args_dict = vars(args)

    _path = args_dict["path"]
    skl = SklModel(_path)

    if args_dict["train"] is not None:
        skl.init_train_data(args_dict["train"])
        skl.fit()


    if args_dict["predict"] is not None:
        skl.init_predict_data(args_dict["predict"])
        skl.predict(x_predict=args_dict["predict"], threshold=args_dict["threshold"])


    skl.dump()
