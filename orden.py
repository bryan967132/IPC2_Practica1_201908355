class Orden:
    def __init__(self,cliente,cantidad,pizzas):
        self.cliente = cliente
        self.cantidad = cantidad
        self.pizzas = pizzas

class Nodo:
    def __init__(self,orden = None,siguiente = None):
        self.orden = orden
        self.siguiente = siguiente

class Cola:
    def __init__(self):
        self.primero = None
    
    def encolar(self,orden):
        if self.primero is None:
            self.primero = Nodo(orden = orden)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(orden)

    def recorrer(self):
        if self.primero is None:
            print('No hay órdenes pendientes')
            return
        actual = self.primero
        while actual:
            print(actual.orden.cliente,actual.orden.cantidad)
            actual.orden.pizzas.recorrer()
            actual = actual.siguiente