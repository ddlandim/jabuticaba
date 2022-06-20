# Módulo main.py

Modulo com o padrão factory method que carrega um json passado como parametro, e iterage sobre os objetos contidos em steps{} de forma ordenada,
faz um split("_")[0] e instancia as classes, conforme um dicionário carregado em variables.py

exemplo de arquivo json

```
{
    "msg":"Default conf file loaded",
    "steps": {
        "DataPrep_1":{
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
        },
        "DataSplit_1" : {
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
    }
}
```