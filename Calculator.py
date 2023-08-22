'''
This is my first "serious" project. I tried building a calculator with the Tkinter module. The main purpose of this project is to learn and practise some pyton code.
I managed to make it work, but the calculator doesn't allow multiples operations without hitting the "=" button first. 
'''

from tkinter import *

# Definition of the root, making it not resizable and creating a frame
root = Tk()
root.title("Calculator")
root.resizable(False, False)
main_frame = Frame(root, bg="grey")
main_frame.pack()


# Definition fo some global variables. (I know is not a good practice but when I started it sounded good)
operation = ""
result = 0
last_operation = None
sub_count = 0
mult_count = 0
div_count = 0


# Screen code
screen_number = StringVar()
screen_number.set("0")         # Initialize the screen value

screen = Entry(main_frame, justify="right", bg="black", fg="white", textvariable=screen_number)
screen.grid(column=0, row=0, padx=10, pady=10, columnspan=4, ipadx=130)


def number_pushed(num):
    '''
    This function lets the user insert numbers into the screen. It has some basic restrictions,
    such as not allowing more than one '0' at the start (only if it has a decimal part: '0.8' but not '08') and allowing
    only one '.', clearing the initial '0' on the screen.
    '''
    global operation
    if operation != "":
        screen_number.set(num)
        operation = ""
    else:
        # Limits the amount of '0' that can be introduce at the left of the number
        if num == "0" and screen_number.get() == "0":
            screen_number.set(screen_number.get())
        # Allows to introduce one '0' at the start to acces its floating part.
        elif num == "." and screen_number.get() == "0":
            screen_number.set("0" + num)
        # Deletes the initial '0' to write the introduced number
        elif screen_number.get() == "0":
            screen_number.set(num)   
        # Limits the number of '.' intoduced
        elif num == "." and num in screen_number.get():
            screen_number.set(screen_number.get())
        # Agregates to the screen the intoduced numbers one after another.     
        else:    
            screen_number.set(screen_number.get() + num)
    

def clean_window():
    '''
    This function resets every variable and cleans the elements on the screen
    '''
    global result
    global sub_count
    global mult_count
    global div_count
    global last_operation
    
    last_operation = None
    screen_number.set("0")
    result = 0
    sub_count = 0
    mult_count = 0
    div_count = 0

    
def operation_pressed(op):
    '''
    This function stores the number on the screen after pressing an operation button. Each case has its own logic, not 
    all of them work the same way
    '''
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
            result += float(screen_number.get())
            screen_number.set("0")
        case "substract":
            if sub_count == 0:
                result = float(screen_number.get())
                sub_count += 1
                screen_number.set("0")
            else:
                result -= float(screen_number.get())
                screen_number.set("0")
        case "multiply":
            if mult_count == 0:
                result = float(screen_number.get())
                mult_count += 1
            else:
                result *= float(screen_number.get())
        case "divide":
            if div_count == 0:
                result = float(screen_number.get())
                div_count += 1
            else:
                if float(screen_number.get()) == 0:
                    screen_number.set("Error, press 'C' to reset")
                    result = 0
                else:      
                    result /= float(screen_number.get())
                    
                    
def press_equals():
    '''
    This function acts when the equals button is pressed. It performs the final operation to the value stored in result among the process.
    '''
    global result
    global last_operation
    global sub_count
    global mult_count
    global div_count
    
    match last_operation:
        case "sum":
            screen_number.set(result + float(screen_number.get()))   
        case "substract":
            screen_number.set(result - float(screen_number.get()))
            sub_count = 0
        case "multiply":
            screen_number.set(result * float(screen_number.get()))
            mult_count = 0
        case "divide":
            if float(screen_number.get()) == 0:
                screen_number.set("Error, press 'C' to reset")
                result = 0
            else: 
                screen_number.set(result / float(screen_number.get()))
                div_count = 0
        case _:
            screen_number.set("0")
                            
    last_operation = None        
    result = 0
            
            
# Functionality line in the calculator
reset_button = Button(main_frame, width=10, height=3, cursor="hand2", text="C", command=clean_window)
reset_button.grid(column=3, row=1, padx=10, pady=10)

# First line of buttons
button7 = Button(main_frame, width=10, height=3, cursor="hand2", text="7", command=lambda:number_pushed("7"))
button7.grid(column=0, row=2, padx=10, pady=10)
button8 = Button(main_frame, width=10, height=3, cursor="hand2", text="8", command=lambda:number_pushed("8"))
button8.grid(column=1, row=2, padx=10, pady=10)
button9 = Button(main_frame, width=10, height=3, cursor="hand2", text="9", command=lambda:number_pushed("9"))
button9.grid(column=2, row=2, padx=10, pady=10)
division_button = Button(main_frame, width=10, height=3, cursor="hand2", text="/", command=lambda:operation_pressed("divide"))
division_button.grid(column=3, row=2, padx=10, pady=10)

# Second line of buttons
button4 = Button(main_frame, width=10, height=3, cursor="hand2", text="4", command=lambda:number_pushed("4"))
button4.grid(column=0, row=3, padx=10, pady=10)
button5 = Button(main_frame, width=10, height=3, cursor="hand2", text="5", command=lambda:number_pushed("5"))
button5.grid(column=1, row=3, padx=10, pady=10)
button6 = Button(main_frame, width=10, height=3, cursor="hand2", text="6", command=lambda:number_pushed("6"))
button6.grid(column=2, row=3, padx=10, pady=10)
buttonX = Button(main_frame, width=10, height=3, cursor="hand2", text="X", command=lambda:operation_pressed("multiply"))
buttonX.grid(column=3, row=3, padx=10, pady=10)

# Third line of buttons
button1 = Button(main_frame, width=10, height=3, cursor="hand2", text="1", command=lambda:number_pushed("1"))
button1.grid(column=0, row=4, padx=10, pady=10)
button2 = Button(main_frame, width=10, height=3, cursor="hand2", text="2", command=lambda:number_pushed("2"))
button2.grid(column=1, row=4, padx=10, pady=10)
button3 = Button(main_frame, width=10, height=3, cursor="hand2", text="3", command=lambda:number_pushed("3"))
button3.grid(column=2, row=4, padx=10, pady=10)
minus_button = Button(main_frame, width=10, height=3, cursor="hand2", text="-", command=lambda:operation_pressed("substract"))
minus_button.grid(column=3, row=4, padx=10, pady=10)

# Fourth line of buttons
button0 = Button(main_frame, width=10, height=3, cursor="hand2", text="0", command=lambda:number_pushed("0"))
button0.grid(column=0, row=5, padx=10, pady=10)
dot_button = Button(main_frame, width=10, height=3, cursor="hand2", text=",",  command=lambda:number_pushed("."))
dot_button.grid(column=1, row=5, padx=10, pady=10)
equals_button = Button(main_frame, width=10, height=3, cursor="hand2", text="=", command=lambda:press_equals())
equals_button.grid(column=2, row=5, padx=10, pady=10)
plus_button = Button(main_frame, width=10, height=3, cursor="hand2", text="+", command=lambda:operation_pressed("sum"))
plus_button.grid(column=3, row=5, padx=10, pady=10)

# Constant loop to run the app
root.mainloop()