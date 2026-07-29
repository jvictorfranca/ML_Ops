# MLflow Validation and Model Logging Examples

This project contains examples demonstrating how to use **MLflow** for:

- Data validation with metric tracking
- Logging a Hugging Face Transformer model
- Registering a model
- Serving the model using MLflow Model Serving

---

# Project Structure

```text
.
├── validate.py         # Dataset validation and MLflow metric logging
├── log_model.py        # Logs and registers the Hugging Face model
├── requirements.txt
└── README.md
```

---

# Prerequisites

Before running the project, make sure you have:

- Python 3.9+
- pip
- MLflow installed
- A running MLflow Tracking Server

---

# 1. Create a Virtual Environment

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

# 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 3. Start MLflow Tracking Server

Start the MLflow server:

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

In another terminal, activate the virtual environment:

```bash
.venv\Scripts\activate
```

Run:

```bash
python log_model.py
```

The script will:

- Download the `t5-small` model from Hugging Face
- Create an MLflow run
- Log the model
- Register the model as:

```
t5-small-summarizer
```

At the end, MLflow will print the Run ID:

Example:

```
50fc33a01db74d3796f677426634317d
```

---

# 5. Configure MLflow Tracking URI

Before serving the model, configure the MLflow Tracking Server for the current terminal session:

```bash
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```

For Windows PowerShell:

```powershell
$env:MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
```

---

# 6. Serve the Model

Start MLflow Model Serving:

```bash
mlflow models serve -m runs:/50fc33a01db74d3796f677426634317d/model --port 5001 --env-manager local
```

The model will be available at:

```
http://127.0.0.1:5001/invocations
```

---

# 7. Test Model Inference

Send a request to the model:

```bash
curl -X POST -H "Content-Type: application/json" --data '{"dataframe_split":{"columns":["text"],"data":[["Today is a perfect day to practice automation skills"]]}}' http://127.0.0.1:5001/invocations
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

The `validate.py` script performs basic data quality checks:

- Empty columns
- Columns with "Unnamed" names
- Fields containing carriage returns (`\r\n`)

Run:

```bash
python validate.py <metrics> <max_errors> <filename>
```

Example:

```bash
python validate.py True 10 dataset.csv
```

When metrics are enabled, MLflow logs:

- Number of unnamed columns
- Number of empty columns

---

# Technologies Used

- Python
- MLflow
- Pandas
- Click
- Hugging Face Transformers
- PyTorch

---

# Notes

The current model is based on `t5-small`.

Despite the example name, the model performs:

```
English → German translation
```

because the input prompt uses:

```
translate English to German:
```

inside the custom MLflow PyFunc model.