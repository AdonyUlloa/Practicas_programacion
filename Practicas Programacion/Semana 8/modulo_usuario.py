
def validar_nombre_usuario(nombre):
    if len(nombre)>=6 and len(nombre)<=12:
        for i in nombre:
            if i in 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890':
                return 'Usuario valido'
            else:
                return 'El nombre de usuario puede contener solo letras y numeros'
    elif len(nombre)<6:
        return 'El nombre de usuario debe contener al menos 6 caracteres'
    else:
        return 'El nombre de usuario no puede contener mas de 12 caracteres'

nombre = input("Ingrese el nombre de usuario: ")

print(validar_nombre_usuario(nombre))