

students = []
for i in range(10):
    name = input(f"Enter student {i + 1} name: ").strip()
    students.append(name)

with open("students.txt", "w", encoding="utf-8") as file:
    for name in students:
        file.write(name + "\n")

print(f"\n names written to {FILE}")
for i, name in enumerate(students, start=1):
    print(f"{i}. {name}")
