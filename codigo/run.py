"""
Proyecto Bimestral
Segundo Bimestre

Problemática:
"""

def crearFacebook():
    """
        explicación de método
    """
    print("Creando cuenta de Facebook")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    idioma = input("Ingrese que idioma habla: ")
    correo = input("Ingrese su correo electronico: ")
    cadena = "Nombre: %s\nEdad: %d\nCiudad: %s\nPais: %s\nIdioma: %s\nCorreo: %s\n" %\
    (nombre,edad,ciudad,pais,idioma,correo)
    return cadena


def crearTwitter():
    """
        explicación de método
    """
    print("Creando cuenta de Twitter")
    nombres = input("Ingrese sus nombres: ")
    apellidos = input("Ingrese sus apellidos: ")
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    idioma = input("Ingrese que idioma habla: ")
    correo = input("Ingrese su correo electronico: ")
    print("Nombres: %s\nApellidos: %s\nEdad: %d\nCiudad: %s\nPais: %s\nIdioma: %s\nCorreo: %s\n" %\
    (nombres,apellidos,edad,ciudad,pais,idioma,correo))


def crearWhatsapp():
    """
        explicación de método
    """
    print("Creando cuenta de Whatsapp")
    nombres = input("Ingrese sus nombres: ")
    numero = int(input("Ingrese su numero de celular: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    cadena = "Nombres: %s\nNuemro: %s\nEdad: %d\nCiudad: %s\nPais: %s\n" %\
    (nombres,numero,edad,ciudad,pais)
    return cadena


def crearTelegram():
    """
        explicación de método
    """
    print("Creando cuenta de Telegram")
    nombres = input("Ingrese sus nombres: ")
    numero = int(input("Ingrese su numero de celular: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    area = input("Ingrese su area de interes: ")
    print ("Nombres: %s\nNuemro: %s\nEdad: %d\nCiudad: %s\nPais: %s\nArea:%s\n" %\
    (nombres,numero,edad,ciudad,pais,area))

def crearSignal():
    """
        explicación de método
    """
    print("Creando cuenta de Signal")
    nombres = input("Ingrese sus nombres: ")
    numero = int(input("Ingrese su numero de celular: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = input("Ingrese el nombre de su ciudad: ")
    pais = input("Ingrese el nombre de su pais: ")
    hobby = input("Ingrese su hobby principal: ")
    cadena ="Nombres: %s\nNuemro: %s\nEdad: %d\nCiudad: %s\nPais: %s\nHobby:%s\n" %\
    (nombres,numero,edad,ciudad,pais,hobby)
    return cadena

def crearInstagram():
    """
        explicación de método
    """
    print("Creando cuenta de Instagram")
    nombres = input("Ingrese sus nombres: ")
    ciudad = input("Ingrese el nombre de su ciudad: ")
    edad = int(input("Ingrese su edad: "))
    correo = input("Ingrese correo electronico: ")
    print ("Nombres: %s\nCiudad: %s\nEdad: %d\nCorreo:%s\n" %\
    (nombres,ciudad,edad,correo))

def crearFlickr():
    """
        explicación de método
    """
    print("Creando cuenta de Flickr")
    nombres = input("Ingrese sus nombres: ")
    correo = input("Ingrese correo electronico: ")
    cadena = "Nombres: %s\nCorreo:%s\n" %\
    (nombres,correo)
    return cadena
def obtenerMensaje(contador):
    """
    explicación de método
    """
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if(contador >= 1 and contador <= 5):
        cadena = (mensajeFinal[0])
    else:
        if(contador >= 6 and contador <= 15):
            cadena = (mensajeFinal[1])
        else:
            if(contador <= 16):
                cadena = (mensajeFinal[2])
    return cadena


if __name__ == "__main__":
    print("proceso inicial")
    bandera = True
    while(bandera):
        contador = 0
        print("Ingrese cualquiera de las opciones para crear una cuenta: \n")
        opcion = int(input("Ingrese 1 para crear una cuenta en Facebook: \n"\
        "Ingrese 2 para crear una cuenta en Twiter: \n"\
        "Ingrese 3 para crear una cuenta en Whatsapp: \n"\
        "Ingrese 4 para crear una cuenta en Telegram: \n"\
        "Ingrese 5 para crear una cuenta en Signal: \n"\
        "Ingrese 6 para crear una cuenta en Instagram: \n"\
        "Ingrese 7 para crear una cuenta en Flickr: \n"))
        if(opcion == 1):
            facebook = crearFacebook()
            print(facebook)
        else:
            if(opcion == 2):
                crearTwitter()
            else:
                if(opcion == 3):
                    Whatsapp = crearWhatsapp()
                    print(Whatsapp)
                else:
                    if(opcion == 4):
                        crearTelegram()
                    else:
                        if(opcion == 5):
                            Signal = crearSignal()
                            print(Signal)
                        else:
                            if(opcion == 6):
                                crearInstagram()
                            else:
                                if(opcion == 7):
                                    Flickr = crearFlickr()
                                    print(Flickr)
                                else:
                                    print("Error, intete colocar los numero presentados")
                                    contador = contador - 1

        opcion2 = input( "Ingrese si para seguir creando cuentas: \n"\
        "Ingrese no para dejar de crear cuentas: \n" )
        if(opcion2 == "si"):
            contador = contador + 1
        else:
            if(opcion2 == "no"):
                bandera = False
                cadena = obtenerMensaje(contador)
                print(cadena)
            else:
                print("Error, intete colocar los numero presentados")
