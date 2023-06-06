class Manusia:
    #Class attribute
    suku = "Jawa"

    def __init__(self, name, age, agama, jnskel, alamat, status):
        self.name = name
        self.age = age
        self.jnskel = jnskel
        self.agama = agama
        self.alamat = alamat
        self.status = status

    def biodata(self):
        return f"Nama: {self.name} \nUsia: {self.age} \nAgama: {self.agama} \nJenis Kelamin: {self.jnskel} \nAlamat: {self.alamat} \nStatus: {self.status}"
    
test_arief = Manusia("Arief", 22, "Islam", "Laki-laki", "Pekalongan", "Jomblo")
print(test_arief.biodata())
print("Suku: ", test_arief.suku)