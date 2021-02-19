"""Research Question #1: Can we predict how long till we have to send a maintence worker to a site to repair a Gate

Data:
X:
- Product number ( Electric Gate: PID: 122 )
- Date and time it was last repaired
- Date and time it was last checked
- How often do they use this door, how many times have they used it in a day
- Temperature of the day (days high and low), humidity
- Temperature of the machine (high and low)

Y:
- # of days til it needs to be checked or the probability it needs to be checked within the month
"""
#import some libraries
#sklearn linear model, polymodel
import random

#generate some data
#[unit number,pid, temp of day, temp of machine]
#[220,2,38, 40, 21]
x = []
y = []
amountOfData = 1000
for gateNumber in range(amountOfData):
  row = []
  gateType = random.randint(1,3)
  row.append(gateNumber)
  row.append(gateType)
  tempDay = random.randint(-1,40)
  row.append(tempDay)
  tempMachine = random.randint(tempDay-5, tempDay + 5)
  row.append(tempMachine)
  diff = abs(tempMachine - tempDay)
  numDays = random.randint(diff-3, diff+3)
  
  x.append(row)
  y.append(numDays)


#make the model, check how accurate it is