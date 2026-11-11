import csv
import json

try:
    txt_name = input("Enter name : ").strip()
    with open("a4_28-09.txt", "w", encoding="utf-8") as file:
        for i in range(2):
            file.write(txt_name + " " + str(i + 1) + "\n")
    with open("a4_28-09.txt", "r", encoding="utf-8") as file:
        print(" file:", file.read().splitlines())
except ValueError:
    print("ValueError: invalid value entered")
except FileNotFoundError:
    print("FileNotFoundError: text file not found")

try:
    csv_name = input("Enter a namee: ").strip()
    csv_age = int(input("Enter an age  "))
    with open("a4_28-09.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": csv_name, "age": csv_age})
    with open("a4_28-09.csv", "r", newline="", encoding="utf-8") as file:
        print("CSV file:", list(csv.DictReader(file)))
except ValueError:
    print("ValueError: invalid value entered")
except FileNotFoundError:
    print("FileNotFoundError: csv file not found")

try:
    json_name = input("Enter a name : ").strip()
    json_age = int(input("Enter a age : "))
    data = {"name": json_name, "age": json_age}
    with open("a4_28-09.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    with open("a4_28-09.json", "r", encoding="utf-8") as file:
        print("JSON file:", json.load(file))
except ValueError:
    print("ValueError: invalid value entered")
except FileNotFoundError:
    print("FileNotFoundError: json file not found")
finally:
    print("Program finished")
