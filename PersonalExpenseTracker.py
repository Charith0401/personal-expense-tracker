import tkinter as tk

root=tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("1200x800")

label=tk.Label(root,text="Current Expenses")
label.pack()

def handleAddExpense():
    label.config(text="Expense Addedfdf")

button=tk.Button(root,text="Add An Expense",command=handleAddExpense)
button.pack()

root.mainloop()
def launch():
    pass
    
