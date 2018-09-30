##PyPoll
#######################################################################################################
##                                                                                                   ##                                                                                          
## 8 888888888o   `8.`8888.      ,8' 8 888888888o       ,o888888o.     8 8888         8 8888         ## 
## 8 8888    `88.  `8.`8888.    ,8'  8 8888    `88.  . 8888     `88.   8 8888         8 8888         ##
## 8 8888     `88   `8.`8888.  ,8'   8 8888     `88 ,8 8888       `8b  8 8888         8 8888         ##
## 8 8888     ,88    `8.`8888.,8'    8 8888     ,88 88 8888        `8b 8 8888         8 8888         ##
## 8 8888.   ,88'     `8.`88888'     8 8888.   ,88' 88 8888         88 8 8888         8 8888         ##
## 8 888888888P'       `8. 8888      8 888888888P'  88 8888         88 8 8888         8 8888         ##
## 8 8888               `8 8888      8 8888         88 8888        ,8P 8 8888         8 8888         ##
## 8 8888                8 8888      8 8888         `8 8888       ,8P  8 8888         8 8888         ##
## 8 8888                8 8888      8 8888          ` 8888     ,88'   8 8888         8 8888         ##
## 8 8888                8 8888      8 8888             `8888888P'     8 888888888888 8 888888888888 ##
##                                                                                                   ##
#######################################################################################################
##                                                                                                   ##
## This script summarizes election_data.csv to calculates the following:                             ##
##  -The total number of votes cast                                                                  ##
##  -A complete list of candidates who received votes                                                ##
##  -The percentage of votes each candidate won                                                      ##
##  -The total number of votes each candidate won                                                    ##
##  -The winner of the election based on popular vote                                                ##
##                                                                                                   ## 
##  Results will be printed to the terminal as well as Results.txt                                   ##
##                                                                                                   ##                                                                                                       
#######################################################################################################
## IMPORT OS AND CSV MODULES                                                                         ##
#######################################################################################################
import os
import csv

#######################################################################################################
## SET FILE PATHS                                                                                    ##
#######################################################################################################
## INPUT
pollcsv = os.path.join('election_data.csv')
 
## OUTPUT
resultstxt = os.path.join('results.txt')
 
#######################################################################################################
## SET ARRAYS AND DEFAULT VARIABLE VALUES                                                            ##
#######################################################################################################
## START ARRAY TO STORE CANDIDATE NAMES 
candidates = []
## START ARRAY TO STORE TOTAL VOTES PER CANDIDATE
v_summary = []

## SET VOTE COUNTS TO START AT 0
votes = 0
 
#######################################################################################################
## DEFINE DEMOCRACY FUNCTION TO ASSIGN NAMES AND VOTES TO APPROPRIATE ARRAY                          ##
#######################################################################################################
def democracy(vote):
    # ADD NEW CANDIDATE TO CANDIDATES ARRAY
    candidate = vote[2]
    if candidate not in candidates:
        candidates.append(candidate)
        # ADD A CORRESPONDING BUCKET IN THE VOTE SUMMARY ARRAY TO STORE VOTES PER CANDIDATE
        v_summary.append(0)

    # ADD VOTE TO CANDIDATE'S INDEX ON THE VOTE SUMMARY ARRAY
    v_summary[candidates.index(candidate)] = (int(v_summary[candidates.index(candidate)]) + 1)
 
## READ INPUT FILE
with open(pollcsv, 'r') as csvfile:

    # USE READER TO DELIMIT FILE CONTENTS BASED ON COMMA
    csvreader = csv.reader(csvfile, delimiter=',')
    # SKIP HEADER
    header = next(csvreader)

    # LOOP FUNCTION FOR EACH ROW
    for row in csvreader:
        democracy(row)
        votes = (votes + 1)
 
#######################################################################################################
## PREPARE FINAL ANALYSIS VALUES FOR PRINTING                                                        ##
#######################################################################################################
## ZIP LISTS AND FIND CANDIDATE WITH THE MOST VOTES
results = dict(zip(candidates, v_summary))
winner = list(results.keys())[list(results.values()).index(max(v_summary))]
 
#######################################################################################################
##  PRINT RESULTS TO TERMINAL                                                                        ##
#######################################################################################################
print("Election Results")
print("-------------------------")
print(f"Total Votes: {int(votes)}")
print("-------------------------")
for candidate in range(len(candidates)):
    cand_name = str(candidates[candidate])
    cand_v_pct = float((v_summary[candidate]/votes))*100
    cand_votes = int(v_summary[candidate])
    print(f"{cand_name}: {cand_v_pct:.3f}%  ({str(cand_votes)})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
 
#######################################################################################################
##  PRINT RESULTS TO OUTPUT                                                                          ##
#######################################################################################################
with open(resultstxt, 'w') as text_file:
    text_file.write("Election Results"+ '\n')
    text_file.write("-------------------------"+ '\n')
    text_file.write(f"Total Votes: {int(votes)}"+ '\n')
    text_file.write("-------------------------"+ '\n')
    for candidate in range(len(candidates)):
        cand_name = str(candidates[candidate]) 
        cand_v_pct = float((v_summary[candidate]/votes))*100
        cand_votes = int(v_summary[candidate])
        text_file.write(f"{cand_name}: {cand_v_pct:.3f}%  ({str(cand_votes)})"+ '\n')
    text_file.write("-------------------------"+ '\n')
    text_file.write(f"Winner: {winner}"+ '\n')
    text_file.write("-------------------------"+ '\n')

