import  os
from clientes.compras import compra
from clientes.Generar_registro_compra import registro


productos=["producto1","prodcto2","producto3","producto4"]
a=True
while(a==True):
    os.system('cls')
    nombre=str(input("Ingrese su nombre de cliente:"))
    email=str(input("Ingrese su email:"))

    cliente=compra(nombre,email)

    while(a==True):
        os.system('cls')
        print("""1-Agregar producto al changuito
2-Elimar un producto del changito
3-Ver changuito
4-Finalizar su compra""")
        try:
            seleccion=int(input("Seleccione una opción:"))

            if seleccion==1:
                os.system('cls')
                print("Lista de productos:")
                for i in range(len(productos)):
                    num=i+1
                    cadena="{}-{}".format(num,productos[i])
                    print(cadena)

                p=int(input("Ingrese el numero del producto de la lista:"))
                cliente.Agregar_changuito(productos[p-1])
                input("Presione enter para continuar...")

            elif seleccion==2:
                os.system('cls')
                items=cliente.Ver_changuito()
                p=int(input("ingrese el numero del producto que desea elimnar:"))
                cliente.Remover_changuito(p-1)
                input("Presione enter para continuar...")

            elif seleccion==3:
                os.system('cls')
                cliente.Ver_changuito()
                input("Presione enter para continar...")

            elif seleccion==4:
                os.system('cls')
                cliente.Ver_changuito()
                verificar=int(input("Esta seguro que desea finalizar su compra? 1-si 2-no:"))
                if(verificar == 1):
                    print("Gracias por su compra")
                    datos=registro("Compras.txt",nombre,email,cliente.Finalizar_compra())
                    datos.crea_o_agrega()
                    input("Presione enter para continuar...")
                    os.system('cls')
                    nueva=int(input("¿Desea hacer una nueva compra ?1-si 2-no"))
                    if(nueva!=1 and nueva==2):
                        a=False
                    elif(nueva!=1 and nueva!=2):
                        print("La opción ingresada no es valida")
                        input("Presione enter para continuar...")
                    break
            else:
                os.system('cls')
                print("La opción ingresada no es valida")
                input("Presione enter para continuar...")
        except:
            os.system('cls')
            print("Opción ingresada no es valida")
            input("Presione enter para continuar...")
print("Fin del programa")