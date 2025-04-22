import json
import re
import logging
from typing import Any, Dict, List

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def to_sentence_case(text: str) -> str:
    """
    Convert a string to sentence case, preserving accents and handling multiple sentences.
    First letter of each sentence is capitalized, rest are lowercase.
    """
    if not text:
        return text

    # Split text into sentences based on common sentence-ending punctuation
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Process each sentence
    cleaned_sentences = []
    for sentence in sentences:
        if sentence:
            # Capitalize first letter, lowercase the rest, preserve accents
            cleaned = sentence[0].upper() + sentence[1:].lower()
            cleaned_sentences.append(cleaned)
    
    # Join sentences back together
    return ' '.join(cleaned_sentences)

def process_value(value: Any) -> Any:
    """
    Recursively process JSON values, converting strings to sentence case.
    Non-string values (lists, dicts, numbers, etc.) are processed appropriately.
    """
    if isinstance(value, str):
        return to_sentence_case(value)
    elif isinstance(value, dict):
        return {k: process_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [process_value(item) for item in value]
    else:
        return value

def clean_json(input_file: str, output_file: str) -> None:
    """
    Clean JSON file by converting text values to sentence case.
    """
    try:
        # Read the input JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Process the JSON data
        if isinstance(data, list):
            cleaned_data = [process_value(item) for item in data]
        elif isinstance(data, dict):
            cleaned_data = process_value(data)
        else:
            raise ValueError("JSON root must be a list or dict")

        # Save the cleaned JSON to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
        
        logger.info(f"Cleaned JSON saved to {output_file}")
    
    except FileNotFoundError:
        logger.error(f"Input file {input_file} not found")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format in {input_file}")
    except Exception as e:
        logger.error(f"Error processing JSON: {e}")

def main():
    input_file = r"C:\Users\victo\Desktop\CS\Job\rm_keys_null\cap_agde_clean.json"
    output_file = r"C:\Users\victo\Desktop\CS\Job\rm_keys_null\cap_agde_clean_sentence_case.json"
    clean_json(input_file, output_file)

if __name__ == "__main__":
    main()