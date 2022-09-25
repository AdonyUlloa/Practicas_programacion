#Estudiantes
'''
EDWIN ADONY ULLOA DIAZ
SMIS001721
JULISSA YAMILETH HERNÁNDEZ CLAROS
SMIS082721
'''

#Importamos las librerias que utilizaremos de tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
#Decidimos titulo, tamaño y color de la ventana.
root.title('Calculadora')
root.geometry('400x380')
root.configure(background='#87CEFA')

#Usaremos para capturar los datos
num1=IntVar()
num2=IntVar()

#Funcion que los servira para hacer las operaciones de la calculadora
def calcular():
	#Aqui se hace la suma
	if opc.get()==1:
		resul=num1.get()+num2.get()
		messagebox.showinfo("Resultado",resul)
	#Aqui se hace la resta
	elif opc.get()==2:
		resul=num1.get()-num2.get()
		messagebox.showinfo("Resultado",resul)
	#Aqui se hace la multiplicacion
	elif opc.get()==3:
		resul=num1.get()*num2.get()
		messagebox.showinfo("Resultado",resul)
	#Aqui se hace la division
	elif opc.get()==4:
		resul=num1.get()/num2.get()
		messagebox.showinfo("Resultado",resul)
	#Aqui se hace el modulo
	elif opc.get()==5:
		resul=num1.get()%num2.get()
		messagebox.showinfo("Resultado",resul)
	#Aqui se hace el exponente
	elif opc.get()==6:
		resul=num1.get()**num2.get()
		messagebox.showinfo("Resultado",resul)
	#opcion por si no selecciona una operacion.
	else:
		messagebox.showinfo("Error","Seleccione una opción")


#Los label
lbl0=Label(root,text='=============',fg = "blue",bg='#87CEFA')
lbl0.place(x=100,y=10,width=200)

lbl1 = Label(root,text='CALCULADORA',fg = "blue",bg='#87CEFA')
lbl1.place(x=100,y=40,width=200)

lbl2=Label(root,text='=============',fg = "blue",bg='#87CEFA')
lbl2.place(x=100,y=70,width=200)

lbl3=Label(root,text='Numero 1',fg = "purple",bg='#87CEFA')
lbl3.place(x=200,y=100,width=50)

#Ingreso de primer dato
et1=Entry(root,justify='center',bg='#20B2AA',textvariable=num1,fg = "red")
et1.place(x=120,y=100,width=60)

lbl5=Label(root,text='Numero 2',fg = "purple",bg='#87CEFA')
lbl5.place(x=195,y=150,width=60)

#Ingreso de segundo dato
et2=Entry(root,justify='center',bg='#20B2AA',textvariable=num2,fg = "red")
et2.place(x=120,y=150,width=60)

opc=IntVar()

#Los radiobutton
lbl7=Label(root,text='==============================================',fg = "blue",bg='#87CEFA')
lbl7.place(x=-50,y=200,width=500)

rdb1=Radiobutton(root,text="Suma",fg = "purple",variable=opc,value=1,bg='#87CEFA')
rdb1.place(x=10,y=250,width=50)

rdb2=Radiobutton(root,text="Resta",fg = "purple",variable=opc,value=2,bg='#87CEFA')
rdb2.place(x=70,y=250,width=50)

rdb4=Radiobutton(root,text="Multiplicacion",fg = "purple",variable=opc,value=3,bg='#87CEFA')
rdb4.place(x=130,y=250,width=100)

rdb5=Radiobutton(root,text="Modulo",fg = "purple",variable=opc,value=5,bg='#87CEFA')
rdb5.place(x=228,y=250,width=80)

rdb6=Radiobutton(root,text="Exponente",fg = "purple",variable=opc,value=6,bg='#87CEFA')
rdb6.place(x=305,y=250,width=80)

lbl8=Label(root,text='==============================================',fg = "blue",bg='#87CEFA')
lbl8.place(x=-50,y=300,width=500)

#Button para hacer las operaciones
btn=Button(root,text='Calcular',bg='#FF1493',width=10,command=calcular)
btn.place(x=160,y=330)

root.mainloop()