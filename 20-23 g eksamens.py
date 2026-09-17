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
