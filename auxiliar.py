from datetime import datetime
from orden import Orden,Cola
from pizza import Pizza,listaPizzas
from ingrediente import Ingrediente,listaIngredientes

cola = Cola()

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Salchicha',4)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Carne',10)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

hora = datetime.now().strftime('%H')
minuto = datetime.now().strftime('%M')
nuevaOrden = Orden(cola.getNumero(),'Brandon',2,pizzas,hora,minuto)
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
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Piña',2)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

hora = datetime.now().strftime('%H')
minuto = datetime.now().strftime('%M')
nuevaOrden = Orden(cola.getNumero(),'Keneth',2,pizzas,hora,minuto)
cola.nuevaOrden(nuevaOrden)

pizzas = listaPizzas()

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Salchicha',4)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Piña',2)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Salchicha',4)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Carne',10)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Piña',2)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Salchicha',4)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

hora = datetime.now().strftime('%H')
minuto = datetime.now().strftime('%M')
nuevaOrden = Orden(cola.getNumero(),'Danny',4,pizzas,hora,minuto)
cola.nuevaOrden(nuevaOrden)

cola.dibujar()

cola.recorrer()

cola.entregarOrden()

cola.recorrer()

cola.entregarOrden()

cola.recorrer()

cola.entregarOrden()

cola.recorrer()

cola.entregarOrden()

cola.recorrer()