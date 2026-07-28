import mlflow

"""
For this to work, you'll need to point MLflow to a database and path. When running locally, you must do this otherwise you'll get into error conditions.
Start a server with:
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root /tmp/ --host 127.0.0.1:5000

The value of `--host` must match the tracking uri in the next cell.

"""


mlflow.set_tracking_uri("http://127.0.0.1:5000")
from mlflow import MlflowClient
client = MlflowClient()

# Create a new registered model
# this model must not exist already
client.create_registered_model("t5-onnx")

# Delete a registered model
client.delete_registered_model("t5-onnx")

# This should fail if there is no previous version created
client.update_model_version(
    name = "t5-small-summarizer",
    version = 1,
    description = "This is the T5 model in an ONNX version 1.6 using Opset 12"
)

client.delete_registered_model("t5-small-summarizer")