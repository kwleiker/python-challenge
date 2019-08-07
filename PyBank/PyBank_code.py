# kWalter 
# Memento Mori

import os
import csv

file = 'pybank_data.csv'
with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csv_header = next(csvfile)

    # definitions 
    kmonth = 0 
    net = 0 
    change = 0 
    lastmonth = 0 
    sumchange = 0 
    maxgain = 0
    maxloss = 0 


    for row in csvreader:
        # front load bin  
        change = int(row[1]) - lastmonth 

        # conditional 1
        if change > maxgain: 
            maxgain = change
            maxgainmonth = row[0]
        else: 
            maxgain = maxgain
        # endif

        # conditional 2 
        if change < maxloss:
            maxloss = change 
            maxlossmonth = row[0]
        else:
            maxloss = maxloss
        # endif

        # end cycle counters 
        kmonth = kmonth + 1 
        sumchange = sumchange + change 
        net = net + int(row[1])
        
        # rear load bin
        lastmonth = int(row[1])
        
# It feels tacky coding "firstmonth" as a number rather than a variable.
averagechange = ((sumchange - 867884) / (kmonth - 1))

# outputs
print("This is not a financial analysis.")
print("_____________________")
print("Total Months:  " + str(kmonth))
print("Net Income:  $" + str(net)) 
print("Average Change:  $" + str(round(averagechange,2)))
print("Greatest Increase in Profits:  $" + str(maxgain) + " in " + str(maxgainmonth))
print("Greatest Decrease in Profits:  $" + str(maxloss) + " in " + str(maxlossmonth))
