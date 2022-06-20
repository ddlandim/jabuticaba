# Jabuticaba: Framework para pipelines de dados e ml.
![Jabuticaba icon](icon.png)

## About Jabuticaba
![Jabuticaba draw](draw.png)
The jabuticaba project is a framework for developing and running machine learning project pipelines.
currently contains 3 classes that do data preparation and splitting, and a class with a machine learning model, all of which use a helper class to manipulate the data during the pipeline.
The objective of the project is to extend these classes so that they can be exported as containers with independent execution.
each class is instantiated as a pipeline object and can be constructed with a .json file containing the construction and execution parameters of this object.

## Factory Method para DataPrep e DataSplit
[Factory Method](./src/README.md)
[DataPrep/Split](./src/steps/README.md)
## Classes ML (execucao sem factory method)
[DataPrep/Split](./src/mlUtils/README.md)