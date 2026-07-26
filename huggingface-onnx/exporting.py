# !python -m transformers.onnx --help

# Configs

from transformers.models.roberta import RobertaConfig, RobertaOnnxConfig
config = RobertaConfig()
onnx_config = RobertaOnnxConfig(config)
print(list(onnx_config.inputs.keys()))

# Exporting a model to ONNX

from transformers.onnx.features import FeaturesManager

distilbert_features = list(FeaturesManager.get_supported_features_for_model_type("distilbert").keys())
print(distilbert_features)


# !python -m transformers.onnx --model=distilbert-base-uncased-finetuned-sst-2-english \ --feature=question-answering .

