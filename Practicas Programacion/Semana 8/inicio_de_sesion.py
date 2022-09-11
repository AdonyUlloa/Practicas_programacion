import modulo_usuario
import modulo_clave

print("=======================")
print("INICIO DE SESIÓN")
print("=======================")

while True:
    user = input("Introduce un nombre de usuario: ")
    validacion = modulo_usuario.validacion_usuario(user)
    print(validacion)
    if validacion == "Usuario válido":
        break

while True:
    clave=input("Introduce contraseña: ")
    validacion2 = modulo_clave.validacion_clave(clave)
    print(validacion2)
    if validacion2 == "Contraseña valida":
        break

print("=======================")
print("BIENVENIDO ", user)
print("=======================")
print("Inicio de sesión registrado")