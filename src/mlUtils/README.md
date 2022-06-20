# class SklModel()
TREINO
    pyhon src/mlUtils/sklModel.py
        --path (obrigatorio para informar dados de exportacao do modelo)
            formato : fs://some-root/some-path/
        --train (obrigatorio para informar pasta com dados de treino)
            formato: fs//some-root/some-path/
            deve conter: X_train.csv,X_test.csv,y_train.csv,y_test.csv
    exemplo:  
    ```
    (datascience) PS C:\Users\douglas.diniz.landim\OneDrive - Accenture\Documents\Desafio_Eng_ML\Project> python .\Src\mlUtils\sklModel.py --path=".\Models\sklModel\" --train=".\Datalake\splited\20220609112022\"
    ```

PREDICAO
    pyhon src/mlUtils/sklModel.py
        --path (obrigatorio para informar dados de exportacao do modelo)
        --predict (obrigatorio para informar caminho do arquivo X_predict já pre-processado, deve ser compativel com leitura pandas)
    exemplo:  
    ```
    \sklModel.py --path=".\Models\sklModel\propension_model_new.joblib" --predict=".\Datalake\splited\20220609112022\X_test.csv" --threshold=0.75
    ```

MELHORIAS:

- CONSTRUIR PIPE COM dicionário kwargs
- REFATORAR PARA O USO COMPLETO DO DATAHANDLER