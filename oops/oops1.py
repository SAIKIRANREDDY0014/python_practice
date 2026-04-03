class Employee:
    name = "sai"
    age = 22
    sal = 100000
    def greet(self):
        print("heello there")

e1 = Employee()
# print(e1.name) 
# del e1
print(e1.name) 
# del e1.greet
e1.greet()
# del e1.age