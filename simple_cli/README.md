# jformat

A simple command-line tool to format JSON files and print the formatted output to stdout.

Built with Python and Click.

## Features

- Format JSON files with readable indentation
- Print formatted JSON directly to the terminal
- Optional sorting of JSON keys
- Simple CLI interface
- Installable as a global command

## Project Structure

```
jformat/
│
├── jformat/
│   ├── __init__.py
│   └── main.py
│
├── example.json
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/jvictorfranca/ML_Ops.git
cd jformat
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install the package:

```bash
pip install -e .
```

After installation, the `jformat` command will be available in your terminal.

---

## Usage

Format a JSON file:

```bash
jformat example.json
```

Example input (`example.json`):

```json
{
    "z": 42,
    "name": "jformat",
    "description": "A simple JSON formatter CLI tool",
    "version": "0.0.1",
    "author": {
        "name": "Joao Franca",
        "role": "developer"
    },
    "features": [
        "JSON formatting",
        "CLI interface",
        "key sorting"
    ],
    "active": true
}
```

Output:

```json
{
    "z": 42,
    "name": "jformat",
    "description": "A simple JSON formatter CLI tool",
    "version": "0.0.1",
    "author": {
        "name": "Joao Franca",
        "role": "developer"
    },
    "features": [
        "JSON formatting",
        "CLI interface",
        "key sorting"
    ],
    "active": true
}
```

---

## Sorting JSON Keys

By default, keys keep the same order as the original file.

To sort keys alphabetically, use:

```bash
jformat example.json --sort
```

or:

```bash
jformat example.json -s
```

Output:

```json
{
    "active": true,
    "author": {
        "name": "Joao Franca",
        "role": "developer"
    },
    "description": "A simple JSON formatter CLI tool",
    "features": [
        "JSON formatting",
        "CLI interface",
        "key sorting"
    ],
    "name": "jformat",
    "version": "0.0.1",
    "z": 42
}
```

---

## Options

### Sort JSON keys

```bash
--sort
```

Short version:

```bash
-s
```

Example:

```bash
jformat example.json -s
```

---

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run directly:

```bash
python jformat/main.py example.json
```

---

## Dependencies

- Python 3.10+
- Click
- Colorama

---

## License

This project is for educational purposes.