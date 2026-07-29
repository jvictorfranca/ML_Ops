# MLflow Basics Example

This project demonstrates how to use **MLflow** to track Machine Learning experiments using an **ElasticNet** regression model trained on the **Wine Quality** dataset.

The project covers:

- Training a Machine Learning model
- Tracking experiments with MLflow
- Logging parameters and metrics
- Saving trained models
- Running MLflow Projects with `MLproject`
- Loading saved models for inference

---

# Project Structure

```text
.
├── basics_example.py      # Model training and MLflow tracking
├── logging.py             # Examples of MLflow logging API
├── run_model.py           # Example of loading and predicting with a saved model
├── MLproject              # MLflow Project configuration
├── conda.yaml             # MLflow environment configuration
├── wine-quality.csv       # Dataset
├── requirements.txt
└── README.md
```

---

# Prerequisites

Before running the project, make sure you have:

- Python 3.9 or higher
- pip
- MLflow installed

---

# 1. Create a Virtual Environment

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

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# 3. Create an MLflow Experiment

Create an experiment called `produce-metrics`:

```bash
mlflow experiments create --experiment-name produce-metrics
```

To automatically send runs to this experiment, add:

```python
mlflow.set_experiment("produce-metrics")
```

before:

```python
with mlflow.start_run():
```

inside `basics_example.py`.

---

# Running the Project Using Python

This is the direct execution method.

---

## 4. Run Training With Default Parameters

```bash
python basics_example.py
```

Default values:

```text
alpha = 0.5
l1_ratio = 0.5
```

---

## 5. Run Training With Custom Hyperparameters

You can specify ElasticNet parameters:

```bash
python basics_example.py <alpha> <l1_ratio>
```

Example:

```bash
python basics_example.py 0.8 0.3
```

Where:

| Parameter | Description |
|---|---|
| alpha | Regularization strength |
| l1_ratio | Balance between L1 and L2 regularization |

During execution MLflow logs:

- Model parameters
- RMSE
- MAE
- R² score
- Trained model artifact

---

# Running the Project Using MLflow Projects

The `MLproject` file allows standardized execution using MLflow.

The current MLproject configuration exposes:

```yaml
main:
  parameters:
    alpha
    l1_ratio
```

---

## 6. Run With Default Parameters

```bash
mlflow run .
```

Equivalent to:

```bash
python basics_example.py 0.5 0.5
```

---

## 7. Run With Custom Parameters

Using MLflow parameters:

```bash
mlflow run . -P alpha=0.8 -P l1_ratio=0.3
```

MLflow will create a new run containing:

```
Experiment
    |
    +-- Run 1
    |     alpha=0.5
    |     l1_ratio=0.5
    |
    +-- Run 2
          alpha=0.8
          l1_ratio=0.3
```

This allows comparison between different model configurations.

---

# 8. Start MLflow UI

To visualize experiments:

```bash
mlflow ui
```

Open:

```
http://127.0.0.1:5000
```

The MLflow interface allows you to inspect:

- Experiments
- Runs
- Parameters
- Metrics
- Artifacts
- Logged models

---

# 9. Running Predictions With a Saved Model

After training, MLflow generates a Run ID:

Example:

```
50fc33a01db74d3796f677426634317d
```

Open:

```python
run_model.py
```

Update:

```python
logged_model = "runs:/<RUN_ID>/model"
```

Example:

```python
logged_model = "runs:/50fc33a01db74d3796f677426634317d/model"
```

Then run:

```bash
python run_model.py
```

The script demonstrates loading the MLflow model and performing predictions.

---

# File Descriptions

## basics_example.py

Main training script.

Responsibilities:

- Load Wine Quality dataset
- Split data into training and testing datasets
- Train an ElasticNet regression model
- Evaluate the model
- Log parameters, metrics, and model artifacts into MLflow

Logged parameters:

```
alpha
l1_ratio
```

Logged metrics:

```
RMSE
MAE
R²
```

---

## logging.py

Demonstrates MLflow logging capabilities.

Examples:

### Logging parameters

```python
mlflow.log_param("num_dimensions", 8)
```

### Logging metrics

```python
mlflow.log_metric("accuracy", 0.45)
```

### Logging artifacts

```python
mlflow.log_artifact("roc.png")
```

---

## run_model.py

Demonstrates:

- Loading a model stored in MLflow
- Running predictions with Pandas
- Running predictions with Spark UDF

---

## MLproject

Defines how the project can be executed through MLflow Projects.

Example:

```bash
mlflow run .
```

The project parameters are:

```yaml
alpha:
  type: float
  default: 0.5

l1_ratio:
  type: float
  default: 0.5
```

Execution command:

```yaml
python basics_example.py {alpha} {l1_ratio}
```

---

# Technologies Used

- Python
- MLflow
- Pandas
- NumPy
- Scikit-learn
- PySpark

---

# Dataset

This project uses the **Wine Quality** dataset.

Dataset source:

```
http://archive.ics.uci.edu/ml/datasets/Wine+Quality
```

Reference:

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.

"Modeling wine preferences by data mining from physicochemical properties."

Decision Support Systems, Elsevier, 47(4):547-553, 2009.