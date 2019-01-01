### Kryptic Artificial Intelligence ###

# Local Libraries

# Libraries
import time
# Standard Libraries

# Function Definition
def greeting(usrName):

    localtime = time.asctime( time.localtime(time.time()) )
    #print ("Local current time :", localtime[10:13])
    hourStr = localtime[10:13]
    hour = int(hourStr)
    timeOfDay = ["morning", "afternoon", "everning"]
    # Morning
    if hour > 00 and hour < 12:
        print("Good {} {}!".format(timeOfDay[0] ,usrName))
    # Afternoon
    if hour > 11 and hour < 17:
        print("Good {} {}!".format(timeOfDay[1] ,usrName))
    # Evening
    if hour > 14 and hour <= 23:
        print("Good {} {}!".format(timeOfDay[2], usrName))

    print("\nWhat may i help you with today?")