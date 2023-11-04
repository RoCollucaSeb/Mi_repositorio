class compra:
    def __init__(self,usuario,email):
        self.usuario=usuario
        self.email=email
        self.changuito=[]

    def Agregar_changuito(self,producto):
        self.changuito.append(producto)
        print("El producto {} fue agregado al changuito de compra correctamente".format(producto))

    def Remover_changuito(self,num):
        item=self.changuito[num]
        self.changuito.remove(item)
        print(f"El producto {item} fue eliminado del changuito de compras ")

    def Ver_changuito(self):
        if self.changuito:
            print("Lista de productos:")
            for i in range(len(self.changuito)):
                print(f"{i+1}-{self.changuito[i]}")
            return  int(len(self.changuito))
        else:
            print("Changuito vacio.")

    def Finalizar_compra(self):
        return self.changuito

    def __str__(self):
        return print(f"Compra de {self.usuario}")