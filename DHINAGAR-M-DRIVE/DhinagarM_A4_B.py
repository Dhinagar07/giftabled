MY_NAME = "Dhinagar M"
class student:
    def __init__(self, name, marks):
        try:
            marks = int(marks)
            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100.")
            
            self.name = name
            self.__marks = marks
        except ValueError:
            print("Invalid marks. Please enter a valid number.")
            return

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Invalid marks.")

    def grade(self):
        if self.__marks >= 80:
            return "A"
        if self.__marks >= 60:
            return "B"
        if self.__marks >= 40:
            return "C"
        if self.__marks < 40:
            return "FAIL"

    def __str__(self):
        return f"Name: {self.name}, Marks: {self.__marks}, Grade: {self.grade()}"


print(student(MY_NAME, 85))

print(student("ram", 55))

print(student("san", 35))
s=student("man", 35)
s.set_marks(-45)

print(s)