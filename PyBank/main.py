#PyBank
##In this challenge, you are tasked with creating a Python script for analyzing
##the financial records of your company. You will give a set of financial data
##called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses.
##Your task is to create a Python script that analyzes the records to calculate each of the following:
    ##The total number of months included in the dataset
    ##The total net amount of "Profit/Losses" over the entire period
    ##The average change in "Profit/Losses" between months over the entire period
    ##The greatest increase in profits (date and amount) over the entire period
    ##The greatest decrease in losses (date and amount) over the entire period

##As an example, your analysis should look similar to the one below:
    ##Financial Analysis
    ##----------------------------
    ##Total Months: 86
    ##Total: $38382578
    ##Average  Change: $-2315.12
    ##Greatest Increase in Profits: Feb-2012 ($1926159)
    ##Greatest Decrease in Profits: Sep-2013 ($-2196167)

##In addition, your final script should both
    ##print the analysis to the terminal and
    ##export a text file with the results.

#import os and csv modules
import os
import csv

#set file path
#input
bankcsv = os.path.join('budget_data.csv')

#output
resultstxt = os.path.join('results.txt')

#start array to store months
months = []
#set array to store monthly changes
changes = []
#set starting ledger balance to 0
pl = 0
#set total
total = 0

#define function for calculating bankcsv results
def myledger(record):
    #add month to months array
    months.append(record[0])
    #capture change in P/L as compared to previous month
    if pl == 0:
        change = 0  #if no prev month, then 0
    else:
        change = int(record[1]) - int(pl)
    #add amount to changes array
    changes.append(change)

#read in the selected file
with open(bankcsv, 'r') as csvfile:

    #delimit file contents based on comma
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    header = next(csvreader)

    #loop for each row
    for row in csvreader:
        myledger(row)
        total = int(total + int(row[1]))
        pl = int(row[1])

#calculate average monthly P/L change
avgchange = round(float((sum(changes)/(len(changes)-1))),2)
#count the number of months in the months array
month_count = int(len(months))
#find greatest increase in profits on the changes array
GInc = max(changes)
#find greatest decrease in losses on the changes array
GDec = min(changes)

#print to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average  Change: ${avgchange}")
print(f"Greatest Increase in Profits: {months[changes.index(GInc)]} (${GInc})")
print(f"Greatest Decrease in Profits: {months[changes.index(GDec)]} (${GDec})")

#print to text file
with open(resultstxt, 'w') as text_file:
    text_file.write("Financial Analysis"+ '\n')
    text_file.write("----------------------------"+ '\n')
    text_file.write(f"Total Months: {month_count}"+ '\n')
    text_file.write(f"Total: ${total}"+ '\n')
    text_file.write(f"Average  Change: ${avgchange}"+ '\n')
    text_file.write(f"Greatest Increase in Profits: {months[changes.index(GInc)]} (${GInc})"+ '\n')
    text_file.write(f"Greatest Decrease in Profits: {months[changes.index(GDec)]} (${GDec})"+ '\n')
    
