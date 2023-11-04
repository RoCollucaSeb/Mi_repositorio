#Gnerar_registro_compra
import os
from datetime import datetime

class registro:
    def __init__(self,nombre_archivo,usuario,email,lista):
        self.nombre_archivo=nombre_archivo#El nombre del archivo debe venir con su terminación ejemplo:"texto.txt"
        self.usuario=usuario
        self.email=email
        self.lista=lista

    def crea_o_agrega(self):

        dt=datetime.now()
        fecha_y_hora=dt.strftime("%A %d %B %Y %I:%M")

        existencia=os.path.isfile(self.nombre_archivo)
        if existencia==True:
            f=open("{}".format(self.nombre_archivo),"a")
            f.write( "\n{} {} con email {} ha realizado una compra de lo sigueinte:{}".format(fecha_y_hora,self.usuario,self.email,self.lista))
            f.close()
        else:
            f=open("{}".format(self.nombre_archivo),"a")
            f.write( "{} {} con email {} ha realizado una cpra de lo sigueinte:{}".format(fecha_y_hora,self.usuario,self.email,self.lista))
            f.close()