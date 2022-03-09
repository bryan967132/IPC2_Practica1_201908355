from orden import Orden,Cola
from pizza import Pizza,listaPizzas
from ingrediente import Ingrediente,listaIngredientes

cola = Cola()

ingredientes = listaIngredientes()
pizzas = listaPizzas()

ingrediente = Ingrediente('Pepperoni',3)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)
pizzas.insertar(pizza)

ingredientes = listaIngredientes()
ingrediente = Ingrediente('Salchicha',4)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Queso',5)
ingredientes.insertar(ingrediente)
ingrediente = Ingrediente('Carne',10)
ingredientes.insertar(ingrediente)
pizza = Pizza(ingredientes)

pizzas.insertar(pizza)

nuevaOrden = Orden('Danny',2,pizzas)
cola.encolar(nuevaOrden)

print(input().isdigit())

#nuevaOrden = Orden('Bryan',1,'pizzas')
#cola.encolar(nuevaOrden)
#
#nuevaOrden = Orden('Keneth',3,'pizzas')
#cola.encolar(nuevaOrden)

cola.recorrer()