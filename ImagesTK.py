

from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title('Picture Changer')




my_image1 =ImageTk.PhotoImage(Image.open("one.jpg"))
my_image2 =ImageTk.PhotoImage(Image.open("two.jpg"))
my_image3 =ImageTk.PhotoImage(Image.open("three.jpg"))
my_image4 =ImageTk.PhotoImage(Image.open("four.jpg"))


image_list = [my_image1,my_image2, my_image3, my_image4]


my_label = Label(image=my_image1)
my_label.grid(row=0, column= 0, columnspan=3)


def forward(image_count):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_count-1])

   
    button_forward= Button(root, text=">>", command=lambda: forward(image_count + 1))
    button_back=Button(root, text="<<",command=lambda: back(image_count -1))

    if image_count ==4:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    


    

def back(image_count):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_count-1])

    button_forward= Button(root, text=">>", command=lambda: forward(image_count + 1))
    button_back=Button(root, text="<<",command=lambda: back(image_count -1))
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


    if image_count == 1:
        button_back = Button(root, text="<<", state=DISABLED)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text=" Exit Program" , command= root.quit)
button_forward = Button(root, text=">>" , command=lambda:forward(2))



button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()