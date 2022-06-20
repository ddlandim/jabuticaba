from asyncio.log import logger
from typing import Any
from pandas import DataFrame
import sklearn
from sklearn.model_selection import train_test_split


def sklearn_train_test_split(args: dict = dict(),
                             X: DataFrame = None, target: DataFrame = None,
                             train_size = 0.7):
    train_size = args.get("train_size", train_size)
    X_train, X_test, y_train, y_test = train_test_split(X, target, train_size=0.7)
    return X_train, X_test, y_train, y_test

fn_dict = {
    "sklearn_train_test_split" : sklearn_train_test_split
}