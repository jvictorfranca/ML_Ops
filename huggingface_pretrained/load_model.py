"""
Loading a model from a local directory.
"""

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

INPUT_FILE = "example.txt"

model = AutoModelForSeq2SeqLM.from_pretrained("summarizeApp")
tokenizer = AutoTokenizer.from_pretrained("summarizeApp")

with open(INPUT_FILE, encoding="utf-8") as f:
    text = f.read()

input_ids = tokenizer.encode(text, return_tensors="pt")
outputs = model.generate(input_ids)

summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(summary)