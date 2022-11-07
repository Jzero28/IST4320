

from tkinter import *

root = Tk()
root.title("My Calculator")

#show input in bar
entry_one= Entry(root, width=35, borderwidth=5)
entry_one.grid(row=0,column=0,columnspan=3, padx=10 , pady=10 )

# removed current number to show next number
def button_click(number):
    current_number = entry_one.get()
    entry_one.delete(0,END)
    entry_one.insert(0, str(current_number) + str(number))

#button to clear current number displayed
def button_clear():
    entry_one.delete(0,END)

#addtion of numbers selected
def button_add():
    first_number=entry_one.get()
    global f_num
    global math
    math = "addition"
    f_num= int(first_number)
    entry_one.delete(0,END)
   
# produced the solution based on the operataion chosen 
def button_equal():
    second_number= entry_one.get()
    entry_one.delete(0, END)

    if math == "addition":
        entry_one.insert(0, f_num + int(second_number))

    if math == "subtraction":
        entry_one.insert(0, f_num - int(second_number))

    if math == "multiplication":
        entry_one.insert(0, f_num * int(second_number))

    if math == "division":
        entry_one.insert(0, f_num / int(second_number))

   
# button to perform substraction
def button_subtract():
    first_number=entry_one.get()
    global f_num
    global math
    math= "subtraction"
    f_num= int(first_number)
    entry_one.delete(0,END)
   
#button to perform multiplication
def button_multiply():
    first_number=entry_one.get()
    global f_num
    global math
    math= "multiplication"
    f_num= int(first_number)
    entry_one.delete(0,END)
   
#Button to perform division
def button_divide():
    first_number=entry_one.get()
    global f_num
    global math
    math= "division"
    f_num= int(first_number)
    entry_one.delete(0,END)



#Define Buttons
button_1 = Button(root, text='1', padx= 40, pady=20,command=lambda:button_click(1) )
button_2 = Button(root, text='2', padx= 40, pady=20,command=lambda:button_click(2) )
button_3 = Button(root, text='3', padx= 40, pady=20,command=lambda:button_click(3) )
button_4 = Button(root, text='4', padx= 40, pady=20,command=lambda:button_click(4) )
button_5 = Button(root, text='5', padx= 40, pady=20,command=lambda:button_click(5))
button_6 = Button(root, text='6', padx= 40, pady=20,command=lambda:button_click(6) )
button_7 = Button(root, text='7', padx= 40, pady=20,command=lambda:button_click(7) )
button_8 = Button(root, text='8', padx= 40, pady=20,command=lambda:button_click(8) )
button_9 = Button(root, text='9', padx= 40, pady=20,command=lambda:button_click(9))
button_0 = Button(root, text='0', padx= 40, pady=20,command=lambda:button_click(0) )

#add button
button_add = Button(root, text='+', padx= 39, pady=20,command=button_add)

#eqaul button
button_equal = Button(root, text='=', padx= 92, pady=20,command=button_equal )

#clear button
button_clear = Button(root, text='Clear', padx= 79, pady=20,command= button_clear )

#subtract, multiply, and divide buttons
button_subtract = Button(root, text='-', padx= 41, pady=20,command=button_subtract)
button_multiply = Button(root, text='x', padx= 40, pady=20,command=button_multiply)
button_divide = Button(root, text='/', padx= 41, pady=20,command=button_divide)


#Display Bottons
button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)

button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column= 2)

button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)

button_0.grid(row= 4,column= 0)

button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row= 5,column= 0)
button_equal.grid(row= 5,column= 1, columnspan=2)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

                                            

root.mainloop()