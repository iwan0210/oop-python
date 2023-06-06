class Employee:
    #Common base class for all employee
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(f"Total Employee {self.empCount}")

    def dislayEmployee(self):
        print(f"Name : {self.name}, Salary : {self.salary}")


empArief = Employee("Arief", 1000000)
empYasir = Employee("Yasir", 2000000)
empArief.dislayEmployee()
empYasir.dislayEmployee()
print(f"Total Employee {Employee.empCount}")