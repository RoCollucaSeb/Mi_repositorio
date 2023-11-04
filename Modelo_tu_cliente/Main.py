#main
from Clientes.compra import compra
from Clientes.login import login

datos = {'usuario1':'contraseña','usuario2':'contraseña','usuario3':'contraseña'}
login1 =login(datos)
while(True):
    print("""Menu Principal
1)Ingresar.
2)Crear un nuevo usuario.
3)Mostrar los nombres de usuario.
4)Cerrar programa.""")
    try:
        opcion = int(input("Seleccione una opción:"))
        if opcion==1:
            a=login1.ingreso()
            compra1=compra(usuario)
            while(a==True):
                print("""1-Agregar producto a la lista
2-Quitar producto
3-Ver changuito
4-Finalizar compra.
""")
                try:
                    opcion1=int(input("Selecicone una opcion:"))
                    if opcion1==1:
                        print("""1- P1
2- P2
3- P3
4- P4
5- P5
6- P6
""")
                        try:
                            opcion2=int(input("Selccione un producto:"))
                            if(opcion2>=1 and opcion2<=6):
                                compra1.Agregar_changuito(f"P{opcion2}")
                        except:
                            print("La opcion seleccionada no es correcta")
                    elif opcion1==2:
                        compra1.Ver_changuito()
                        try:
                            opcion3=int(input("Ingrese el nombre del producto que quiere eliminar:"))
                            compra1.Remover_changuito(f"p{opcion3}")
                        except:
                            print("El producto seleccionado no existe.")
                    elif opcion1==3:
                        compra1.Ver_changuito()
                    elif opcion1==4:
                        compra1.Finalizar_compra()

                except:
                    print("La opción seleccionada no es correcta")
        elif opcion==2:
            login1.nuevo_usuario()
        elif opcion==3:login1.listar()
        elif opcion==4:
            print("Fin del programa")
            break
    except:#Esta excepción está en caso de que se ingrese una opción que no sea un número,es para prevenir un error tipo Value
        print("La opcion seleccionada es incorrecta.")
        input("Presione enter para continuar")