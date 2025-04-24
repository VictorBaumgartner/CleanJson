
# 🧼 JSON Data Cleaner

## 🔍 Overview

**JSON Data Cleaner** is a Python utility script to **sanitize and standardize JSON files**, especially useful for data preprocessing in data pipelines, APIs, or datasets collected from user inputs or web scraping.

It performs:

✅ Removal of empty values: `null`, `[]`, `"[]"`  
✅ Sentence case transformation of strings (while **preserving accents**)  
✅ Unicode normalization for consistent storage and searchability

---

## 📁 Input Example

```json
{
  "name": "josé DURAND",
  "bio": "[]",
  "hobbies": null,
  "skills": [],
  "location": "PARIS, FRANCE"
}
```

---

## ✅ Output Example

```json
{
  "name": "José durand",
  "location": "Paris, france"
}
```

---

## ⚙️ Features

- **Empty Detection**: Recognizes and removes `"[]"`, `[]`, and `null` values.
- **Unicode-Safe Normalization**: Keeps accented characters like `é`, `ç`, `à`, etc.
- **Sentence Case**: Applies sentence casing to strings (`"hello WORLD"` → `"Hello world"`).
- **Recursive Cleaning**: Works on deeply nested JSON objects or arrays.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/json-data-cleaner.git
   cd json-data-cleaner
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Dependencies are minimal:
```txt
Unidecode==1.3.6
```

---

## 🧪 Usage

```bash
python clean_json.py --input input.json --output cleaned.json
```

### Options

| Flag        | Description                  |
|-------------|------------------------------|
| `--input`   | Path to the original JSON    |
| `--output`  | Path to save the cleaned JSON |

---

## 🧠 How It Works (Core Logic)

```python
import json
import unicodedata

def is_empty(value):
    return value in (None, [], "[]")

def to_sentence_case(text):
    if not isinstance(text, str) or not text.strip():
        return text
    normalized = unicodedata.normalize('NFC', text.strip())
    return normalized[0].upper() + normalized[1:].lower()

def clean_json(data):
    if isinstance(data, dict):
        return {
            key: clean_json(value)
            for key, value in data.items()
            if not is_empty(value)
        }
    elif isinstance(data, list):
        cleaned = [clean_json(item) for item in data if not is_empty(item)]
        return cleaned if cleaned else None
    elif isinstance(data, str):
        return to_sentence_case(data)
    return data
```

---

## 📂 Example Script: `clean_json.py`

```python
import json
import argparse
from cleaner import clean_json  # The core logic is in cleaner.py

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean and normalize JSON data.")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output cleaned JSON file")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    cleaned = clean_json(data)

    with open(args.output, "w", encoding="utf-8") as outfile:
        json.dump(cleaned, outfile, indent=4, ensure_ascii=False)

    print("✅ JSON cleaned and saved to", args.output)
```

---

## 🧪 Test Case

```bash
echo '{"title": "BONJOUR LE MONDE", "empty": [], "bio": "[]", "city": "lyon"}' > test.json
python clean_json.py --input test.json --output result.json
```

Result:
```json
{
  "title": "Bonjour le monde",
  "city": "Lyon"
}
```

---

## 🧊 Tips

- 🔁 You can plug this into a pipeline to auto-clean datasets before ingestion.
- 🌍 It supports UTF-8, so it works with French, Spanish, Vietnamese, etc.
- 🧩 Easily extendable: Add slugify, deduplication, or language detection.

---

## 📄 License

MIT License – feel free to use, improve, and share!
