class Orden:
    def __init__(self,numero,cliente,cantidad,pizzas,hora,minuto):
        self.numero = numero
        self.cliente = cliente
        self.cantidad = cantidad
        self.pizzas = pizzas
        self.hora = hora
        self.minuto = minuto

class Nodo:
    def __init__(self,orden = None,siguiente = None,anterior = None):
        self.orden = orden
        self.siguiente = siguiente
        self.anterior = anterior

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.numero = 1
    
    def getNumero(self):
        return self.numero
    
    def nuevaOrden(self,orden):
        if self.primero is None:
            self.primero = Nodo(orden = orden)
            self.ultimo = self.primero
            self.numero += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        self.ultimo = Nodo(orden = orden,anterior = self.ultimo)
        actual.siguiente = self.ultimo
        self.numero += 1
    
    def entregarOrden(self):
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
        print('║                    Orden Entregada                   ║')
        print('║                                                      ║')
        print('╠══════════════════════════════════════════════════════╣')
        print('║                                                      ║')
        espacios = ''
        detalles = 'No. {:<4} Cliente: {:<13}'.format(actual.orden.numero,actual.orden.cliente)
        for i in range(48 - len(detalles)):
            espacios += ' '
        print('║   ',detalles,espacios,'║')
        print('║                                                      ║')
        actual.orden.pizzas.recorrer()
        print('╠══════════════════════════════════════════════════════╣')
        print('║                                                      ║')
        espacios = ''
        tiempo = 'Preparación: ' + str(actual.orden.pizzas.getTiempo()) + ' min'
        for i in range(48 - len(tiempo)):
            espacios += ' '
        print('║   ',tiempo,espacios,'║')
        print('║                                                      ║')
        print('╚══════════════════════════════════════════════════════╝')

        self.primero = actual.siguiente

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
            detalles = 'No. {:<4} Cliente: {:<13} En: {} min'.format(actual.orden.numero,actual.orden.cliente,actual.orden.pizzas.getTiempo())
            for i in range(48 - len(detalles)):
                espacios += ' '
            print('║   ',detalles,espacios,"║")
            print('║                                                      ║')
            actual.orden.pizzas.recorrer()
            print('║                                                      ║')
            if actual.siguiente is not None:
                print('╠══════════════════════════════════════════════════════╣')
            actual = actual.siguiente
        print('╚══════════════════════════════════════════════════════╝')