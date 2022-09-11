
'''
Crear un módulo para validación de nombres de usuarios, que cumplirá las 
siguientes características: 
• El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo 
de 12. 
• El nombre de usuario debe ser alfanumérico. 
• Si el nombre de usuario es de menos de 6 caracteres "El nombre de usuario 
debe contener al menos 6 caracteres". 
• Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre 
de usuario no puede contener más de 12 caracteres". 
• Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el 
mensaje "El nombre de usuario puede contener solo letras y números". 
• Nombre de usuario válido, retorna “Usuario válido”. 
'''

def validacion_usuario(usuario):
    if len(usuario) < 6:
        return "El nombre de usuario debe contener al menos 6 caracteres"
    elif len(usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    elif not usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return "Usuario válido"
    