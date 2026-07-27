# Summarize CLI

A simple command-line tool that summarizes text using the **T5 Small** model from Hugging Face.

## Requirements

* Python 3.9+
* pip

---

# Installation

Clone the repository:

```bash
git clone https://github.com/jvictorfranca/ML_Ops.git
cd ML_Ops
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# Running without installing the package

You can execute the main script directly.

### Summarize a text file

```bash
python summarize/main.py --file example.txt
```

### Summarize a web page

```bash
python summarize/main.py --url https://en.wikipedia.org/wiki/Artificial_intelligence
```

---

# Installing as a CLI application

Install the project locally:

```bash
pip install .
```

Or install it in development mode:

```bash
pip install -e .
```

After installation, the `summarize` command will be available from your terminal.

### Summarize a text file

```bash
summarize --file example.txt
```

### Summarize a web page

```bash
summarize --url https://en.wikipedia.org/wiki/Artificial_intelligence
```

---

# Example

Create a file named `example.txt` and copy the sample text below into it.

Then run:

```bash
summarize --file example.txt
```

Or, if you have not installed the package:

```bash
python summarize/main.py --file example.txt
```

---

# Project structure

```text
ML_Ops/
│
├── summarize/
│   ├── __init__.py
│   └── main.py
│
├── requirements.txt
├── setup.py
└── README.md
```

---

# Technologies

* Python
* Click
* Hugging Face Transformers
* T5 Small
