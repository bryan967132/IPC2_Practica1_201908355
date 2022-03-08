class Ingrediente:
    def __init__(self,nombre,tiempo):
        self.nombre = nombre
        self.tiempo = tiempo

class Nodo:
    def __init__(self,ingrediente = None,siguiente = None):
        self.ingrediente = ingrediente
        self.siguiente = siguiente

class listaIngredientes:
    def __init__(self):
        self.primero = None

    def insertar(self,ingrediente):
        if self.primero is None:
            self.primero = Nodo(ingrediente = ingrediente)
            return
        actual = self.primero
        while actual:
            actual = actual.siguiente
        actual = Nodo(ingrediente = ingrediente)