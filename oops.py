class employee:
    #special method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes")
        self.id = 123
        self.salary = 50000 
        self.designation = "Software Engineer"
        print("Finished executing attributes")

    def travel(self, dest):
        print("Started executing travel method")
        print(f"Employee is now travelling to {dest}")
        print("Finished executing travel method")
# Creating an object/instance of the class
sam = employee()


print(sam.id)

sam.travel("Dhaka")
print(type(sam))