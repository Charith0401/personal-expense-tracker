import sqlite3
import re #regex in python
from tabulate import tabulate
from datetime import datetime
import calendar

conn=sqlite3.connect('pet.db') #database used for project
cursor=conn.cursor() #allows queries to be made

def handleUserInput(field): #function that handles validation for the all the fields in the expenses table (field corresponds to position in table)
    if (field==0):
        prompt=str(input("\nPlease Enter The Expense Name: "))
    elif (field==1):
        prompt=str(input("\nPlease Enter The Category:"))
    elif (field==2):
        prompt=str(input("\nPlease Enter The Date (dd-mm-yy): "))
    else:
        prompt=str(input("\nPlease Enter The Expense Amount: "))
    
    if (field==0 or field==1): # if the field is expense name or category
        while (not len(prompt)>0 and re.search(r'\d',prompt)):
                prompt=str(input("\nPlease Enter Valid Data (characters only): "))
                if (len(prompt)>0 and prompt.isdigit()==False):
                    break
    if (field==2): # if the field is a date
        valid=False
        while (valid==False):
                try:
                    datetime.strptime(prompt,'%d-%m-%y')
                    valid=True
                except:
                    prompt=str(input("\nPlease Enter An Appropriate Date (dd-mm-yy): "))
                    valid=False
                    
    if (field==3): # if the field is amount
            valid=False
            while (valid==False):
                try:
                    while (int(prompt)<0):
                            prompt=str(input("\nPlease Enter Valid Data (digits only): "))
                            if (int(prompt)>0):
                                valid=True
                                break
                except:
                    print("ERROR")

            
    return prompt

def handleAddExpense(): # function called when user wants to add an expense
    #function called depending on field position in expenses table
    title=handleUserInput(0)
    category=handleUserInput(1)
    date=handleUserInput(2)
    expense=handleUserInput(3)

    try:
        cursor.execute("INSERT INTO expenses (title,category,date,amount) VALUES (?,?,?,?)",(title,category,date,expense))
        conn.commit() #this saves this query/action for this current connection and is the line that actually executes a query
        print("Expense Added To Database\n")
    except:
        print("ERROR\n")
    
def retrieveCurrentExpenses():
    print("CURRENT EXPENSES")
    cursor.execute("SELECT * FROM expenses")
    records=cursor.fetchall()

    tabulateArray=[]
    for i in range (0,len(records)):
        tabulateArray.append(records[i])
    return records,tabulateArray

def handleDeleteExpense():
    records,tabulateArray=retrieveCurrentExpenses()
    if (len(records)>0):
        print(tabulate(tabulateArray,headers=["ID","Expense","Category","Date","Amount"]))
        id=str(input("\nPlease Enter The ID Of The Expense To Be Deleted: "))
        try:
            cursor.execute("DELETE FROM expenses WHERE id=?",(id))
            conn.commit()
            print("Successfully Deleted Expense")
        except:
            print("ERROR: ID Does Not Exist")
    else:
        print("No Expenses In Database")
        
def handleSummaryOfExpenses():
    dummyArray=[]
    totalExpenses=0
    records,tabulateArray=retrieveCurrentExpenses()
    if (len(records)>0):
        inputMonth=int(input("Please Enter A Month Number To Filter: "))
        while (not inputMonth or inputMonth<0 or inputMonth>12):
            inputMonth=int(input("Please Enter A Month Between 1 and 12: "))

        print("\nSUMMARY OF EXPENSES FOR MONTH OF",calendar.month_name[inputMonth])
        for j in range (0,len(records)):
            temp=datetime.strptime(records[j][3],'%d-%m-%y')
            if (temp.month==inputMonth):
                dummyArray.append(records[j])
                totalExpenses+=int(records[j][4])
        print(tabulate(dummyArray,headers=["ID","Title","Category","Date","Amount"]))
        print("TOTAL EXPENSES: ",totalExpenses)
    else:
        print("No Expenses In Database")

def handleUserSelection(option):
    if (option==1):
        handleAddExpense()
    elif (option==2):
        records,tabulateArray=retrieveCurrentExpenses()
        if (len(records)>0):
            print(tabulate(records,headers=["ID","Title","Category","Date","Amount"]))
        else:
            print("No Expenses In Database")
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

    
    
