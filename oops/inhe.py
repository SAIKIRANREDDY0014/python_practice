class Parent:
    message = "parent"
    def show(self):    #base class 
        print(f"this is a parent class ")

class Child(Parent):
    message = "child"
    def playgame(self):    #derived class
        print(f"playing a game as a {self.message}")        



a = Parent()
b = Child()

print(a.show(),b.show(),b.playgame(),a.message,b.message)