# MLflow Validation and Model Serving Examples

This project demonstrates how to use **MLflow** for:

- Dataset validation
- MLflow metric tracking
- Logging Hugging Face Transformer models
- Registering models in MLflow Model Registry
- Serving models using MLflow Model Serving
- Running workflows using MLflow Projects

---

# Project Structure

```text
.
├── validate.py         # Dataset validation and MLflow metric logging
├── log_model.py        # Logs and registers the Hugging Face model
├── MLproject           # MLflow Project configuration
├── conda.yaml          # MLflow environment configuration
├── requirements.txt
└── README.md
```

---

# Prerequisites

Before running the project, make sure you have:

- Python 3.9+
- pip
- MLflow installed

---

# 1. Create Virtual Environment

## Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 2. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# 3. Start MLflow Tracking Server

Start the MLflow tracking server:

```bash
mlflow server --host 127.0.0.1 --port 5000
```

The MLflow UI will be available at:

```
http://127.0.0.1:5000
```

Keep this terminal running.

---

# 4. Log and Register the Model

Open another terminal and activate the environment:

```bash
.venv\Scripts\activate
```

---

## Running Directly with Python

Execute:

```bash
python log_model.py
```

The script will:

1. Download the `t5-small` model from Hugging Face
2. Create an MLflow run
3. Log the PyFunc model
4. Register the model in MLflow Model Registry

The registered model name will be:

```
t5-small-summarizer
```

Example output:

```
Successfully registered model 't5-small-summarizer'.

Created version '1' of model 't5-small-summarizer'.
```

The script will also print the Run ID:

Example:

```
50fc33a01db74d3796f677426634317d
```

---

# 5. Run Using MLflow Projects

The project can also be executed using the `MLproject` file.

Run:

```bash
mlflow run . -e log_model
```

This executes:

```bash
python log_model.py
```

through MLflow Projects.

---

# 6. Configure MLflow Tracking URI

Before serving the model, configure the MLflow Tracking Server.

## Bash / Git Bash

```bash
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```

## Windows PowerShell

```powershell
$env:MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
```

---

# 7. Serve the Model

Use the Run ID generated when logging the model.

Example:

```
50fc33a01db74d3796f677426634317d
```

Start MLflow Model Serving:

```bash
MLFLOW_TRACKING_URI=http://127.0.0.1:5000 mlflow models serve -m runs:/50fc33a01db74d3796f677426634317d/model --port 5001 --env-manager local
```

The model API will be available at:

```
http://127.0.0.1:5001/invocations
```

---

# 8. Test Model Inference

Send a request using curl:

```bash
curl -X POST \
-H "Content-Type: application/json" \
--data '{"dataframe_split":{"columns":["text"],"data":[["Today is a perfect day to practice automation skills"]]}}' \
http://127.0.0.1:5001/invocations
```

Expected response:

```json
{
  "predictions": [
    "Heute ist ein perfekter Tag, um Automatisierungsfähigkeiten zu üben."
  ]
}
```

---

# Dataset Validation

The `validate.py` script performs basic data quality validation.

It checks:

- Empty columns
- Columns containing `"Unnamed"`
- Fields containing carriage returns (`\r\n`)

---

## Run Validation Directly

```bash
python validate.py True 10 dataset.csv
```

Parameters:

| Parameter | Description |
|---|---|
| metrics | Enable MLflow metric logging |
| max_errors | Maximum number of allowed errors |
| filename | Dataset file path |

When metrics are enabled, MLflow logs:

```
unnamed
zero_count_columns
```

---

# Run Validation Using MLflow Projects

The validation workflow is also available through `MLproject`.

Example:

```bash
mlflow run . -e validate -P metrics=True -P max_errors=10 -P filename=dataset.csv
```

This executes:

```bash
python validate.py True 10 dataset.csv
```

---

# MLproject Configuration

The project contains two MLflow entry points.

## log_model

Responsible for logging and registering the Transformer model.

Run:

```bash
mlflow run . -e log_model
```

Equivalent command:

```bash
python log_model.py
```

---

## validate

Responsible for dataset validation.

Parameters:

```yaml
metrics
max_errors
filename
```

Example:

```bash
mlflow run . -e validate -P metrics=True -P max_errors=10 -P filename=dataset.csv
```

---

# Technologies Used

- Python
- MLflow
- Pandas
- Click
- Hugging Face Transformers
- PyTorch

---

# Model Information

Registered model:

```
t5-small-summarizer
```

Base model:

```
t5-small
```

from Hugging Face.

Despite the project name, the current implementation performs:

```
English → German translation
```

The model receives the prompt:

```
translate English to German:
```

before generating the output.

---

# Complete Workflow

```
MLproject
    |
    v
mlflow run . -e log_model
    |
    v
log_model.py
    |
    v
MLflow Run
    |
    v
Registered Model
    |
    v
mlflow models serve
    |
    v
REST API
    |
    v
curl request
```