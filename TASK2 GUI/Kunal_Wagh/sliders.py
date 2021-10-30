from tkinter import*
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title("Slider tutorial")
def getdollar():
    tmsg.showinfo("Amount Credited!",f"We have creadited{myslider1.get()}dollars to your acc")
myslider = Scale(root,from_=0, to=100)
myslider.pack()

myslider1 = Scale(root,from_=0, to=100,orient=HORIZONTAL)
myslider1.pack()

Button(root,text="get dollars!",command=getdollar).pack()
root.mainloop()