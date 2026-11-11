import csv

FILE = "a2_28-09.csv"
 


def write_csv():
    rows = []
    for i in range(1, 11):
        roll_no = input(f"Enter roll number for student {i}: ").strip()
        name = input(f"Enter name for student {i}: ").strip()
        age = input(f"Enter age for student {i}: ").strip()
        course = input(f"Enter course for student {i}: ").strip()
        rows.append({"roll_no": roll_no, "name": name, "age": age, "course": course})

    with open(FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["roll_no", "name", "age", "course"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n{len(rows)} records written to {FILE}")


def read_csv():
    with open(FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("\n--- File contents ---")
        for row in reader:
            print(f"{row['roll_no']:>6} | {row['name']:<20} | {row['age']:>3} | {row['course']}")


write_csv()
read_csv()
