class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []

    def pick_up(self, item):
        self.bag.append(item)
        print(f"  {self.name} picks up: {item}")

    def has_item(self, item):
        return item in self.bag

    def show_bag(self):
        if self.bag:
            print(f"  Bag: {', '.join(self.bag)}")
        else:
            print("  Bag: (empty)")


class Place:
    def __init__(self, name, required_item=None):
        self.name = name
        self.required_item = required_item
        self.locked = required_item is not None

    def enter(self, player):
        if not self.locked:
            print(f"  {player.name} enters {self.name}.")
            return True
        if player.has_item(self.required_item):
            self.locked = False
            print(f"  {player.name} uses the {self.required_item} to unlock the {self.name}.")
            print(f"  {player.name} enters {self.name}.")
            return True
        print(f"  {self.name} is locked. It needs: {self.required_item}.")
        return False


class Chest:
    def __init__(self, secret_code, treasure):
        self.secret_code = secret_code
        self.treasure = treasure
        self.opened = False

    def open(self, code):
        if self.opened:
            print(f"  Chest is already open. Treasure: {self.treasure}")
            return True
        if code == self.secret_code:
            self.opened = True
            print(f"  Correct code! The chest opens and reveals {self.treasure}.")
            return True
        print("  Wrong code! The chest stays shut.")
        return False


def ask(prompt):
    value = input(prompt).strip()
    while value == "":
        print("  Input cannot be empty.")
        value = input(prompt).strip()
    return value


def run_route(route, player_name, place_name, key_item, secret_code, treasure, wrong_code):
    print("=" * 50)
    print(f"ROUTE: {route.upper()}")
    print("=" * 50)

    player = Player(player_name)
    hall = Place("Hall")
    vault = Place(place_name, required_item=key_item)
    chest = Chest(secret_code=secret_code, treasure=treasure)

    hall.enter(player)
    player.show_bag()

    if route == "failed":
        print(f"\n1. Trying to enter the {place_name} without the {key_item}...")
        if not vault.enter(player):
            print(f"  FAILED: the {place_name} is locked and the {key_item} is missing.")

        print(f"\n2. Finding the {key_item} and unlocking the {place_name}...")
        player.pick_up(key_item)
        vault.enter(player)
        player.show_bag()

        print(f"\n3. Trying the wrong chest code ({wrong_code})...")
        chest.open(wrong_code)
        print("\nResult: FAILED ROUTE - the chest never opens, no treasure.")
        return False

    print("\n1. Looking around the hall...")
    player.pick_up(key_item)
    player.show_bag()

    print(f"\n2. Unlocking the {place_name} with the {key_item}...")
    if not vault.enter(player):
        print("\nResult: FAILED ROUTE - the place is locked.")
        return False

    print("\n3. Opening the chest with the correct code...")
    if not chest.open(secret_code):
        print("\nResult: FAILED ROUTE - the chest code was wrong.")
        return False

    print(f"\nResult: SUCCESS ROUTE - {player.name} escapes with {chest.treasure}!")
    return True


def main():
    print("=== ADVENTURE GAME SETUP ===")
    player_name = ask("Enter player name: ")
    place_name = ask("Enter locked place name: ")
    key_item = ask(f"Enter the item that unlocks the {place_name}: ")
    secret_code = ask("Set the chest secret code: ")
    treasure = ask("Enter the treasure inside the chest: ")

    wrong_code = ask("Enter a WRONG code for the failed route: ")
    while wrong_code == secret_code:
        print("  The wrong code must be different from the secret code.")
        wrong_code = ask("Enter a WRONG code for the failed route: ")

    print()
    run_route("failed", player_name, place_name, key_item, secret_code, treasure, wrong_code)
    print()
    run_route("success", player_name, place_name, key_item, secret_code, treasure, wrong_code)


if __name__ == "__main__":
    main()
