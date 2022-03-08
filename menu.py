from limpiarConsola import Limpiar
class Menu:
    def menuP(self):
        limpiar = Limpiar()
        limpiar.limpiarConsola()
        opcion = 0
        print()
        while opcion != 5:
            try:
                self.opciones()
                opcion = int(input('Opción: '))
                if opcion == 1:
                    limpiar.limpiarConsola()
                elif opcion == 2:
                    limpiar.limpiarConsola()
                elif opcion == 3:
                    limpiar.limpiarConsola()
                elif opcion == 4:
                    limpiar.limpiarConsola()
                    print("""╔══════════════════════════════════════════════════════╗
║                   Desarrollador                      ║
╠══════════════════════════════════════════════════════╣
║           Carnet: 201908355                          ║
║           Nombre: Danny Hugo Bryan                   ║
║           Apellido: Tejaxún Pichiyá                  ║
╚══════════════════════════════════════════════════════╝""")
                elif opcion == 5:
                    print('\n¡Finalizado!')
                else:
                    limpiar.limpiarConsola()
                    print('\nSolo números entre 1 y 5\n')
            except:
                limpiar.limpiarConsola()
                print('\nOpción inválida\n')

        
    def opciones(self):
        print("""╔══════════════════════════════════════════════════════╗   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀
║                                                      ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
║                                                      ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀
║                    Menú Principal                    ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆
║                                                      ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀
║           1. Nueva Orden                             ║   ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
║           2. Ver Avance de la Cola                   ║   ⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
║           3. Entregar Orden                          ║   ⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
║           4. Información del Desarrollador           ║   ⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋
║           5. Salir                                   ║    ⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁
║                                                      ║   ⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁
║                                                      ║   ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉
║                                                      ║   ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋
╚══════════════════════════════════════════════════════╝   ⠈⠓⠾⠇
""")
        