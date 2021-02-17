import math
import tkinter as tk    
def call(label,n):
    s=n.get()
    label.config(text='Number of inflows is '+s)
    return 
root= tk.Tk()
root.title("Mass Balance")
root.geometry('400x250')# This size can be changed if needed
n_inflows_txt= tk.Label(root,text= 'How many inflows?')
n_inflows_txt.grid(row=1)
n_inflows_ans= tk.Entry(root)
n_inflows_ans.grid(row=2)
Num_inflows= tk.Label(root)
Num_inflows.grid(row=7)
n_flow_input=tk.Button(root, text="Next", relief='raised',command=lambda:call(Num_inflows, n_inflows_ans))
n_flow_input.grid(row=3)
root.mainloop()