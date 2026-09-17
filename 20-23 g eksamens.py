#python
from datetime import datetime
class masinas:
    def __init__ ( self, zimols, modelis, regd, masa, benzins ):
        self.laiks = datetime.now().strftime("%Y-%M-%d")
        self.zimols = zimols
        self.modelis = modelis
        self.regd = regd
        self.masa = masa
        self.benzins = benzins

auto_tests = masinas
zimols = "audi"
modelis = "A4"
regd = "22.10.2019"
masa = 1800
degviela = "BG"

print(zimols, modelis, regd, masa, degviela)

#oop2

class kubs:
    def __init__ (self, malas_garums, krāsas_nosaukums):
        self.malas_garums = malas_garums
        self.krāsas_nosaukums = krāsas_nosaukums
        

    def aprekinat_tilpumu(self, tilpums, malas_garums):
        self.tilpums = tilpums
        self.malas_garums = malas_garums
        tilpums = malas_garums*malas_garums*malas_garums

kubg = kubs.aprekinat_tilpumu
malas_garums = 10
krāsas_nosaukums = "zaļa"
print(malas_garums)




kubr = kubs.aprekinat_tilpumu
malas_garums = 1
krāsas_nosaukums = "sarkana"
print(malas_garums)

del kubr
print("Kubsr ir likvidēts")






