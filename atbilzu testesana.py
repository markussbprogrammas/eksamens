class Transportlidzeklis:
    def __init__(self, zimols, modelis, reg_datums, pilna_masa, degvielas_veids):
        self.zimols = zimols
        self.modelis = modelis
        self.reg_datums = reg_datums
        self.pilna_masa = pilna_masa
        self.degvielas_veids = degvielas_veids

    def __str__(self):
        return f"{self.zimols} {self.modelis} {self.reg_datums} {self.pilna_masa} {self.degvielas_veids}" 

    def __del__(self):
        print(f"'{self.zimols} {self.modelis} {self.reg_datums} {self.pilna_masa} {self.degvielas_veids} ' is being destroyed") 

auto = Transportlidzeklis("AUDI","A4","22.10.2019","1800","BG")

print(auto)
del auto



class Kubs:
    def __init__(self, malas_garums, krasa):
        self.malas_garums = malas_garums
        self.krasa = krasa
        if self.malas_garums not in range(2,11):
            self.malas_garums = 2

    def __del__(self):
        print(f"Izdzēsts {self.krasa}objekts")
        pass

    def aprekinat_tilpumu(self):
        tilpums = self.malas_garums ** 3
        return tilpums

class Bloks(Kubs):
    def __init__(self, malas_garums,krasa, kubu_skaits, forma):
        super().__init__(malas_garums,krasa)
        self.__kubu_skaits = kubu_skaits

        if forma in [11, 12, 13, 14, 22]:
            self.derigums = 0
        else:
            print("Bloks nederīgs")
            self.derigums = 1

        if self.__kubu_skaits not in range(1, 5):
            print("Neatbilst nosacījumiem,kubu skaits blokā nav no 1 līdz 4")
    def tilpums(self):
        return ((self.__kubu_skaits * self.malas_garums)**3)        
kubg = Kubs(10, "zaļš")
kubr = Kubs(1, "sarkans")

print(kubg.krasa, kubg.aprekinat_tilpumu())
print("kubr malas garums", kubr.malas_garums)
del(kubr)
print("kubg malas garums",kubg.malas_garums)
bloks1 = Bloks(5, "oranžs", 3, 13)
print(bloks1.nosaukums, bloks1.tilpums())
bloks2 = Bloks(7, "zils", 5, 23)
print(bloks2.nosaukums, bloks2.derigums)
bloks2.forma = 12
print(bloks2.nosaukums, bloks2.derigums)


        




    