from orden import Orden,Cola

cola = Cola()

def menuP():
        opcion = 0
        print()
        while opcion != 5:
            try:
                opciones()
                opcion = int(input('Opción: '))
                if opcion == 1:
                    pass
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    print('\n¡Finalizado!')
                else:
                    print('\nSolo números entre 1 y 5\n')
            except:
                print('\nOpción inválida\n')

        
def opciones():
        print("""╔══════════════════════════════════════════════════════╗   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣶⣦⣄⣀
║                                                      ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
║                    Menú Principal                    ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀
║                                                      ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆
║           1. Nueva Orden                             ║   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀
║           2. Ver Avance de la Cola                   ║   ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀
║           3. Entregar Orden                          ║   ⠀⠀⠀⠀⠀⠀⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇
║           4. Información del Desarrollador           ║   ⠀⠀⠀⠀⠀⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇
║           5. Salir                                   ║   ⠀⠀⠀⠀⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋
║                                                      ║    ⠀⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁
║                                                      ║   ⠀⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁
║                                                      ║   ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉
║                                                      ║   ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋
╚══════════════════════════════════════════════════════╝   ⠈⠓⠾⠇""")

menuP()