from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)
mainFrame = Frame(root, bg="grey")
mainFrame.pack()


operation = ""
result = 0
last_operation = None
sub_count = 0
mult_count = 0
div_count = 0

# Código para la screen

screenNumber = StringVar()
screenNumber.set("0")         # Inicializamos el valor de la calculadora

screen = Entry(mainFrame, justify="right", bg="black", fg="white", textvariable=screenNumber)
screen.grid(column=0, row=0, padx=10, pady=10, columnspan=4, ipadx=130)

# Funciones pulsamiento

def numeroPulsado(num):
    
    global operation
    if operation != "":
        screenNumber.set(num)
        operation = ""
    else:
        # Limita la cantidad de "0"s que se pueden introducir a la izquierda de un número
        if num == "0" and screenNumber.get() == "0":
            screenNumber.set(screenNumber.get())
        # Permite escribir valores flotantes con un "0" delante
        elif num == "." and screenNumber.get() == "0":
            screenNumber.set("0" + num)
        # Borra el "0" inicial para escribir el primer número introducido
        elif screenNumber.get() == "0":
            screenNumber.set(num)   
        # Limita el número de comas que se introducen
        elif num == "." and num in screenNumber.get():
            screenNumber.set(screenNumber.get())
        # Agrega los nuevos números uno tras otro.     
        else:    
            screenNumber.set(screenNumber.get() + num)
    
def cleanWindow():
    
    global result
    global sub_count
    global mult_count
    global div_count
    global last_operation
    
    last_operation = None
    screenNumber.set("0")
    result = 0
    sub_count = 0
    mult_count = 0
    div_count = 0
    
def operationPressed(op):
    
    global operation
    global result
    global last_operation
    global sub_count
    global mult_count
    global div_count
    
    operation = op
    last_operation = op
       
    match(op):
        case "sum":
            result += float(screenNumber.get())
            screenNumber.set("0")
        case "substract":
            if sub_count == 0:
                result = float(screenNumber.get())
                sub_count += 1
                screenNumber.set("0")
            else:
                result -= float(screenNumber.get())
                screenNumber.set("0")
        case "multiply":
            if mult_count == 0:
                result = float(screenNumber.get())
                mult_count += 1
            else:
                result *= float(screenNumber.get())
        case "divide":
            if div_count == 0:
                result = float(screenNumber.get())
                div_count += 1
            else:
                if float(screenNumber.get()) == 0:
                    screenNumber.set("Error, press 'C' to reset")
                    result = 0
                else:      
                    result /= float(screenNumber.get())
                    
def pressEquals():
    
    global result
    global last_operation
    global sub_count
    global mult_count
    global div_count
    
    print("Process: ", last_operation)
    match last_operation:
        case "sum":
            screenNumber.set(result + float(screenNumber.get()))   
        case "substract":
            screenNumber.set(result - float(screenNumber.get()))
            sub_count = 0
        case "multiply":
            screenNumber.set(result * float(screenNumber.get()))
            mult_count = 0
        case "divide":
            if float(screenNumber.get()) == 0:
                screenNumber.set("Error, press 'C' to reset")
                result = 0
            else: 
                screenNumber.set(result / float(screenNumber.get()))
                div_count = 0
        case _:
            screenNumber.set("0")
                            
    last_operation = None        
    result = 0
            
            


# Linea funcionalidades

botonReset = Button(mainFrame, width=10, height=3, cursor="hand2", text="C", command=cleanWindow)
botonReset.grid(column=3, row=1, padx=10, pady=10)

# Primera fila de botones

boton7 = Button(mainFrame, width=10, height=3, cursor="hand2", text="7", command=lambda:numeroPulsado("7"))
boton7.grid(column=0, row=2, padx=10, pady=10)
boton8 = Button(mainFrame, width=10, height=3, cursor="hand2", text="8", command=lambda:numeroPulsado("8"))
boton8.grid(column=1, row=2, padx=10, pady=10)
boton9 = Button(mainFrame, width=10, height=3, cursor="hand2", text="9", command=lambda:numeroPulsado("9"))
boton9.grid(column=2, row=2, padx=10, pady=10)
botonDiv = Button(mainFrame, width=10, height=3, cursor="hand2", text="/", command=lambda:operationPressed("divide"))
botonDiv.grid(column=3, row=2, padx=10, pady=10)

# Segunda fila de botones

boton4 = Button(mainFrame, width=10, height=3, cursor="hand2", text="4", command=lambda:numeroPulsado("4"))
boton4.grid(column=0, row=3, padx=10, pady=10)
boton5 = Button(mainFrame, width=10, height=3, cursor="hand2", text="5", command=lambda:numeroPulsado("5"))
boton5.grid(column=1, row=3, padx=10, pady=10)
boton6 = Button(mainFrame, width=10, height=3, cursor="hand2", text="6", command=lambda:numeroPulsado("6"))
boton6.grid(column=2, row=3, padx=10, pady=10)
botonX = Button(mainFrame, width=10, height=3, cursor="hand2", text="X", command=lambda:operationPressed("multiply"))
botonX.grid(column=3, row=3, padx=10, pady=10)

# Tercera fila de botones

boton1 = Button(mainFrame, width=10, height=3, cursor="hand2", text="1", command=lambda:numeroPulsado("1"))
boton1.grid(column=0, row=4, padx=10, pady=10)
boton2 = Button(mainFrame, width=10, height=3, cursor="hand2", text="2", command=lambda:numeroPulsado("2"))
boton2.grid(column=1, row=4, padx=10, pady=10)
boton3 = Button(mainFrame, width=10, height=3, cursor="hand2", text="3", command=lambda:numeroPulsado("3"))
boton3.grid(column=2, row=4, padx=10, pady=10)
botonMenos = Button(mainFrame, width=10, height=3, cursor="hand2", text="-", command=lambda:operationPressed("substract"))
botonMenos.grid(column=3, row=4, padx=10, pady=10)

# Cuarta fila de botones

boton0 = Button(mainFrame, width=10, height=3, cursor="hand2", text="0", command=lambda:numeroPulsado("0"))
boton0.grid(column=0, row=5, padx=10, pady=10)
botonCom = Button(mainFrame, width=10, height=3, cursor="hand2", text=",",  command=lambda:numeroPulsado("."))
botonCom.grid(column=1, row=5, padx=10, pady=10)
botonIgual = Button(mainFrame, width=10, height=3, cursor="hand2", text="=", command=lambda:pressEquals())
botonIgual.grid(column=2, row=5, padx=10, pady=10)
botonMas = Button(mainFrame, width=10, height=3, cursor="hand2", text="+", command=lambda:operationPressed("sum"))
botonMas.grid(column=3, row=5, padx=10, pady=10)

root.mainloop()