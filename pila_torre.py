"""
Implemente un programa, utilizando la clase Pila que permita la resolución del juego de las Torres de Hanoi para tres discos 
"""
class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre
    
    def apilador(self, item):
        self.items.append(item)
    
    def desapilador(self):
        return self.items.pop() if self.items else None
    
    def __str__(self):
        return self.nombre

def mover_disco(pila_origen, pila_moviento):
    disco = pila_origen.desapilador()
    if disco is not None:
        pila_moviento.apilador(disco)
        print(f"Mover {disco} de {pila_origen} a {pila_moviento}")

def torre(n,origen,movimiento, auxiliar):
    if n == 1:
        mover_disco(origen, movimiento)
    else:
        torre(n-1, origen, auxiliar, movimiento)
        mover_disco(origen, movimiento)
        torre(n-1, auxiliar, movimiento, origen)

origen = Pila("Origen")
movimiento = Pila("Movimiento")
auxiliar = Pila("Auxiliar")

for disco in range(3,0,-1):
    origen.apilador(disco)

torre(3,origen,movimiento, auxiliar)
print("¡Haz salvado el mundo!")