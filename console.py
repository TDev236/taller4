from boa_constrictor import BoaConstrictor
from huron import Huron

boa1 = BoaConstrictor("Julia", 13.2, 4, "Colombia", 0.4)
huron1 = Huron("Huron1", 4.5, 3, "Usa", 5)

print(boa1.hacer_sonido())
print(huron1.hacer_sonido())
print(boa1.calcular_flete())
print(boa1.comer_raton())
print(boa1.ratones_comidos())
print(boa1.comer_raton())
print(boa1.ratones_comidos())

for ratones in range(1,10):
    boa1.comer_raton()
    
print(boa1.ratones_comidos())
