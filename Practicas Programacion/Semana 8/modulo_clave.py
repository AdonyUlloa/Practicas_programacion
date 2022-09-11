 
"""
2. Crear un módulo para validación de contraseñas, que cumplirá las siguientes 
características: 
• La contraseña debe contener un mínimo de 8 caracteres.. 
• La contraseña no puede contener espacios en blanco. 
• Contraseña válida, retorna “Contraseña valida” 
• Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura". 
"""
def validacion_clave(clave):
	if len(clave)>=8 and clave.isspace()==False:
		return "Contraseña valida"
	else:
		return "La contraseña elegida no es segura, La contraseña debe contener un mínimo de 8 caracteres sin espacios en blanco"

