import tkinter as tk

# class Expenses:
#     def __init__(self,title,category,date,amount):
#         self.title=title
#         self.category=category
#         self.date=date
#         self.amount=amount

#     def setTitle(self,title):
#         self.title=title
    
#     def setCategory(self,category):
#         self.category=category
    
#     def setDate(self,date):
#         self.date=date
    
#     def setAmount(self,amount):
#         self.amount=amount
    
#     def getTitle(self):
#         print("Title of Expense is ",self.title)
    
#     def getCategory(self):
#         print("Category is",self.category)

#     def getDate(self):
#         print("Title of Expense is ",self.date)

#     def getAmount(self):
#         print("Title of Expense is ",self.amount)


def handleAddExpense():
    label.config(text="Expense Addedfdf")
    print("========Adding An Expense========")
    title=str(input("\nPlease Enter The Title: "))
    category=str(input("\nPlease Enter The Category:"))
    category=str(input("\nPlease Enter The Date: "))
    expense=str(input("\nPlease Enter The Expense Amount: "))


    
def handleViewExpenses():
    pass

def handleDeleteExpense():
    pass

def handleSummaryOfExpenses():
    pass


def handleUserSelection(option):
    if (option==1):
        handleAddExpense()
    elif (option==2):
        handleViewExpenses()
    elif (option==3):
        handleDeleteExpense()
    else:
        handleSummaryOfExpenses()
    
def onLoad():
    root.title("Personal Expense Tracker")
    root.geometry("1200x800")

    label=tk.Label(root,text="Current Expenses")
    label.pack()

    button=tk.Button(root,text="Add An Expense",command=handleAddExpense)
    button.pack()
    print("OPTIONS AVAILABLE:\n1.Add Expense\n2.View Expenses\n3.Delete Expense\n4.Summary Of Expenses Per Month")
    option=int(input())
    handleUserSelection(option)
    print(option)
    return label

root=tk.Tk()
label=onLoad()
root.mainloop()
    
    
