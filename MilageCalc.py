# Milage Calculator
# Start Date: 04/25/2024
# Modified Date: 04/28/2024

from datetime import datetime

goalPlace = ""
startPlace = ""
endPlace = ""
startMilage = 0
endMilage = 0
total = 0

print("")
print("======================")
print("Milage Calculator")
print("By: Dan Uff")
print("Version 1.0")
print("")
print("(c) 2024 CPS CO.")
print("======================")
print("https://www.cpsoft.us/")
print("======================")
print("")
goalPlace = input("Where are you going :")
startPlace = input("Where did you START :")
endPlace = input("Where you STOP :")
startMiliage = input("STARTING Milage :")
endMilage = input("ENDING Milage :")
showDat = datetime.now()

total = (int(startMiliage) + int(endMilage))

print("===================================================")
print("You started from: ",str(startPlace))
print("You're going to: ",str(endPlace))
print("Starting Milage : ",int(startMiliage))
print("Ending Milage : ",int(endMilage))
print("")
print("You drove a total of ",int(total),"miles today.")
print("===================================================")
print("")
print("*** END OF INFORMATION ***")
print("")
print("Information as of:",showDat)
