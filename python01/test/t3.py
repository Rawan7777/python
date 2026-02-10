class Garden:
    def __init__(self, owner):
        self.owner = owner

    class Plant:
        def __init__(self, outer):
            self.outer = outer


g = Garden("Alice")
p = g.Plant(g)

print("I know the object where:", p.__dict__)
# Output:
# I know the object where: {'outer': <__main__.Garden object at 0x7fea40c5f230>}

