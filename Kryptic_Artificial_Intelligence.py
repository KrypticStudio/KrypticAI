### Kryptic Artificial Intelligence ###

# Local Libraries
from KAI import KAI_Name
from KAI import KAI_Greet
from KAI import KAI_UserInfo
from KAI import KAI_User_Input

# Libraries
import speech_recognition as sr
# Standard Libraries
import sys
# Function Definition


# Main Function
def main():
    r = sr.Recognizer()
    program_Name = "Kryptic Artificial Intelligence\n\n"
    User_Name = KAI_UserInfo.userName()
    usrName = User_Name[0].split()
    KAI_Name.programName(program_Name)
    KAI_Greet.greeting(usrName[0])

    while True:
        #KAI_User_Input.userInput(input("   >>> "))
        #KAI_User_Input.maths(input("   >>> "))
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                KAI_User_Input.userInput(text)
            except:
                print("Sorry could not recognize what you said")

    

# Call to Main Function

main()