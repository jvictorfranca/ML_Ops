# MLflow Basics Example

This project demonstrates how to use **MLflow** to track Machine Learning experiments using an **ElasticNet** regression model trained on the **Wine Quality** dataset.

## Project Structure

```text
.
├── basics_example.py      # Model training and MLflow tracking
├── logging.py             # Examples of logging parameters, metrics, and artifacts
├── run_model.py           # Example of loading and running predictions
├── MLproject              # MLflow Project configuration
├── wine-quality.csv       # Dataset
├── requirements.txt
└── README.md
```

---

## Prerequisites

Before running the project, make sure you have:

- Python 3.9 or higher
- pip

---

## 1. Create a Virtual Environment (Optional but Recommended)

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 2. Install the Dependencies

Install all required packages by running:

```bash
pip install -r requirements.txt
```

---

## 3. Create an MLflow Experiment

Before running the training script, create an experiment named **produce-metrics**:

```bash
mlflow experiments create --experiment-name produce-metrics
```

If you want all runs to be automatically logged to this experiment, add the following line to `basics_example.py` before `mlflow.start_run()`:

```python
mlflow.set_experiment("produce-metrics")
```

---

## 4. Run the Training Script

### Using the Default Parameters

```bash
python basics_example.py
```

### Specifying Hyperparameters

```bash
python basics_example.py 0.5 0.5
```

Where:

- First argument → `alpha`
- Second argument → `l1_ratio`

Example:

```bash
python basics_example.py 0.8 0.3
```

During execution, MLflow will log:

- Model parameters
- Evaluation metrics (RMSE, MAE, and R²)
- Trained model

---

## 5. View the Experiments

Start the MLflow UI:

```bash
mlflow ui
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

From the MLflow interface, you can explore:

- Experiments
- Runs
- Parameters
- Metrics
- Registered models
- Artifacts

---

## 6. Run Predictions Using a Saved Model

Open `run_model.py` and replace:

```python
logged_model = "runs:/<RUN_ID>/model"
```

with the **Run ID** generated after training.

Then run:

```bash
python run_model.py
```

The script demonstrates how to make predictions using:

- Pandas DataFrames
- Spark DataFrames (Spark UDF)

---

## File Descriptions

### `basics_example.py`

Responsible for:

- Loading the dataset
- Training an ElasticNet model
- Computing evaluation metrics
- Logging parameters, metrics, and the trained model to MLflow

---

### `logging.py`

Contains examples of how to use the MLflow API to log:

- Parameters
- Metrics
- Artifacts

---

### `run_model.py`

Demonstrates how to:

- Load a model logged with MLflow
- Run predictions using a Pandas DataFrame
- Run predictions using a Spark DataFrame

---

### `MLproject`

Configuration file used by **MLflow Projects** for standardized project execution.

Run the project with:

```bash
mlflow run .
```

---

## Technologies Used

- Python
- MLflow
- Pandas
- NumPy
- Scikit-learn
- PySpark (for Spark prediction examples)

---

## Dataset

This project uses the **Wine Quality** dataset, available at:

http://archive.ics.uci.edu/ml/datasets/Wine+Quality
```