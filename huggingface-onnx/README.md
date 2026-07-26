# Hugging Face and ONNX introduction
ONNX Runtime is a performance-focused inference engine for ONNX models. It is cross-platform and open source. It supports execution of models on a wide range of devices, from CPUs to GPUs.

ONNX allows for interoperability between different frameworks and tools, it is open source and therefore can be easily extended, and it is efficient and scalable.

This notebook will explore the ONNX runtime and how to use it with Hugging Face Transformers.

## Installation 
Make sure you are using the right libraries. It might be easier to use conda to install the dependencies and runtime settings. For example:

```yaml
name: huggingface-onnx

dependencies:
  - python=3.8
  - pytorch::pytorch
  - pip
  - transformers[onnx]
  - pip:
    - ipywidgets
```

## Supported with ready-made configurations
There are a few models that are supported right away with configurations, which means that it will be easy to port an existing Hugging Face model over to ONNX.

Some of the popular models are:

- BART
- BERT
- Data2VecText
- Data2VecVision
- DistilBERT
- OpenAI GPT-2
- RoBERTa
- T5
- Whisper
- YOLOS

## Configs
Configurations are important because they allow you correctly interact and map with the resulting model. Hugging Face already includes ready-to-use configurations for the popular models, so no need to figure out how that mapping should go.

## Suggested reading
Learn more about some other options and other supported serialization to ONNX in the [Hugging Face Transformers Serialization](https://huggingface.co/docs/transformers/serialization) documentation.

# Exporting Hugging Face models to ONNX
You can use both Python modules used as a command-line tool or use the libraries directly. This notebook will explore how to export using the `transformers.onnx` module as a CLI and then consume that resulting model with Hugging Face and the `onnxruntime` library.

## Find the features
List the available features for a specific model. You can then use that feature when exporting to ONNX.

## Explore and further reading
Go through the ONNX models and how they can work with the `onnxruntime` in the [ONNX Zoo](https://github.com/onnx/models)

