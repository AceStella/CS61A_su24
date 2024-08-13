class A:
    def __init__(self):
        print("A's __init__")

    def method(self):
        print("Method A")

class B(A):
    def __init__(self):
        super().__init__()  # Calls A's __init__
        print("B's __init__")

    def method(self):
        super().method()  # Calls A's method
        print("Method B")

class C(A):
    def __init__(self):
        super().__init__()  # Calls A's __init__
        print("C's __init__")

    def method(self):
        super().method()  # Calls A's method
        print("Method C")

class D(B, C):
    def __init__(self):
        super().__init__()  # Calls B's __init__, then C's __init__, then A's __init__
        print("D's __init__")

    def method(self):
        super().method()  # Calls B's method, which in turn calls A's method, then prints Method C and Method D

# Create an instance of D
d = D()
d.method()

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)  # Initialize base class Person
        self.job_title = job_title

class Manager(Employee):
    def __init__(self, name, job_title, department):
        super().__init__(name, job_title)  # Initialize base class Employee
        self.department = department

# Create an instance of Manager
manager = Manager("Alice", "Team Lead", "Engineering")

# Access attributes
print(f"Name: {manager.name}")         # From Person
print(f"Job Title: {manager.job_title}") # From Employee
print(f"Department: {manager.department}") # From Manager