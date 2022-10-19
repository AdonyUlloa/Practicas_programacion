from tkinter.font import BOLD
from PIL import Image, ImageTk, ImageFilter
from tkinter import Tk, Button, Label, filedialog
from tkinter import messagebox

ventana=Tk()
ventana.title("Pupuseria rosita")
ventana.geometry("2000x1000")
ventana.configure(bg="#002E94")

lbl1 = Label(ventana,text='ROSITA SV',fg = "#E1CEB5",bg='#002E94')
lbl1.place(x=0,y=20,width=200)
lbl1.config(font=("Verdana",15, BOLD))

lbl1 = Label(ventana,text='ESPECIALIDADES',fg = "#E1CEB5",bg='#002E94')
lbl1.place(x=600,y=40,width=200)
lbl1.config(font=("Verdana",15, BOLD))


imagen1 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\pu_q.png")
imagen1 = imagen1.filter(ImageFilter.SHARPEN)
photo1 = ImageTk.PhotoImage(imagen1)
reducida1 = imagen1.resize((100,100), Image.Resampling.LANCZOS)
photo1= ImageTk.PhotoImage(reducida1)
label1 = Label(ventana, image=photo1)
label1.place(x=500,y=100)


imagen2 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\pu_fyq.jpg")
imagen2 = imagen1.filter(ImageFilter.SHARPEN)
photo2 = ImageTk.PhotoImage(imagen2)
reducida2 = imagen2.resize((100,100), Image.Resampling.LANCZOS)
photo2= ImageTk.PhotoImage(reducida2)
label2 = Label(ventana, image=photo2)
label2.place(x=500,y=100)

imagen3 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\pu_r.png")
imagen3 = imagen3.filter(ImageFilter.SHARPEN)
photo3 = ImageTk.PhotoImage(imagen3)
reducida3 = imagen3.resize((100,100), Image.Resampling.LANCZOS)
photo3= ImageTk.PhotoImage(reducida3)
label3= Label(ventana, image=photo3)
label3.place(x=500,y=100)

imagen1 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\coca.png")
imagen1 = imagen1.filter(ImageFilter.SHARPEN)
photo1 = ImageTk.PhotoImage(imagen1)
reducida1 = imagen1.resize((100,100), Image.Resampling.LANCZOS)
photo1= ImageTk.PhotoImage(reducida1)
label2 = Label(ventana, image=photo1)
label2.place(x=500,y=100)

imagen1 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\choc.png")
imagen1 = imagen1.filter(ImageFilter.SHARPEN)
photo1 = ImageTk.PhotoImage(imagen1)
reducida1 = imagen1.resize((100,100), Image.Resampling.LANCZOS)
photo1= ImageTk.PhotoImage(reducida1)
label2 = Label(ventana, image=photo1)
label2.place(x=500,y=100)

imagen1 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\fresco.png")
imagen1 = imagen1.filter(ImageFilter.SHARPEN)
photo1 = ImageTk.PhotoImage(imagen1)
reducida1 = imagen1.resize((100,100), Image.Resampling.LANCZOS)
photo1= ImageTk.PhotoImage(reducida1)
label2 = Label(ventana, image=photo1)
label2.place(x=500,y=100)


ventana.mainloop()