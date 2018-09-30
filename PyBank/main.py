#PyBank
##########################################################################
##                                                                      ##
##     /$$$$$$$            /$$$$$$$                      /$$            ##
##    | $$__  $$          | $$__  $$                    | $$            ##
##    | $$  \ $$ /$$   /$$| $$  \ $$  /$$$$$$  /$$$$$$$ | $$   /$$      ##
##    | $$$$$$$/| $$  | $$| $$$$$$$  |____  $$| $$__  $$| $$  /$$/      ##
##    | $$____/ | $$  | $$| $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$/       ##
##    | $$      | $$  | $$| $$  \ $$ /$$__  $$| $$  | $$| $$_  $$       ##
##    | $$      |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$  | $$| $$ \  $$      ##
##    |__/       \____  $$|_______/  \_______/|__/  |__/|__/  \__/      ##
##               /$$  | $$                                              ##
##              |  $$$$$$/                                              ##
##               \______/                                               ##
##                                                                      ##
##########################################################################
##                                                                      ##
##  This Python script analyzes financial data from budget_data.csv.    ##
##                                                                      ##
##  Each of the following are calculated:                               ##
##  -Total number of months included in the dataset                     ##
##  -Total net amount of "Profit/Losses" over the entire period         ##
##  -Average change in "Profit/Losses" between months                   ##
##  -Date and amount for greatest increase in profits                   ##
##  -Date and amount for greatest decrease in losses                    ##
##                                                                      ##
##  Results will be printed to the terminal as well as Results.txt      ##
##                                                                      ##
##########################################################################
## IMPORT OS AND CSV MODULES                                            ##
##########################################################################
import os
import csv

##########################################################################
## SET FILE PATHS                                                       ##
##########################################################################
## INPUT
bankcsv = os.path.join('budget_data.csv')
 
## OUTPUT
resultstxt = os.path.join('results.txt')
 
##########################################################################
## SET ARRAYS AND DEFAULT VARIABLE VALUES                               ##
##########################################################################
## START ARRAY TO STORE MONTHS 
months = []
## START ARRAY TO STORE MONTHLY CHANGES
changes = []
PLs = []
## SET PROFIT/LOSS TO START AT 0
pl = 0
## SET TOTAL TO START AT 0
total = 0
 
##########################################################################
## DEFINE MYLEDGER FUNCTION FOR CAPTURING MONTHS & CHANGES              ##
##########################################################################
def myledger(record):
    # ADD MONTH TO MONTHS ARRAY
    months.append(record[0])
    # CAPTURE MONTHLY CHANGE IN P/L AS COMPARED TO PREVIOUS MONTH
    if pl == 0:
        change = 0  # IF THERE'S NOT PREVIOUS MONTH, DEFAULT CHANGE TO 0
    else:
        change = int(record[1]) - int(pl)
    # ADD CHANGE AMOUNT TO CHANGES ARRAY
    changes.append(change)
 
## READ INPUT FILE
with open(bankcsv, 'r') as csvfile:

    # USE READER TO DELIMIT FILE CONTENTS BASED ON COMMA
    csvreader = csv.reader(csvfile, delimiter=',')
    # SKIP HEADER
    header = next(csvreader)

    # LOOP FUNCTION FOR EACH ROW
    for row in csvreader:
        myledger(row)
        total = int(total + int(row[1]))
        pl = int(row[1])
 
##########################################################################
## PREPARE FINAL ANALYSIS VALUES FOR PRINTING                           ##
##########################################################################
## CALCULATE AVERAGE MONTHLY P/L CHANGE
avgchange = round(float((sum(changes)/(len(changes)-1))),2)
## COUNT THE NUMBER OF MONTHS IN THE MONTHS ARRAY
month_count = int(len(months))
## RETURN THE GREATEST INCREASE IN PROFITS ON THE CHANGES ARRAY
GInc = max(changes)
## FIND THE GREATEST DECREASE IN LOSSES ON THE CHANGES ARRAY
GDec = min(changes)
 
##########################################################################
##  PRINT RESULTS TO TERMINAL                                           ##
##########################################################################
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average  Change: ${avgchange}")
print(f"Greatest Increase in Profits: {months[changes.index(GInc)]} (${GInc})")
print(f"Greatest Decrease in Profits: {months[changes.index(GDec)]} (${GDec})")
 
##########################################################################
##  PRINT RESULTS TO OUTPUT                                             ##
##########################################################################
with open(resultstxt, 'w') as text_file:
    text_file.write("Financial Analysis"+ '\n')
    text_file.write("----------------------------"+ '\n')
    text_file.write(f"Total Months: {month_count}"+ '\n')
    text_file.write(f"Total: ${total}"+ '\n')
    text_file.write(f"Average  Change: ${avgchange}"+ '\n')
    text_file.write(f"Greatest Increase in Profits: {months[changes.index(GInc)]} (${GInc})"+ '\n')
    text_file.write(f"Greatest Decrease in Profits: {months[changes.index(GDec)]} (${GDec})"+ '\n')
    
