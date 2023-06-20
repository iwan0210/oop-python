class Man_Employee:
    suku = "Bugis"
    empCount = 0

    def __init__(self, name, age, agama, jnskel, alamat, status, salary):
        self.name = name
        self.age = age
        self.agama = agama
        self.jnskel = jnskel
        self.alamat = alamat
        self.status = status
        self.salary = salary
        Man_Employee.empCount += 1
    
    def displayCount(self):
        print("Total Employee %d" % Man_Employee.empCount)
    
    def displayEmployee(self):
        print("Name :", self.name, ", Salary :", self.salary)
    
    def biodata(self):
        return f"Nama: {self.name} \nUsia: {self.age} \nAgama: {self.agama} \nJenis Kelamin: {self.jnskel} \nAlamat: {self.agama} \nStatus: {self.status} \nGaji: {self.salary}"
    
tes_qois = Man_Employee("Ageng", 22, "Agama", "Laki-laki", "Batang", "Jomblo", 1000000)
print(tes_qois.biodata())
print("Suku: ", tes_qois.suku)

tes_qois.displayEmployee()
tes_qois.displayEmployee()
print("total Employee: %d" % Man_Employee.empCount)