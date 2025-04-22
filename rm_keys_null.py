import json

# Charger les données depuis le fichier JSON
with open(r"C:\Users\victo\Desktop\CS\Job\rm_keys_null\herault_json.json", "r", encoding="utf-8") as file:
    data = json.load(file)

cleaned_data = []

for item in data:
    row = item.get("row_to_json", {})
    
    if isinstance(row, dict):
        # Supprimer les champs avec valeurs nulles, vides ou listes vides
        filtered = {k: v for k, v in row.items() if v not in [None, "", []]}

        # Vérifie si le titre est présent et non vide
        has_title = "title" in filtered and filtered["title"].strip() != ""

        # Vérifie si la row contient plus que juste "id" ou "id" + "activities"
        keys = list(filtered.keys())
        valid_content = len(keys) > 1 and not (len(keys) == 2 and "id" in keys and "activities" in keys)

        if has_title and valid_content:
            cleaned_data.append(filtered)

# Sauvegarder le JSON nettoyé
with open(r"C:\Users\victo\Desktop\CS\Job\rm_keys_null\resultats_herault_clean.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=2)

print("✅ Nettoyage terminé. Fichier sauvegardé : resultats_jobs_clean.json")
