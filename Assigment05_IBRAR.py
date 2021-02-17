# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# IBRAR,02.16.2021,Added code to complete assignment
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstRow = [] # A list of rows to create dictionary
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # Capture the user option selection
strTask = "" # Capture task input from user
StrPriority = "" # Capture priority input from user
strRemove = "" # Capture task to remove from user
strMenu = """
Menu of Options
    1 - Show current data
    2 - Add a new task.
    3 - Remove an existing task.
    4 - Save Data to File
    5 - Exit Program
"""  # A menu of user options


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
taskFile = open(objFile, "r")
for row in taskFile:
    lstRow = row.split("|")  # Returns a list!
    dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
taskFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Below is the current list of tasks: \n")
        print("Task","|","Priority")
        for row in lstTable:
            print(row["Task"],"|",row["Priority"])
        print()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please enter a task: ")
        strPriority = input("Please assign a priority to the task [High, Medium or Low]: ")
        dicRow = {"Task": strTask.title(), "Priority": strPriority.title()}
        lstTable.append(dicRow)
        print("\nThe task, ",strTask.strip(), ", has been added to the table.\n", sep="")
        continue
    # Step 5 - Remove an item from the list/Table based on its name
    elif (strChoice.strip() == '3'):
        print("Here are the tasks currently in the table: ")
        print()
        for row in lstTable:
            print(row["Task"])
        strRemove = input("\nPlease enter the task that you would like to remove: ")
        countRemove = 0
        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():
                lstTable.remove(row)
                countRemove += 1
                print("\nThe task, ",strRemove.strip(), ", has been removed from the table.\n", sep="")
        if countRemove == 0:
            print("\nThe task, ",strRemove.strip(), ", is not one of the tasks in the table.\n", sep="")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        taskFile = open(objFile, "w")
        for row in lstTable:
            taskFile.write(row["Task"]+ "|" + row["Priority"] + "\n")
        taskFile.close()
        print("\n All tasks have been saved to the file.\n")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("\nThank you and GoodBye!")
        break  # and Exit the program
