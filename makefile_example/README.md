# Python Project

This project uses a **Makefile** to automate common development tasks such as installing dependencies, formatting code, running static analysis, and executing tests.

## Prerequisites

Before getting started, make sure you have the following installed:

- Python 3.x
- pip
- make

### Linux

The `make` utility is usually pre-installed. If not, install it with:

```bash
sudo apt install make
```

### Windows

You can use one of the following options:

- Git Bash (Git for Windows)
- Windows Subsystem for Linux (WSL)
- Chocolatey:

```powershell
choco install make
```

---

## Installation

Clone the repository and run:

```bash
make install
```

This command:

- Upgrades `pip`;
- Installs all dependencies listed in `requirements.txt`.

Equivalent commands:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Available Commands

### Install Dependencies

```bash
make install
```

Installs all required project dependencies.

---

### Run Tests

```bash
make test
```

Runs the test suite using **pytest** with verbose output.

---

### Format Code

```bash
make format
```

Formats all Python files in the project using **Black**.

---

### Run Linter

```bash
make lint
```

Analyzes `hello.py` using **Pylint**, while disabling convention (`C`) and refactoring (`R`) messages.

---

### Run All Tasks

```bash
make all
```

Executes the following commands in sequence:

1. Install dependencies
2. Run the linter
3. Execute the test suite

---

## Makefile

```Makefile
install:
	pip install --upgrade pip &&
	pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test
```

Each section defines a **target** that can be executed with the `make` command.

For example:

- `install` installs project dependencies.
- `test` runs the test suite.
- `format` formats the source code.
- `lint` performs static code analysis.
- `all` executes multiple targets in sequence.

---

## Creating a Makefile

Create a file named exactly:

```
Makefile
```

> The file name must start with a capital **M** and **must not have a file extension**.

Then, define your targets. For example:

```Makefile
hello:
	echo "Hello, World!"
```

Run the target with:

```bash
make hello
```

Output:

```
Hello, World!
```

You can add as many targets as needed to automate your development workflow.