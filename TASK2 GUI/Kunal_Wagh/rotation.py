# import necessary modules
from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk

 
root = Tk()
root.title("Gesture Detection Application")
root.geometry("400x320") # set starting size of window
# root.maxsize(400, 320) # width x height
# root.config(bg="#6FAFE7") # set background color of root window
 
Heading = Label(root, text="Demonstrator Application2", bg="#2176C1", fg='white', relief=RAISED)
Heading.pack(ipady=5, fill='x')
Heading.config(font=("Font", 20)) # change font and size of label
   

image = Image.open("plane_side_no-bg.png")
# width, height = image.size
# image.thumbnail((width/5, height/5))
photoimage = ImageTk.PhotoImage(image)
image_label = Label(root, image=photoimage, bg="white", relief=SUNKEN)
image_label.image = photoimage
image_label.pack(pady=5)

def rotate_image(degrees):
    new_image = image.rotate(-int(degrees))
    photoimage = ImageTk.PhotoImage(new_image)
    image_label.image = photoimage #Prevent garbage collection
    image_label.config(image = photoimage)
    

w2 = Scale(root, from_=0, to=360, tickinterval= 30, orient=HORIZONTAL, length=300, command = rotate_image)
w2.set(360)
w2.pack()
w2.set(0)
                                                                                            
root.mainloop()
