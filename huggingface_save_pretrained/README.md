# Text Summarizer with Hugging Face Transformers

This project demonstrates how to download a Hugging Face summarization model, save it locally, and use it to generate text summaries.

## Project Structure

```text
.
├── save_model.py
├── load_model.py
├── example.txt
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Download the Model

Run the following command:

```bash
python save_model.py
```

This script downloads the pretrained summarization model from Hugging Face and saves it locally for future use.

---

## Example Input

The project includes an `example.txt` file containing sample text for testing.

You can replace its contents with your own text if you'd like to summarize something different.

---

## Generate a Summary

Run:

```bash
python load_model.py
```

The script will:

- Load the locally saved model.
- Read the contents of `example.txt`.
- Generate a summary.
- Print the result to the console.

---

## Example Output

**Input**

```text
Artificial Intelligence (AI) is transforming industries across the world by automating repetitive tasks, improving decision-making, and enabling innovative solutions through machine learning and deep learning.
```

**Output**

```text
Artificial Intelligence is transforming industries by automating tasks and improving decision-making.
```

---

## Technologies

- Python
- PyTorch
- Hugging Face Transformers

---

## License

This project is available for educational and learning purposes.