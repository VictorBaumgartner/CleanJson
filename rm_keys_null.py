import json

# Charger le fichier JSON d'origine
with open(r"C:\Users\victo\Desktop\CS\Job\rm_keys_null\herault_json.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Traitement : retirer les "null" et aplatir les objets "row_to_json"
cleaned_data = []
for item in data:
    row = item.get("row_to_json", {})
    if isinstance(row, dict):
        cleaned_row = {k: v for k, v in row.items() if v is not None}
        if cleaned_row:
            cleaned_data.append(cleaned_row)

# Sauvegarder dans un nouveau fichier
with open(r"C:\Users\victo\Desktop\CS\Job\rm_keys_null\resultats_herault_clean.json", "w", encoding="utf-8") as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=2)

print("✅ Nettoyage terminé !")
