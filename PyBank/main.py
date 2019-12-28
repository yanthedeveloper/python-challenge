#import the csv module so that we can open the csv file 
import csv
#open the csv file using an absolute file path
with open("/Users/aliny/Desktop/python-challenge/PyBank/budget_data.csv", 'r') as budgetfile:
    #create a variable with .reader() that we will use to read the csv file
    csv_reader = csv.reader(budgetfile)

    with open('results_file.csv', 'w') as new_file:

        csv_writer = csv.writer(new_file)

        #initialize the variable that will store the value of all the profit/losses added up together
        total = 0
        #initialize the numMonths variable that will store the number of months in the csv file
        numMonths = 0
        #initialize the monthDifferences that we will use to store the differences in the profit/losses from month to month
        monthDifferences = 0
        #initialize the averageChange variable that we will use to calculate the average change in the profit/losses
        averageChange = 0
        #initialize the list changes that will store all the values of the profit/losses from month to month
        changes = []
        #initialize the monthList that will store all of the months 
        monthList = []

        #use next(csv_reader) so that we can skip the header and start at the next row in the csv file
        #which contains the first row with actual values
        next(csv_reader)

        #initialize a for loop that will loop through each line in the csv file
        for line in csv_reader:
            #for every line line the csv_reader, the number of months increases by 1
            numMonths +=1
            #total is calculated by adding all of the values in line[1] to each other
            total += int(line[1])
            #changes is filled with all of the values in line[1]
            changes.append(line[1])
            #monthList is filled with all of the values in line[0]
            monthList.append(line[0])

        #this is a for loop. the length of the for loop is the length of changes - 1
        #in this for loop we are calculating the differences between each month and we
        #are appending these value to newChanges
        #the reason that the length is -1 is because we know that since we are subtracting
        #the values from each other, we are going to have one less value than the actual number
        #of items in the list
        newChanges = [int(changes[i+1]) - int(changes[i]) for i in range(len(changes) -1)]

        #initialize the variable that we will use to add all the values in newChanges together
        totalNew = 0

        #initialize the for loop that we will use to loop throught newChanges and add 
        for x in newChanges:
            #totalNew is equal to all of the value in newChanges added together
            totalNew += int(x)

        #print the total that was calculated in the csv_reader for loop    
        csv_writer.writerow(["Total: ", total])
        #declare the formula for calculatind the average change
        averageChange = totalNew/len(newChanges)
        #print the average change
        print("Average Change: ", + averageChange)
        #print the total months
        print("Total Months: ", numMonths)
        #print the greatest increase in profits. to print these i will take the index of the maximum value of 
        #newChanges and add 1 to it in order to get the corresponding month from the month list
        print("Greatest Increase in Profits: " + monthList[newChanges.index(max(newChanges))+1], max(newChanges))
        #print the greatest decrease in profits. to print these i will take the index of the maximum value of 
        #newChanges and add 1 to it in order to get the corresponding month from the month list 
        print("Greatest Decrease in Profits: " + monthList[newChanges.index(min(newChanges))+1], min(newChanges))