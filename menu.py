from orden import Orden,Cola
from pizza import Pizza,listaPizzas
from ingrediente import Ingrediente,listaIngredientes
from limpiarConsola import Limpiar

class Menu:
    def menuP(self):
        limpiar = Limpiar()
        limpiar.limpiarConsola()
        opcion = 0
        ordenes = Cola()
        while opcion != 6:
            try:
                self.opciones()
                opcion = int(input('Opción: '))
                if opcion == 1:
                    ordenes.encolar(self.nuevaOrden())
                    limpiar.limpiarConsola()
                    print('\nNueva Orden en Cola')
                elif opcion == 2:
                    limpiar.limpiarConsola()
                elif opcion == 3:
                    limpiar.limpiarConsola()
                elif opcion == 4:
                    limpiar.limpiarConsola()
                    ordenes.recorrer()
                elif opcion == 5:
                    limpiar.limpiarConsola()
                    self.miInfo()
                elif opcion == 6:
                    print('\n¡Finalizado!')
                else:
                    limpiar.limpiarConsola()
                    print('\nSolo números entre 1 y 6')
            except:
                limpiar.limpiarConsola()
                print('\nOpción inválida')

    def nuevaOrden(self):
        print('\nNueva Orden')
        cliente = input('Ingrese el nombre del cliente: ')
        cantidad = input('Ingrese la cantidad de pizzas: ')
        while not cantidad.isdigit():
            cantidad = input('Ingrese la cantidad de pizzas: ')
        cantidad = int(cantidad)
        pizzas = listaPizzas()
        for i in range(cantidad):
            ingredientes = listaIngredientes()
            print('\nPizza',i + 1)
            print('Marque con una X si desea el ingrediente')
            if input('1. Pepperoni (3 min): ').upper() == 'X':
                ingrediente = Ingrediente('Pepperoni',3)
                ingredientes.insertar(ingrediente)
            if input('2. Salchicha (4 min): ').upper() == 'X':
                ingrediente = Ingrediente('Salchicha',4)
                ingredientes.insertar(ingrediente)
            if input('3. Carne (10 min): ').upper() == 'X':
                ingrediente = Ingrediente('Carne',10)
                ingredientes.insertar(ingrediente)
            if input('4. Queso (5 min): ').upper() == 'X':
                ingrediente = Ingrediente('Queso',5)
                ingredientes.insertar(ingrediente)
            if input('5. Piña (2 min): ').upper() == 'X':
                ingrediente = Ingrediente('Piña',2)
                ingredientes.insertar(ingrediente)
            pizza = Pizza(ingredientes)
            pizzas.insertar(pizza)
        return Orden(cliente,cantidad,pizzas)
        
    def opciones(self):
        print("""
╔══════════════════════════════════════════════════════╗   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀
║                                                      ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
║                    Menú Principal                    ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀
║                                                      ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆
╠══════════════════════════════════════════════════════╣   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀
║                                                      ║   ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
║           1. Nueva Orden                             ║   ⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
║           2. Ver Avance de la Cola                   ║   ⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
║           3. Entregar Orden                          ║   ⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋
║           4. Ver Órdenes Pendientes                  ║    ⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁
║           5. Información del Desarrollador           ║   ⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁
║           6. Salir                                   ║   ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉
║                                                      ║   ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋
╚══════════════════════════════════════════════════════╝   ⠈⠓⠾⠇
""")
    def miInfo(self):
        print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║                    Desarrollador                     ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║              Carnet: 201908355                       ║
║              Nombre: Danny Hugo Bryan                ║
║              Apellido: Tejaxún Pichiyá               ║
║                                                      ║
╚══════════════════════════════════════════════════════╝""")