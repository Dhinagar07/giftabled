class location:
    def __init__(self, name, description, key=None, code=None):
        self.name = name
        self.description = description
        self._key = key
        self.code = code

    def get_key(self):
        return self._key

    def visit(self):
        print(f"You are at {self.name}. {self.description}")
    
class canteen(location):
   def enter(self):
        self.visit()
        return self.get_key()

class Lab(location):
    def visit(self, key):
        if key == self._key:
            print(f"You are at {self.name}. {self.description}")
        else:
            print(key)
            print("You don't have the key to enter this location.")
    def enter(self, key):
        self.visit(key)
        return self.get_key()


bag = []
while True:
    print("Where would you like to go?")
    print("1. Canteen")
    print("2. Lab")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        canteen_location = canteen("Canteen", "A place to eat and relax.", key="--key-->")
        key = canteen_location.enter()
        if key:
            bag.append(key)
            print(f"Your key: {key}")
    elif choice == "2":
        key = bag[0] if bag else None
        lab_location = Lab("Lab", "A place for experiments and research.", key, code="1234")
        x=lab_location.enter(key)
        if x:
            print("you op[ebed chest abd wob tropy")
    elif choice == "3":
        print("Exiting the game.")
        break
    else:
        print("Invalid choice. Please try again.")