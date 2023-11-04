class compra:
    def __init__(self,usuario):
        self.usuario=usuario
        self.changuito=[]

    def Agregar_changuito(self,item):
        self.changuito.append(item)
        print("Producto agregado a la lista")
        input ("Presione enter para continuar...")

    def Remover_changuito(self,item):
        self.changuito.remove(item)
        print("El producto fue eliminado exitosamente")
        input ("Presione enter para continuar...")

    def Ver_changuito(self):
        if self.changuito:
            print("Lista de objetos en la compra:")
            for item in self.changuito:
                print(f"-{item}")
        else:
            print("Changuito vacio.")

    def Finalizar_compra(self):
        print(f"Compra de {self.usuario}")
        if self.changuito:
            print("Lista de objetos en la compra:")
            for item in self.changuito:
                print(f"-{item}")
        else:
            print("Changuito vacio.")

    def __str__(self):
        return print(f"Compra de {self.usuario}")