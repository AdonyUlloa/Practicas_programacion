#Estudiantes
'''
EDWIN ADONY ULLOA DIAZ
SMIS001721
JULISSA YAMILETH HERNÁNDEZ CLAROS
SMIS082721
'''
#Importamos las librerias que utilizaremos de tkinter

from tkinter.font import BOLD
from tkinter import *
from PIL import Image, ImageFilter, ImageTk
from tkinter import messagebox

#Funcion para la factura
def calcular():
    n1= num1.get()
    pup = pupusa.get()
    beb = bebida.get()
    dom = domi.get()
    messagebox.showinfo('COMPRA','Mirar factura en consola')
    
    #Diferentes if y elif
    #Queso
    if n1 and pup and beb and dom == False:
        print("Falta selecionar datos")
    elif pup == 1:
        #Gaseosa
        if beb == 1:
            if dom == 1:
                print("====================================================")
                print( "Producto     Cantidad     Precio \n Queso      ", n1, "        $", 0.70*n1, "\n Gaseosa      -          $0.75 \n Costo de envio      -    $1.50 \n           Total:        $",(0.70*n1)+0.75+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Queso      ", n1, "        $", 0.70*n1, "\n Gaseosa      -          $0.75 \n Costo de envio      -    $0.00 \n           Total:        $",(0.70*n1)+0.75 )
        #Chocolaate
        elif beb == 2:
            if dom == 1:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Queso      ", n1, "        $", 0.70*n1, "\n Chocolate    -          $0.50 \n Costo de envio      -    $1.50 \n           Total:        $",(0.70*n1)+0.50+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Queso      ", n1, "        $", 0.70*n1, "\n Chocolate    -          $0.50 \n Costo de envio      -    $0.00 \n           Total:        $",(0.70*n1)+0.50 )
        #Fresco
        elif beb == 3:
            if dom == 1:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Queso      ", n1, "        $", 0.70*n1, "\n Fresco       -          $0.60 \n Costo de envio      -    $1.50 \n           Total:        $",(0.70*n1)+0.60+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Queso      ", n1, "        $", 0.70*n1, "\n Fresco       -          $0.60 \n Costo de envio      -    $0.00 \n           Total:        $",(0.70*n1)+0.60 )
        
        
    #FyQ     
    elif pup == 2:
        #Gaseosa
        if beb == 1:
            if dom == 1:
                print("====================================================")
                print("Producto     Cantidad     Precio \n FyQ       ", n1, "        $", 0.65*n1, "\n Gaseosa      -          $0.75 \n Costo de envio      -    $1.50 \n           Total:        $",(0.65*n1)+0.75+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n FyQ        ", n1, "        $", 0.65*n1, "\n Gaseosa      -          $0.75 \n Costo de envio      -    $0.00 \n           Total:        $",(0.65*n1)+0.75 )
        #Chocolaate
        elif beb == 2:
            if dom == 1:
                print("====================================================")
                print("Producto     Cantidad     Precio \n FyQ        ", n1, "        $", 0.65*n1, "\n Chocolate    -          $0.50 \n Costo de envio      -    $1.50 \n           Total:        $",(0.65*n1)+0.50+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n FyQ        ", n1, "        $", 0.65*n1, "\n Chocolate    -          $0.50 \n Costo de envio      -    $0.00 \n           Total:        $",(0.65*n1)+0.50 )
        #Fresco
        elif beb == 3:
            if dom == 1:
                print("====================================================")
                print("Producto     Cantidad     Precio \n FyQ        ", n1, "        $", 0.65*n1, "\n Fresco       -          $0.60 \n Costo de envio      -    $1.50 \n           Total:        $",(0.65*n1)+0.60+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n FyQ        ", n1, "        $", 0.65*n1, "\n Fresco       -          $0.60 \n Costo de envio      -    $0.00 \n           Total:        $",(0.65*n1)+0.60 )
   
    #Revueltas               
    elif pup == 3:
        #Gaseosa
        if beb == 1:
            if dom == 1:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Revueltas  ", n1, "        $", 0.60*n1, "\n Gaseosa      -          $0.75 \n Costo de envio      -    $1.50 \n           Total:        $",(0.60*n1)+0.75+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Revueltas  ", n1, "        $", 0.60*n1, "\n Gaseosa      -          $0.75 \n Costo de envio      -    $0.00 \n           Total:        $",(0.60*n1)+0.75 )
        #Chocolaate
        elif beb == 2:
            if dom == 1:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Revueltas  ", n1, "        $", 0.60*n1, "\n Chocolate    -          $0.50 \n Costo de envio      -    $1.50 \n           Total:        $",(0.60*n1)+0.50+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Revueltas  ", n1, "        $", 0.60*n1, "\n Chocolate    -          $0.50 \n Costo de envio      -    $0.00 \n           Total:        $",(0.60*n1)+0.50 )
        #Fresco
        elif beb == 3:
            if dom == 1:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Revueltas  ", n1, "        $", 0.60*n1, "\n Fresco       -          $0.60 \n Costo de envio      -    $1.50 \n           Total:        $",(0.60*n1)+0.60+1.50 )
            elif dom == 2:
                print("====================================================")
                print("Producto     Cantidad     Precio \n Revueltas  ", n1, "        $", 0.60*n1, "\n Fresco       -          $0.60 \n Costo de envio      -    $0.00 \n           Total:        $",(0.60*n1)+0.60 )
    
    else:
        print("Faltan datos por ingresar")
        
#Inciamos tk
ventana=Tk()
#Declaramos variables para captura de datos
num1 = DoubleVar()
pupusa=IntVar()
bebida=IntVar()
domi=IntVar()
#configuramos ventana
ventana.title("Pupuseria rosita")
ventana.geometry("1200x650")
ventana.configure(bg="#002E94")

#Label de titutlo
lbl1 = Label(ventana,text='ROSITA SV', fg="#FFFFFF",bg='#002E94')
lbl1.place(x=0,y=20,width=200)
lbl1.config(font=("Verdana",15, BOLD))

#label especialidades de pupusas
lbl1 = Label(ventana,text='ESPECIALIDADES',fg = "#E1CEB5",bg='#002E94')
lbl1.place(x=450,y=40,width=200)
lbl1.config(font=("Verdana",15, BOLD))

#Diferentesimagenes y radio button para pupusas

#1
imagen1 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\pu_qu.jpg")
imagen1 = imagen1.filter(ImageFilter.SHARPEN)
photo1 = ImageTk.PhotoImage(imagen1)
reducida1 = imagen1.resize((100,100), Image.Resampling.LANCZOS)
photo1= ImageTk.PhotoImage(reducida1)
label1 = Label(ventana, image=photo1)
label1.place(x=200,y=100)
radio1=Radiobutton(ventana, text="QUESO" , value=1 , variable=pupusa)
radio1.place(x=210, y=230)
radio1.configure(bg="#002E94", fg="#FFFFFF")

#2
imagen2 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\pu_fyq.jpg")
imagen2 = imagen2.filter(ImageFilter.SHARPEN)
photo2 = ImageTk.PhotoImage(imagen2)
reducida2 = imagen2.resize((100,100), Image.Resampling.LANCZOS)
photo2= ImageTk.PhotoImage(reducida2)
label2 = Label(ventana, image=photo2)
label2.place(x=510,y=100)
radio2=Radiobutton(ventana, text="F/Q" , value=2 , variable=pupusa)
radio2.place(x=520, y=230)
radio2.configure(bg="#002E94", fg="#FFFFFF")

#3
imagen3 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\pu_re.jpg")
imagen3 = imagen3.filter(ImageFilter.SHARPEN)
photo3 = ImageTk.PhotoImage(imagen3)
reducida3 = imagen3.resize((100,100), Image.Resampling.LANCZOS)
photo3= ImageTk.PhotoImage(reducida3)
label3= Label(ventana, image=photo3)
label3.place(x=800,y=100)
radio3=Radiobutton(ventana, text="REVUELTAS" , value=3 , variable=pupusa)
radio3.place(x=830, y=230)
radio3.configure(bg="#002E94", fg="#FFFFFF")

#Label de la bebidas
lb4= Label(ventana,text='Bebidas',fg = "#E1CEB5",bg='#002E94')
lb4.place(x=450,y=340,width=200)
lb4.config(font=("Verdana",15, BOLD))


#Diferentesimagenes y radio button para bebidas
#4
imagen4 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\coca.jpg")
imagen4 = imagen4.filter(ImageFilter.SHARPEN)
photo4 = ImageTk.PhotoImage(imagen4)
reducida4 = imagen4.resize((100,100), Image.Resampling.LANCZOS)
photo4= ImageTk.PhotoImage(reducida4)
label2 = Label(ventana, image=photo4)
label2.place(x=200,y=400)
radio4=Radiobutton(ventana, text="Gaseosa" , value=1 , variable=bebida)
radio4.place(x=210, y=520)
radio4.configure(bg="#002E94", fg="#FFFFFF")

#5
imagen5 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\choc.jpg")
imagen5 = imagen5.filter(ImageFilter.SHARPEN)
photo5 = ImageTk.PhotoImage(imagen5)
reducida5 = imagen5.resize((100,100), Image.Resampling.LANCZOS)
photo5= ImageTk.PhotoImage(reducida1)
label5 = Label(ventana, image=photo5)
label5.place(x=500,y=400)
radio5=Radiobutton(ventana, text="Chocolate" , value=2 , variable=bebida)
radio5.place(x=510, y=520)
radio5.configure(bg="#002E94", fg="#FFFFFF")

#6
imagen6 = Image.open(r"C:\Users\PC\Documents\Programacion\Practicas Programacion\SEMANA 13 PARCIALES\fresco.jpg")
imagen6 = imagen6.filter(ImageFilter.SHARPEN)
photo6 = ImageTk.PhotoImage(imagen6)
reducida6 = imagen6.resize((100,100), Image.Resampling.LANCZOS)
photo6= ImageTk.PhotoImage(reducida6)
label6 = Label(ventana, image=photo6)
label6.place(x=800,y=400)
radio6=Radiobutton(ventana, text="Fresco" , value=3 , variable=bebida)
radio6.place(x=810, y=520)
radio6.configure(bg="#002E94", fg="#FFFFFF")



#label de domiciolio y radio button
lb8=Label(ventana,text="Domicilio", background="#5DADE2")
lb8.place(x=390, y=600)
lb8.configure(bg="#002E94", fg="#FFFFFF")
radio7=Radiobutton(ventana, text="si" , value=1 , variable=domi)
radio7.place(x=450, y=600)
radio7.configure(bg="#002E94", fg="#FFFFFF")
radio8=Radiobutton(ventana, text="no" , value=2 , variable=domi)
radio8.place(x=500, y=600)
radio8.configure(bg="#002E94", fg="#FFFFFF")

#label y box de cantidad de pupusas
lb8=Label(ventana,text="Cantidad", background="#5DADE2")
lb8.place(x=1000, y=250)
lb8.configure(bg="#002E94", fg="#FFFFFF")
cant=Entry(ventana, font=10, bg="white", textvariable=num1)
cant.place(x=1060, y=250, width=100)


#Button que manda a imprimir
btn=Button(ventana, text="Imprimir Factura", command=calcular)
btn.place(x=1000,y=550, width=150, height= 50)
btn. configure( bg= "#00aae4")

ventana.mainloop()