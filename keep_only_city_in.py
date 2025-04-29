import json

with open(r'C:\Users\victo\Desktop\CS\Job\rm_keys_null\herault_clean_sentence_case.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# List of cities to exclude
included_cities = {"Cap-d'agde", "Agde", "La tamarissiere", "Le grau-d'agde", "Pezenas", "Portiragnes"}

# Filter out entries where city is in the excluded list
filtered_data = [item for item in data if item.get("city") in included_cities]

with open(r'C:\Users\victo\Desktop\CS\Job\rm_keys_null\cap_agde_only_filtered.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)
