import os
import webbrowser
class Orden:
    def __init__(self,numero,cliente,cantidad,pizzas,hora,minuto,espera = None):
        self.numero = numero
        self.cliente = cliente
        self.cantidad = cantidad
        self.pizzas = pizzas
        self.hora = hora
        self.minuto = minuto
        self.espera = espera

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
            self.primero.orden.espera = 0
            self.numero += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        self.ultimo = Nodo(orden = orden,anterior = self.ultimo)
        if self.getMinDif(actual.orden.hora,actual.orden.minuto,self.ultimo.orden.hora,self.ultimo.orden.minuto) > actual.orden.pizzas.getTiempo() + actual.orden.espera:
            self.ultimo.orden.espera = 0
        else:
            self.ultimo.orden.espera = actual.orden.pizzas.getTiempo() + actual.orden.espera - self.getMinDif(actual.orden.hora,actual.orden.minuto,self.ultimo.orden.hora,self.ultimo.orden.minuto)
        actual.siguiente = self.ultimo
        self.numero += 1

    def getMinDif(self,horaI,minutoI,horaF,minutoF):
        return (int(horaF) - int(horaI)) * 60 + int(minutoF) - int(minutoI)
    
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
        espacios = ''
        hora = '{:<9}Hora: {}:{}'.format('',actual.orden.hora,actual.orden.minuto)
        for i in range(48 - len(hora)):
            espacios += ' '
        print('║   ',hora,espacios,'║')
        print('║                                                      ║')
        actual.orden.pizzas.recorrer()
        print('║                                                      ║')
        print('╠══════════════════════════════════════════════════════╣')
        print('║                                                      ║')
        espacios = ''
        
        tiempo = 'Preparación: {:<10} En Cola: {} '.format(str(actual.orden.pizzas.getTiempo()) + ' min',str(actual.orden.espera) + ' min')
        for i in range(48 - len(tiempo)):
            espacios += ' '
        print('║   ',tiempo,espacios,'║')
        print('║                                                      ║')
        print('╚══════════════════════════════════════════════════════╝')

        primero = actual
        self.primero = actual.siguiente

        if self.ultimo.orden.numero == primero.orden.numero:
            self.ultimo = None
            return
        actual = self.ultimo
        while actual.anterior and actual.anterior.orden.numero != primero.orden.numero:
            actual = actual.anterior
        actual.anterior = None
    
    def dibujar(self):
        colatxt = """digraph {
    node [shape = none fontcolor="#0060B2"]
    rankdir=DOWN;
    cola[
        label=<
            <table border="0" cellborder="1" cellspacing="5" cellpadding="4">
                <tr>"""
        if self.ultimo is not None:
            actual = self.ultimo
            while actual:
                colatxt += """
                    <td style="rounded" color="#0060B2" bgcolor = "white" height = "100" width = "60">No. """ + str(actual.orden.numero) + """<br/>""" + actual.orden.cliente + """<br/>""" + str(actual.orden.cantidad) + """ Pizzas</td>"""
                actual = actual.anterior
        else:
            colatxt += """
                    <td style="rounded" color="#0060B2" bgcolor = "white" height = "100" width = "60">No hay<br/>ordenes<br/>pendientes</td>"""
        colatxt += """
                </tr>
            </table>
        >
    ];
}"""
        with open('Archivos/Cola.txt','w') as cola:
            cola.write(colatxt)
        os.system('circo -Tpdf Archivos/Cola.txt -o Cola.pdf')
        webbrowser.open('Cola.pdf')
        

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
            espacios = ''
            hora = '{:<9}Hora: {}:{}'.format('',actual.orden.hora,actual.orden.minuto)
            for i in range(48 - len(hora)):
                espacios += ' '
            print('║   ',hora,espacios,'║')
            print('║                                                      ║')
            actual.orden.pizzas.recorrer()
            print('║                                                      ║')
            if actual.siguiente is not None:
                print('╠══════════════════════════════════════════════════════╣')
            actual = actual.siguiente
        print('╚══════════════════════════════════════════════════════╝')