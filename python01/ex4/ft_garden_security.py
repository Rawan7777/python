#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self._height = height
        self._age = age

    def set_height(self, new_height):
        if new_height > 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age
    
    def current_infos(self):
        print(f"Current plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)")

if __name__ == "__main__":

    print("=== Garden Security System ===")

    rose = SecurePlant("rose", 25, 30)

    print(f"Plant created: {rose.name}")

    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    rose.current_infos()