import json

data = {
    "name": "Aarav",
    "roll_number": 101,
    "age": 20,
    "department": "CA",
}

with open("a3_28-09.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

with open("a3_28-09.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded)
