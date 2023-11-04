class persona:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    def __str__(self):
        return f"Nombre:{self.nombre}"