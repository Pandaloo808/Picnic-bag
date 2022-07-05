from tkinter import *
import random

root=Tk()

root.title("Picnic Bag List")
root.geometry("300x200")
root.configure(bg="#6dbbbf")

items=["food","phone","Blanket","Drinks","Chocolates"]
print(items)

output=Label(root,text="Items: Food, Phone, Blanket, Drinks, Chocolates")
output.place(relx=0.5,rely=0.4,anchor=CENTER)

output=Label(root,bg="#6dbbbf",fg="green")

def thingy():
    bob=random.randint(0,4)
    chosen=items[bob]
    print(chosen)
    output["text"]=" You should put " + chosen + " in your bag"
    
btn=Button(root,text="Which Item to put in the bag?", command=thingy, bg="purple", fg="yellow")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
output.place(relx=0.5,rely=0.65,anchor=CENTER)

root.mainloop()