# Example Hugging Face Dataset Loader

This repository provides a minimal example of a custom dataset loading script for the Hugging Face `datasets` library.

It demonstrates how to implement a `GeneratorBasedBuilder` with custom dataset features, split generation, and example loading.

## Usage

```python
from datasets import load_dataset

dataset = load_dataset("YOUR_USERNAME/YOUR_REPO")
```

## Repository Structure

```
.
├── example_dataset.py
├── README.md
└── (optional example data files)
```

## Note

This repository is intended **only as an example** of a custom dataset loader.

For most datasets, the recommended approach is **not** to write a loading script. Instead, upload your dataset directly as **JSON**, **JSONL**, **CSV**, or **Parquet** files. The Hugging Face Hub can automatically detect these formats, allowing users to load the dataset without any custom Python code.

Official documentation:
- https://huggingface.co/docs/datasets/main/en/repository_structure

## License

MIT