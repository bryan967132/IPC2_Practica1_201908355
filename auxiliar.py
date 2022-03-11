from datetime import datetime
from orden import Orden,Cola
from pizza import Pizza,listaPizzas
from ingrediente import Ingrediente,listaIngredientes
from graphviz import Digraph

cola = Cola()

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Piña',2)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

nuevaOrden = Orden(cola.getNumero(),'Brandon',1,pizzas,'20','06')
cola.nuevaOrden(nuevaOrden)

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Salchicha',4)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

nuevaOrden = Orden(cola.getNumero(),'Keneth',2,pizzas,'20','07')
cola.nuevaOrden(nuevaOrden)

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Salchicha',4)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

nuevaOrden = Orden(cola.getNumero(),'Danny',1,pizzas,'20','08')
cola.nuevaOrden(nuevaOrden)

#cola.dibujar()

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Salchicha',4)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

nuevaOrden = Orden(cola.getNumero(),'Luna',4,pizzas,'20','11')
cola.nuevaOrden(nuevaOrden)

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

nuevaOrden = Orden(cola.getNumero(),'Brandon',1,pizzas,'20','25')
cola.nuevaOrden(nuevaOrden)

cola.recorrer()

cola.entregarOrden()

cola.entregarOrden()

cola.entregarOrden()

cola.entregarOrden()

cola.entregarOrden()

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Piña',2)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

nuevaOrden = Orden(cola.getNumero(),'Lunita',2,pizzas,'20','31')
cola.nuevaOrden(nuevaOrden)

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Piña',2)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

nuevaOrden = Orden(cola.getNumero(),'Hugo',2,pizzas,'20','32')
cola.nuevaOrden(nuevaOrden)

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

nuevaOrden = Orden(cola.getNumero(),'Estela',1,pizzas,'20','45')
cola.nuevaOrden(nuevaOrden)

cola.entregarOrden()

cola.entregarOrden()

cola.entregarOrden()