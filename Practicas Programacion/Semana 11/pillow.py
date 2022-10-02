#Estudiantes
'''
EDWIN ADONY ULLOA DIAZ
SMIS001721
JULISSA YAMILETH HERNÁNDEZ CLAROS
SMIS082721
'''
#Importamos las librerias que utilizaremos de tkinter
from tkinter.font import BOLD
from PIL import Image, ImageTk, ImageFilter
from tkinter import Tk, Button, Label, filedialog
from tkinter import messagebox
#definimos color tamaño y botones de la ventana
ventana=Tk()
ventana.title("Mi primera vez usando pillow ")
ventana.geometry("2000x1000")
ventana.configure(bg="#002E94")

#carga de la imagen 
def cargar():
    archivo=filedialog.askopenfilename()
    imagen2=Image.open(archivo)
    render2=ImageTk.PhotoImage(imagen2)
    label2.configure(image=render2)
    label2.image=render2
    messagebox.showinfo('IMAGEN','Se cargo la imagen correctamente')
    
    #los filtros
def filtro1():
    imagen2 = imagen1
    imagen2.mode
    imagen2 = imagen2.convert("L")
    messagebox.showinfo('IMAGEN','Se aplico el filtro blanco negro')
    imagen2.show()

def filtro2():
    imagen2 = imagen1.filter(ImageFilter.BLUR)
    messagebox.showinfo('IMAGEN','Se aplico el filtro desenfocar ')
    imagen2.show()

def filtro3():
    imagen2 = imagen1.filter(ImageFilter.CONTOUR)
    messagebox.showinfo('IMAGEN','Se aplico el filtro contorno')
    imagen2.show()

def filtro4():
    imagen2 = imagen1.filter(ImageFilter.EMBOSS)
    messagebox.showinfo('IMAGEN','Se aplico el filtro resaltar')
    imagen2.show()


#Aqui abajo cargamos la imagen
imagen1= Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\Semana 11\lago.jpg")
reducir=imagen1.resize((200,200), Image.Resampling.LANCZOS)
render=ImageTk.PhotoImage(reducir)
render=ImageTk.PhotoImage(imagen1)
label1=Label(ventana,image=render)

#Cuadro donde aparece la imagen
label2=Label(ventana, image="")
label2.place(x=20, y=70,width=1000,height=550)

#Label del titulo
lbl1 = Label(ventana,text='PILLOW',fg = "#E1CEB5",bg='#002E94')
lbl1.place(x=0,y=20,width=200)
lbl1.config(font=("Verdana",20, BOLD))

#Boton de carga de la imagen
btn0=Button(ventana,text="CARGAR FOTOGRAFIA",
command=cargar,font=("Verdana",10), width=15, height=1,
bg="#083AA9", fg="#FFE7CC", activebackground="#743c92",activeforeground="#ffffff")
btn0.place(x=1100,y=350,width=200)

#Primer filtro
btn1 = Button(ventana, text="Filtro 1", command=filtro1,
font=("Verdana",10), width=10, height=1, bg="#004777", fg="#FFE7CC",
activebackground="#743c92",activeforeground="#ffffff" )
btn1.place(x=200,y=650) 

#Segundo filtro
btn2 = Button(ventana, text="Filtro 2", command=filtro2,
font=("Verdana",10), width=10, height=1, bg="#004777",fg="#FFE7CC",
activebackground="#743c92",activeforeground="#ffffff" )
btn2.place(x=400,y=650)

#tercer filtro
btn3 = Button(ventana, text="Filtro 3", command=filtro3,
font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff",
activebackground="#743c92",activeforeground="#ffffff")
btn3.place(x=600,y=650)

#cuarto filtro
btn4 = Button(ventana, text="Filtro 4", command=filtro4,
font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff",
activebackground="#743c92",activeforeground="#ffffff")
btn4.place(x=800,y=650)

ventana.mainloop()

