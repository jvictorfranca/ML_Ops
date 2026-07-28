import mlflow
from mlflow import log_metric
from random import choice

# Log parameters (key-value pairs)
mlflow.log_param("num_dimensions", 8)
mlflow.log_param("regularization", 0.1)

# Log a metric; metrics can be updated throughout the run
mlflow.log_metric("accuracy", 0.1)
...
mlflow.log_metric("accuracy", 0.45)

# Log artifacts (output files)
mlflow.log_artifact("roc.png")

# Log metrics in a loop

metric_names = ["cpu", "ram", "disk"]

percentages = [i for i in range(0, 100)]

for i in range(40):
    log_metric(choice(metric_names), choice(percentages))