import math
import tkinter as tk    
root= tk.Tk()
greeting=tk.Label(
        text='Name')
        #bg= 'black', #bg= background
        #fg= 'white') #fg= forground
entry=tk.Entry(root)
greeting.pack()
entry.pack()
name=entry.get()
print(name)
root.mainloop()
print(name)