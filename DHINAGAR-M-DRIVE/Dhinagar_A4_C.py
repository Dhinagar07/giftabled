import pickle
import csv
import json
from DhinagarM_A4_B import Student
MY_NAME = "Dhinagar M"
d={}
for i in range(3):
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    d[i] = Student(name, marks)

def textfile():
    with open("Dhinagar_A4_C.txt", "w", encoding='utf-8') as f:
        for key in d:
            f.write(f"{d[key].name} , {d[key].get_marks()}\n")
        print("dumped as text")

    with open("Dhinagar_A4_C.txt", "r", encoding='utf-8') as f:
        
        print("loaded text\n")
        for line in f:
            print(line.strip())

def csvfile():

    with open("Dhinagar_A4_C.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "marks"])
        writer.writeheader()
        for key in d:
            writer.writerow({"name": d[key].name, "marks": d[key].get_marks()})
        print("dumped as CSV")

    with open("Dhinagar_A4_C.csv", "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        print("loaded CSV\n")
        for row in reader:
            print(f"{row}")

def jsonfile():
    
    with open("Dhinagar_A4_C.json", "w", encoding='utf-8') as f:
        json.dump({key: {"name": d[key].name, "marks": d[key].get_marks()} for key in d}, f)
        print("dumped as JSON")

    with open("Dhinagar_A4_C.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        print("loaded JSON\n")
        print(data)
    
def binfile():

    with open("Dhinagar_A4_C.bin", "wb") as f:
        pickle.dump(d, f)
        print("dumped as bin")

    with open("Dhinagar_A4_C.bin", "rb") as f:
        q=pickle.load(f)
        print("loaded from bin")

    for key in q:
        print(f"{key} : {d[key]}")

textfile()
csvfile()
jsonfile()
binfile()