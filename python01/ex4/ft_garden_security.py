class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}")

    def set_height(self, new_height):
        if new_height > 0:
            self.height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age):
        if new_age > 0:
            self.age = new_age
            print(f"Age updated: {new_age}cm [OK]")
        else:
            print(f"Invalid operation attempted: age {new_age}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.height

    def get_age(self):
        return self.age
    
    def current_infos(self):
        print(f"Current plant: {self.name} ({self.get_height()}cm, {self.get_age()} days)")
    

print("=== Garden Security System ===")

rose = SecurePlant("rose", 25, 30)

rose.set_age(-10)
rose.set_height(-5)
rose.current_infos()