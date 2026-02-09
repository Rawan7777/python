#!/usr/bin/env python3

class SecurePlant:

    """Represents a plant with secure height and age attributes"""

    def __init__(self, name: str, height: int, age: int) -> None:

        """Initialize a SecurePlant instance.
        :param name: Name of the plant
        :param height: Height in centimeters
        :param age: Age in days"""

        self.name = name.capitalize()
        self._height = height
        self._age = age

    def set_height(self, new_height: int) -> None:

        """Safely update the plant's height.
        Rejects negative values"""

        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted:"
                  f" height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age: int) -> None:

        """Safely update the plant's age.
        Rejects negative values"""

        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {self._age} days [OK]")
        else:
            print(f"Invalid operation attempted:"
                  f" age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """Return the plant's current height"""
        return self._height

    def get_age(self) -> int:
        """Return the plant's current age"""
        return self._age


if __name__ == "__main__":

    print("=== Garden Security System ===")

    rose = SecurePlant("rose", 0, 0)
    print(f"Plant created: {rose.name}")

    rose.set_height(25)
    rose.set_age(30)

    print()
    rose.set_height(-5)
    print()

    print(f"Current plant: {rose.name} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")
