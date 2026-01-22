class MathUtils:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    @staticmethod
    def add(a, b):
        return a + b
    
    
print(MathUtils.add(3, 5))

m = MathUtils("x", 1, 1)
print(m.add(3, 5))
