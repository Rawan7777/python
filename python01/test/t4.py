class Garden:
    def __init__(self, owner):
        self.owner = owner
    
    # def __add__(self, c):
    #         return "iugiuoubj"

    class Plant:
        def __init__(self, outer_instance):
            self.outer = outer_instance  # store reference to outer instance

        

        def show_owner(self):
            # Access outer instance's attribute
            print(f"The owner is {self.outer.owner}")

    def create_magic_object(self):
        self.object_in_class = self.Plant(self)
        self.object_in_class.show_owner()
        # print(dir(self.object_in_class))

# Usage
object_out_class = Garden("Alice")
object_out_classs = Garden(";kjb;")
object_out_class.create_magic_object()
c = object_out_class + object_out_classs
print(c)