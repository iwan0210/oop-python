class Employee:
    #Common base class for all employee
    empCount = 0

    def __init__(self, name, salary, age, agama, jnskel, alamat, status):
        self.name = name
        self.salary = salary
        self.age = age
        self.jnskel = jnskel
        self.agama = agama
        self.alamat = alamat
        self.status = status
        Employee.empCount += 1

    def displayCount(self):
        print(f"Total Employee {self.empCount}")

    def dislayEmployee(self):
        print(f"Name : {self.name}, Salary : {self.salary}")

    def biodata(self):
        return f"Nama: {self.name} \nUsia: {self.age} \nAgama: {self.agama} \nJenis Kelamin: {self.jnskel} \nAlamat: {self.alamat} \nStatus: {self.status}"

empArief = Employee("Arief", 1000000, 22, "Islam", "Laki-laki", "Pekalongan", "Jomblo")
empYasir = Employee("Yasir", 2000000, 33, "Islam", "Laki-laki", "Batang", "Menikah")
empArief.dislayEmployee()
print(empArief.biodata())
empYasir.dislayEmployee()
print(empYasir.biodata())
print(f"Total Employee {Employee.empCount}")