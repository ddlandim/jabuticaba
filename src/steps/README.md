# Classes de preparação e split dos dados
- Construção com dicionários {}
- modulo principal main.py atua como "factory method" carregando o arquivo .conf e passando o dicionário na construção da classe.

# Classe DataPrep()
- script: dataPrep.py
- Constructor com dicionário python, dataPrep_obj = DataPrep(args_dict)
- Deve conter os parametros de contrução de um DataHandler contendo os parametros do manipulador de arquivos (pandas/spark) para o carregamento do dataframe
exemplo:
```
args_dict = {
    "DataHandler" : {
        "pandas" : {
            "delimiter" : ",",
            "header" : "infer",
            "index_col" : "GLOBO_ID"
        }
    },
    "input_path": "../Datalake/raw/desafiocartola.csv",
    "target_column": "pro_target",
    "target_path" : "../Datalake/transformed/target.csv",
    "features_path" : "../Datalake/transformed/features.csv",
    "apply_functions" : {
        "call_1": {
            "columns" : ["anos_desde_criacao", "instagram_num", "facebook_num", "min_camp", "interacoes_g1", "tempo_desperd", "iteracao_volei", "iteracao_atletismo"],
            "function" : "get_long_tail"
        },
        "call_2": {
            "columns" : ["pixels"],
            "function" : "get_total_pixels"
        },
        "call_3" : {
            "columns" : ["avg_3", "avg_4"],
            "function" : "ceil"
        }
    }
}
```
)

# class DataSplit():
- Constructor com dicionário python, dataPrep_obj = DataPrep(args_dict)
- Deve conter os parametros de contrução de um DataHandler contendo os parametros do manipulador de arquivos (pandas/spark) para o carregamento do dataframe
exemplo:
```
args_dict = {
    "DataHandler" : {
        "pandas" : {
            "delimiter" : ",",
            "header" : "infer",
            "index_col" : "GLOBO_ID"
        }
    },
    "target_path" : "../Datalake/transformed/target.csv",
    "features_path" : "../Datalake/transformed/features.csv",
    "split_path" : "../Datalake/splited",
    "split_fn" : {
        "lib" : "sklearn",
        "function" : "train_test_split",
        "args" : {
            "train_size" : 0.7
        }
    }
}
```
dataPrep_obj = DataPrep(args_dict)