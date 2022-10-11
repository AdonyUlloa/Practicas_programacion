#Estudiantes 
''' 
EDWIN ADONY ULLOA DIAZ
SMIS001721 
JULISSA YAMILETH HERNÁNDEZ CLAROS
MIS082721
'''

#Cargamos unas librerias que ocuparemos, hay algunas que no se usaron
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from select import select
import smtplib
from source import email
from dotenv import load_dotenv
from tkinter import END, Button, Entry, Label, StringVar, Text, Tk, messagebox, ttk

load_dotenv()

#Cargamos el programa
ventana = Tk()
ventana.title("CORREOS PYTHON")
ventana.geometry("650x500")
ventana.resizable(False,False)
ventana.configure(background="#276e90")


#Cargamos los datos para enviar el mensaje
def enviar():
    emisor = correo.get()
    password = passw.get()
    destinatario = email.get()
    asunto = subject.get()
    mensaje = message.get(1.0, END)
    print(destinatario)
    print(mensaje)
    ventana.destroy()
    try:
        msg = MIMEMultipart()
        msg['From'] = emisor
        msg['To'] = destinatario
        msg['Subject'] = asunto

        #Aqui esta el cuerpo de nuestro sencillo HTML, donde enviamos dos variables
        cuerpo = """
       
           <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>CORREOS PYTHONt</title>
                </head>
                <body>
                    <h1>Mi primer mensaje</h1>
                    <p>Mensaje enviado desde Python por {0} <p>
                    <h1>{1}</h1>
                </body>
            </html>
        """
        #Aqui recopilamos los datos y enviamos
        msg.attach(MIMEText(cuerpo.format(emisor, mensaje), 'html'))
        texto = msg.as_string()

        #Usamos SMTP
        serverSMTP = smtplib.SMTP('smtp.gmail.com', 587)
        serverSMTP.ehlo()
        serverSMTP.starttls()
        serverSMTP.ehlo()
        serverSMTP.login(emisor, password)
        serverSMTP.sendmail(emisor, destinatario, texto)
        messagebox.showinfo("Enviar correo", "Correo enviado exitosamente")
        serverSMTP.close()
        
        
    except Exception as e:
        messagebox.showerror("Error", str(e))


#Creamos todos los label y Entry para recopilar los datos a usurios
lbl = Label(ventana, text="| BIENVENIDO |")
lbl.place(x=400, y=20)
lbl.configure(foreground="black", background="#efefef", font=("Arial Bold", 11))

lbl = Label(ventana, text="| AQUI PUEDES ENVIAR CORREOS CON \n TU CORREO Y CONTRASEÑA SMTP \n PERSONAL |")
lbl.place(x=360, y=50)
lbl.configure(foreground="black", background="#efefef", font=("Arial Bold", 8))

lbl = Label(ventana, text="Correo: ")
lbl.place(x=20, y=30)
lbl.configure(foreground="white", background="#0a3143", font=("Arial Bold", 10))

#El programa puede enviar correo con cualquier correo.
correo = Entry(ventana)
correo.place(x=125, y=30)
correo.configure(background="#cecfc9", font=("Arial", 12))

lbl = Label(ventana, text="Contraseña SMTP: ")
lbl.place(x=20, y=70)
lbl.configure(foreground="white", background="#0a3143", font=("Arial Bold", 10))

#Se solicita la contraseña SMTP 
passw = Entry(ventana)
passw.place(x=130, y=70)
passw.configure(background="#cecfc9", font=("Arial", 12))
passw.configure(show="*")


#Se pide el correo que queremos enviar el mensaje
lbl = Label(ventana, text="Destinatario: ")
lbl.place(x=20, y=110)
lbl.configure(foreground="white", background="#0a3143", font=("Arial Bold", 10))
#Correo al que se envia
email = Entry(ventana)
email.place(x=125, y=110)
email.configure(background="#cecfc9", font=("Arial", 12))

#Se solicita escribir el asunto
lbl = Label(ventana, text="Asunto: ")
lbl.place(x=20, y=150)
lbl.configure(foreground="white", background="#0a3143", font=("Arial Bold", 10))
#Asunto
subject = Entry(ventana)
subject.place(x=125, y=150)
subject.configure(background="#cecfc9", font=("Arial", 12))

#Se solicita el mensaje a enviar
lbl = Label(ventana, text="Mensaje: ")
lbl.place(x=20, y=190)
lbl.configure(foreground="white", background="#0a3143", font=("Arial Bold", 10))
#Mensaje
message = Text(ventana)
message.place(x=80, y=220, width=550, height=200)
message.configure(background="white", font=("Arial", 11))

#Button para enviar el mensaje
btn = Button(ventana, text="Enviar", command=enviar)
btn.place(x=550, y=430)
btn.configure(foreground="white",background="#0a3143", font=("Arial", 11))

ventana.mainloop()

