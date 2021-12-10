from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

def rotate_image1(degrees):
    new_image = image1.rotate(-int(degrees))
    photoimage1 = ImageTk.PhotoImage(new_image)
    label1.image = photoimage1 
    label1.config(image = photoimage1)
def rotate_image2(degrees):
    new_image = image2.rotate(-int(degrees))
    photoimage2 = ImageTk.PhotoImage(new_image)
    label2.image = photoimage2 
    label2.config(image = photoimage2)
def rotate_image3(degrees):
    new_image = image3.rotate(-int(degrees))
    photoimage3 = ImageTk.PhotoImage(new_image)
    label3.image = photoimage3 
    label3.config(image = photoimage3)
root = Tk()
root.title("PLANE GUI")


image1 = Image.open("plane_side_no-bg.png")
photoimage1 = ImageTk.PhotoImage(image1)
image2 = Image.open("plane_front_no-bg.png")
photoimage2 = ImageTk.PhotoImage(image2)
image3 = Image.open("plane_top_no-bg.png")
photoimage3 = ImageTk.PhotoImage(image3)

label1 = Label(root, image=photoimage1)
label1.image = photoimage1
label2 = Label(root, image=photoimage2)
label2.image = photoimage2
label3 = Label(root, image=photoimage3)
label3.image = photoimage3


blank_label1 = Label(root, text="  ")
blank_label2 = Label(root, text="  ")
blank_label3 = Label(root, text="  ")

e1 = Entry(root,width=40,bg="sky blue",fg="black",border=5)
e2 = Entry(root,width=40,bg="sky blue",fg="black",border=5)
e3 = Entry(root,width=40,bg="sky blue",fg="black",border=5)

# j = e1.get()
# k = e2.get()
# l = e3.get()

blabel1 = Label(root, text="  ")
blabel2 = Label(root, text="  ")
blabel3 = Label(root, text="  ")

b1= Scale(root,from_=-360, to=360,orient=HORIZONTAL,length=360, command=rotate_image1)
b2 = Scale(root,from_=-360, to=360,orient=HORIZONTAL,length=360,command=rotate_image2)
b3 = Scale(root,from_=-360, to=360,orient=HORIZONTAL,length=360,command=rotate_image3)

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)

blank_label1.grid(row=1,column=0)
blank_label2.grid(row=1,column=1)
blank_label3.grid(row=1,column=2)

e1.grid(row=2,column=0)
e2.grid(row=2,column=1)
e3.grid(row=2,column=2)

blabel1.grid(row=3,column=0)
blabel2.grid(row=3,column=1)
blabel3.grid(row=3,column=2)

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)
b3.grid(row=4,column=2)



root.mainloop()