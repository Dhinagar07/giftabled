import csv
try:
    with open("partD.csv", "r", newline="", encoding="utf-8") as file:
        d = csv.DictReader(file)
        
        for row in d:
            print(row)
            if 0 <= int(row["Mark"]) <= 100:
                print(f"Name: {row['Name']}, Mark: {row['Mark']}")
            else:
                raise ValueError("Mark must be between 0 and 100.")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except ValueError as e:
    print(f"Value error: {e}")