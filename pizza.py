class Pizza:
    def __init__(self,ingredientes):
        self.ingredientes = ingredientes

class Nodo:
    def __init__(self,pizza = None,siguiente = None):
        self.pizza = pizza
        self.siguiente = siguiente

class listaPizzas:
    def __init__(self):
        self.primero = None

    def insertar(self,pizza):
        if self.primero is None:
            self.primero = Nodo(pizza = pizza)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(pizza = pizza)
    
    def recorrer(self):
        actual = self.primero
        while actual:
            actual.pizza.ingredientes.recorrer()
            actual = actual.siguiente
    
    def getTiempo(self):
        actual = self.primero
        tiempo = 0
        while actual:
            tiempo += actual.pizza.ingredientes.getTiempo()
            actual = actual.siguiente
        return tiempo