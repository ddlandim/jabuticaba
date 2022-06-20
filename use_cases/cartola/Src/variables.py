from steps.dataPrep import DataPrep
from steps.dataSplit import DataSplit
from runUtils.logger import MyLogger
project = "Desafio_Eng_ML"
logger = MyLogger()
logging_codes = {
    0: logger.error,
    1: logger.info
}
steps_dict = {
    "DataPrep" : DataPrep,
    "DataSplit" : DataSplit
}