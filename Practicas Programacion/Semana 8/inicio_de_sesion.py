
import modulo_usuario
import modulo_clave

print("INICIO DE SESIÓN")

usuario=input("Introduce usuario: ")
clave=input("Introduce contraseña: ")

print(modulo_usuario.validar_nombre_usuario(usuario))
print(modulo_clave.validacion_clave(clave))