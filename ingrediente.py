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
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(ingrediente = ingrediente)

    def recorrer(self):
        actual = self.primero
        contador = 1
        pizza = '║    ➤   '
        while actual:
            pizza += "{}. {:<11}".format(contador,actual.ingrediente.nombre)
            if contador == 3 and actual.siguiente:
                espacios = ''
                for i in range(55 - len(pizza)):
                    espacios += ' '
                pizza += espacios + '║\n║        '
            if contador <= 3 and actual.siguiente is None:
                espacios = ''
                for i in range(55 - len(pizza)):
                    espacios += ' '
                pizza += espacios + '║'
            if contador > 3 and actual.siguiente is None:
                espacios = ''
                for i in range(112 - len(pizza)):
                    espacios += ' '
                pizza += espacios + '║'
            contador += 1
            actual = actual.siguiente
        print(pizza)
    
    def getTiempo(self):
        actual = self.primero
        tiempo = 0
        while actual:
            tiempo += actual.ingrediente.tiempo
            actual = actual.siguiente
        return tiempo