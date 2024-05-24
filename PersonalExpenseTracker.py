import sqlite3
import re #regex in python
from tabulate import tabulate
from datetime import datetime
import calendar

conn=sqlite3.connect('pet.db') #database used for project
cursor=conn.cursor() #allows queries to be made

def handleUserInput(field): #function that handles validation for the all the fields in the expenses table (field corresponds to position in table)
    if (field==0):
        prompt=str(input("\nPlease Enter The Title: "))
    elif (field==1):
        prompt=str(input("\nPlease Enter The Category:"))
    elif (field==2):
        prompt=str(input("\nPlease Enter The Date: "))
    else:
        prompt=int(input("\nPlease Enter The Expense Amount: "))
    
    if (field==0 or field==1): # if the field is expense name or category
        while (prompt=="" and re.search(r'\d',prompt)):
                prompt=str(input("\nPlease Enter Valid Data (characters only): "))
                if (len(prompt)>0 and prompt.isdigit()==False):
                    break
    elif (field==2): # if the field is a date
        valid=False
        while (valid==False):
                try:
                    datetime.strptime(prompt,'%d-%m-%y')
                    valid=True
                except:
                    prompt=str(input("\nPlease Enter An Appropriate Date: "))
                    valid=False
    else: # if the field is amount
         while (prompt=="" and re.search(r'\d',prompt)==False):
                prompt=str(input("\nPlease Enter Valid Data (digits only): "))
                if (len(prompt)>0 and prompt.isdigit()==False):
                    break
    return prompt

def handleAddExpense():
    print("ADDING AN EXPENSE")
    title=handleUserInput(0)
    category=handleUserInput(1)
    date=handleUserInput(2)
    expense=handleUserInput(3)

    try:
        cursor.execute("INSERT INTO expenses (title,category,date,amount) VALUES (?,?,?,?)",(title,category,date,expense))
        conn.commit() #this basically saves this query/action for this current connection and is the line that actually executes a query
        print("Expense Added To Database\n")
    except:
        print("ERROR\n")
    
def retrieveCurrentExpenses():
    print("CURRENT EXPENSES")
    cursor.execute("SELECT * FROM expenses")
    records=cursor.fetchall()
    return records

def handleDeleteExpense():
    print("DELETING AN EXPENSE")
    retrieveCurrentExpenses()
    id=str(input("Please Enter The ID Of The Expense To Be Deleted: "))
    try:
        cursor.execute("DELETE FROM expenses WHERE id=?",(id))
        conn.commit()
    except:
        print("ERROR: ID Does Not Exist")

def handleSummaryOfExpenses():
    records=retrieveCurrentExpenses()
    inputMonth=int(input("Please Enter A Month Number To Filter: "))
    dummyArray=[]
    if (inputMonth>0 and inputMonth<=12):
        print("EXPENSES FOR MONTH OF ",calendar.month_name[inputMonth])
        for j in range (0,len(records)):
            temp=datetime.strptime(records[j][3],'%d-%m-%y')
            if (temp.month==inputMonth):
                dummyArray.append(records[j])
                # print(tabulate(records[j],headers=["ID","Title","Category","Date","Amount"]))
                # print(tabulate(records,headers=["ID","Title","Category","Date","Amount"]))
            print(tabulate(dummyArray,headers=["ID","Title","Category","Date","Amount"]))
    else:
        

def handleUserSelection(option):
    if (option==1):
        handleAddExpense()
    elif (option==2):
        records=retrieveCurrentExpenses()
        print(tabulate(records,headers=["ID","Title","Category","Date","Amount"]))
    elif (option==3):
        handleDeleteExpense()
    else:
        handleSummaryOfExpenses()
    
def onLoad():
    print("\nOPTIONS AVAILABLE:\n1.Add Expense\n2.View Expenses\n3.Delete Expense\n4.Summary Of Expenses Per Month\n")
    try:
        option=int(input("Please Choose An Option: "))
        handleUserSelection(option)
    except:
        onLoad()

stop=0
while (stop==0):
    onLoad()

    
    
