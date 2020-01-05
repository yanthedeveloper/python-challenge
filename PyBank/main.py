import os
#import the csv module so that we may open and read the csv file
import csv
import sys
#sys.stdout = open('truFile.txt', 'a+')
#os.system("notepad.exe truFile.txt")
#os.system("notepad.exe diff.txt")
#open the csv file and pass to it the variable 'budgetfile'
with open("/Users/aliny/Desktop/python-challenge/PyBank/budget_data.csv", 'r') as budgetfile:
    
    #initialize the varible that we will use to loop through and read the csv file
    csv_reader = csv.reader(budgetfile)
    
    #initialize that variable that we will use to store the total of the profit/losses
    total = 0
    #number of months
    numMonths = 0
    #month to month differences
    monthDifferences = 0
    #average change between the months
    averageChange = 0
    #list of the changes between the months
    changes = []
    #list of months
    monthList = []
    #list for the header row 
    header = []
    #skip the header
    next(csv_reader)

    #looping through the csv file
    for line in csv_reader:
        #header.append(csv_reader[line])
        #for every line add 1 to the number of months
        numMonths +=1
        #add up the total 
        total += int(line[1])
        #append the values to the changes list
        changes.append(line[1])
        #append the months to the month list
        monthList.append(line[0])

    #append the values of the month to month differences to the list 'newChanges'
    newChanges = [int(changes[i+1]) - int(changes[i]) for i in range(len(changes) -1)]

    #total of the month to month differences
    totalNew = 0

    #loop through the newChanges list
    for x in newChanges:
        #add up the total of the differences
        totalNew += int(x)
  
    print(header)
    #print the original total
    print("Total: ", total)
    #define the formula for average change
    averageChange = round(totalNew/len(newChanges), 2)
    #print the average change
    print("Average Change: ", averageChange)
    #print the total number of months
    print("Total Months: ", numMonths)
    #print the greatest increase in profits
    print("Greatest Increase in Profits: " + monthList[newChanges.index(max(newChanges))+1], max(newChanges))
    #print the greatest decrease in profits
    print("Greatest Decrease in Profits: " + monthList[newChanges.index(min(newChanges))+1], min(newChanges))
    
    #create a new file that we will use to print the answers to
    file = open('GT.txt', 'w+')
    #direct the output of the following lines to that file
    sys.stdout = file

    print(header)
    #print the original total
    print("Total: ", total)
    #define the formula for average change
    averageChange = round(totalNew/len(newChanges), 2)
    #print the average change
    print("Average Change: ", averageChange)
    #print the total number of months
    print("Total Months: ", numMonths)
    #print the greatest increase in profits
    print("Greatest Increase in Profits: " + monthList[newChanges.index(max(newChanges))+1], max(newChanges))
    #print the greatest decrease in profits
    print("Greatest Decrease in Profits: " + monthList[newChanges.index(min(newChanges))+1], min(newChanges))
    #open the final text file

    #close the file object
    file.close()

    #open our new file
    os.system("notepad.exe GT.txt")