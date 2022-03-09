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
            print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║               No hay órdenes pendientes              ║
║                                                      ║
╚══════════════════════════════════════════════════════╝""")
            return
        actual = self.primero
        print('\n╔══════════════════════════════════════════════════════╗')
        print('║                                                      ║')
        print('║                   Órdenes En Cola                    ║')
        print('║                                                      ║')
        print('╠══════════════════════════════════════════════════════╣')
        while actual:
            print('║                                                      ║')
            espacios = ''
            cliente = actual.orden.cliente
            for i in range(26 - len(cliente)):
                espacios += ' '
            espacios1 = ''
            tiempo = 'En: ' + str(actual.orden.pizzas.getTiempo()) + ' min'
            for i in range(16 - len(tiempo)):
                espacios1 += ' '
            print('║       ',actual.orden.cliente,espacios,tiempo,espacios1,"║")
            print('║                                                      ║')
            actual.orden.pizzas.recorrer()
            print('║                                                      ║')
            if actual.siguiente is not None:
                print('╠══════════════════════════════════════════════════════╣')
            actual = actual.siguiente
        print('╚══════════════════════════════════════════════════════╝')