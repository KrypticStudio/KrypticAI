### Kryptic Artificial Intelligence ###

# Local Libraries
from KAI import KAI_UserInfo

# Libraries

# Standard Libraries
import math
import re

# Function Definition

def userInput(usrInput):
    user_name = KAI_UserInfo.userName()
    birth = KAI_UserInfo.dateOfBirth()

    if usrInput[:11].lower() == "how are you":
        print("Im doing great!")
    if usrInput[:15].lower() == "what is my name":
        print("Your name is {}.".format(user_name[0]))
    
    if usrInput[:21].lower() == "what is my first name":
        print("Your fisrt name is {}.".format(user_name[1]))

    if usrInput[:22].lower() == "what is my middle name":
        print("Your middle name is {}.".format(user_name[2]))

    if usrInput[:20].lower() == "what is my last name":
        print("Your last name is {}.".format(user_name[3]))

    if usrInput[:13].lower() == "how tall am i":
        print("You are {}.".format(KAI_UserInfo.height()))

    if usrInput[:15].lower() == "when was i born":
        print("You were born on {}".format(birth[0]))

    if usrInput[:21].lower() == "what month was i born":
        print("You were born in {} ".format(birth[1]))
    
    if usrInput[:19].lower() == "what day was i born":
        day = str(birth[2])
        print("You were born on the {}".format(day))
    
    if usrInput[:20].lower() == "what year was i born":
        print("You were born in {}".format(birth[3]))




# Math
def maths(usrInput):
    addition = find(["add", "plus"])
    if addition in usrInput:

        usrInput.replace(addition, "+")

    print(eval(userInput))


