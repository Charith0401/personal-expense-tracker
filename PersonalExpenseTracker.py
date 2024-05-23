import tkinter as tk
import sqlite3
import re #regex in python
from tabulate import tabulate
from datetime import datetime

conn=sqlite3.connect('pet.db') #database used for project
cursor=conn.cursor() #allows queries to be made

def handleValidation(field): #function that handles validation for the all the fields in the expenses table (field corresponds to position in table)
    if (field==0):
        prompt=str(input("\nPlease Enter The Title: "))
    elif (field==1):
        prompt=str(input("\nPlease Enter The Category:"))
    elif (field==2):
        prompt=str(input("\nPlease Enter The Date: "))
    else:
        prompt=int(input("\nPlease Enter The Expense Amount: "))
    
    if (field!=2):
        while (prompt=="" and re.search(r'\d',prompt)):
                prompt=str(input("\nPlease Enter An Appropriate Title: "))
                if (len(prompt)>0 and prompt.isdigit()==False):
                    break
    else:
        valid=False
        while (valid==False):
                try:
                    datetime.strptime(prompt,'%d-%m-%y')
                    valid=True
                except:
                    prompt=str(input("\nPlease Enter An Appropriate Date: "))
                    valid=False
    return prompt

def handleAddExpense():
    # label.config(text="Expense Added")
    print("========Adding An Expense========")
    title=handleValidation(0)
    category=handleValidation(1)
    date=handleValidation(2)
    expense=handleValidation(3)

    try:
        cursor.execute("INSERT INTO expenses (title,category,date,amount) VALUES (?,?,?,?)",(title,category,date,expense))
        conn.commit() #this basically saves this query/action for this current connection and is the line that actually executes a query
        print("Expense Added To Database\n")
    except:
        print("ERROR\n")
    
def handleViewExpenses():
    cursor.execute("SELECT * FROM expenses")
    records=cursor.fetchall()
    print(tabulate(records,headers=["ID","Title","Category","Date","Amount"]))
    # for i in range(0,len(records)):
    #     print(tabulate(records[i]))

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
    # root.title("Personal Expense Tracker")
    # root.geometry("1200x800")

    # label=tk.Label(root,text="Current Expenses")
    # label.pack()

    # button=tk.Button(root,text="Add An Expense",command=handleAddExpense)
    # button.pack()
    print("\nOPTIONS AVAILABLE:\n1.Add Expense\n2.View Expenses\n3.Delete Expense\n4.Summary Of Expenses Per Month\n")
    try:
        option=int(input("Please Choose An Option: "))
        handleUserSelection(option)
    except:
        onLoad()
    # return label

# root=tk.Tk()
stop=0
while (stop==0):
    onLoad()
# root.mainloop()
    
    
