class login:
    def __init__(self,datos):
        self.datos=datos

    def ingreso(self,datos):#Función para ingresar con nombre de usuario
        usuario=str(input("\nIngrese el nombre de usuario:"))
        A=self.datos.get(usuario,True)#Comprueba que el nombre de usuario exista en los datos almacenados
        while(A==True):
            usuario=str(input("Usuario no encontrado, vuelva a ingresarlo O ingrese 0 para volver al menu principal:"))
            if usuario=='0':return False
            A=self.datos.get(usuario,True)
        while(True):
                contraseña=str(input("Ingrese su contraseña, o 0 para volver al menú principal:"))
                if contraseña=='0': return
                if (contraseña == self.datos[usuario]):#Verifica que la contraseña coincida con la del usuario
                    print("BIENVENIDO {}!!!".format(usuario))
                    input("\nPresione enter para continuar...")
                    return True
                print("Contraseña inccorecta")#en caso contrario marca dice que la contraseña no es la correcta

    def nuevo_usuario(self):
        A=False#esta asignacion la hago para que dal dato A por esas casulidades tenga el dato True almacenado, solo es una precaución
        usuario=str(input("Ingrese el nombre de usuario:"))
        A=self.datos.get(usuario,True)#Verifica que el nombre de usuario esté disponible
        while(A!=True):#en caso de no estárlo lo vuelve a solicitar repetidamente hasta que encuentre uno disponible
            usuario=str(input("""El usuario ya existe, igrese otro nombre de usuario O ingrese 0 para volver al menu principal:"""))
            if usuario=='0':return
            A=self.datos.get(usuario,True)
        if(A==True):#Ingresa acá si el usuario está disponible
            contraseña1=str(input("Ingrese su contraseña, o ingrese 0 para volver al menú principal:"))
            while(True):
                if contraseña1=='0': return
                if(len(contraseña1)<8):
                    print("La contraseña debe tener al menos 8 carátes")
                if(len(contraseña1)>=8):
                    contraseña2=str(input("Repita la contraseña:"))
                    if(contraseña1==contraseña2):
                        self.datos[usuario]=contraseña1
                        print("Usuario creado correctamente.")
                        input("\nPresione enter para continuar...")
                        return
                    else:print("La contraseña no coinciden")
                contraseña1=str(input("Ingrese nuevamente una contraseña con 8 caracteres, o ingrese 0 para salir:"))

    def listar(self):
        a=list(self.datos.keys())#debo transformar los datos en lista, si no tirraría un error en el FOR que está debajo
        print("Nombres de usuarios existentes:")
        for i in range(len(a)):
            print(a[i])
        input("\nPresione enter para continuar...")
        return