#import the csv module so that we may read the csv file
import csv

#open the csv file and pass it the variable 'election'
with open("/Users/aliny/Desktop/python-challenge/PyPoll/election_data.csv", "r") as election:
    #initialize the varibale that we will use to read and loop throught the csv file
    csv_reader = csv.reader(election)

    #initialize the variable that will store the number of votes
    numVotes = 0
    #initialize the list that will store the list of candidates
    candidates = []
    #initialize the varibale that we will use to store the amount of Khan votes
    khanVotes = 0
    #initialize the variable that we will use to store the amount of Correy votes
    correyVotes = 0
    #initialize the varible that we will use to store the amount of Li votes
    liVotes = 0
    #initialize the variable that we will use to store the amount of O'tooley votes
    otooleyVotes = 0
    csv_lines = []

    #skip the header in the csv file
    next(csv_reader)

    #initialize the for loop that we will use to loop through the lines in the csv file
    for line in csv_reader:
        #for every line in the csv file, add 1 to the total number of votes
        numVotes +=1
        #append the names of the candidates to the list 'candidates'
        candidates.append(line[2])
        #if line[2] is Khan, add 1 to the total number of Khan votes
        if line[2] ==  "Khan":
            khanVotes += 1
        #if line[2] is Correy, add 1 to the total number of Correy votes
        if line[2] ==  "Correy":
            correyVotes += 1
        #if line[2] is Li, add 1 to the total number of Li votes
        if line[2] ==  "Li":
            liVotes += 1
        #if line[2] is O'Tooley, add 1 to the total number of O'Tooley votes
        if line[2] ==  "O'Tooley":
            otooleyVotes += 1
        
    #print the total number of votes
    print("Total Votes :", numVotes)
    #set() allows me to print a filter out the repititions in a list 
    #print(sorted(set(candidates)))
    #print the total number of Khan votes along with the percentage of his votes
    print("Khan: " + "{0:.0%}".format(khanVotes/numVotes) + " (" + str(khanVotes) + ")")
    #print the total number of Correy votes along with the percentage of his votes
    print("Correy: " + "{0:.0%}".format(correyVotes/numVotes) + " (" + str(correyVotes) + ")")
    #print the total number of Li votes along with the percentage of his votes
    print("Li: " + "{0:.0%}".format(liVotes/numVotes) + " (" + str(liVotes) + ")")
    #print the total number of O'Tooley votes along with the percentage of his votes
    print("O'Tooley: " + "{0:.0%}".format(otooleyVotes/numVotes) + " (" + str(otooleyVotes) + ")")