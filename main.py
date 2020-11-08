import pyttsx3
import os
import random
from datetime import datetime
import webbrowser

def speak(sp):
    engine=pyttsx3.init()
    engine.say(sp)
    print(sp)
    engine.runAndWait()


speak("hi iam a chatbot you can chat with me please enter your name")
user_name=input("enter your name:")


file_size=os.path.getsize("name.txt")

if file_size == 0:
    user_name_file=open("name.txt",'w')
    user_name_file.write(user_name)
    speak("i will remember next time thank you")
    user_name_file.close()
else:
    user_name_file = open("name.txt",'r')
    user_name_file.read()
    print(user_name_file)
    user_name_file.close()

while True:
    main = input("you:")

    a1=["hi","hello","hey"]
    a2=["time","current time"]
    a3=["google",]
    a4=["add"]

    if main in a1:
        rand=random.choice(a1)
        speak(rand)
    elif main in a2:
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        speak("the time is") or speak(current_time)

    elif main in a3:
        get=webbrowser.open("www.google.com",new=2)
    elif main in a4:
        first_number=input("enter first number:")
        second_number=input("enter second number:")
        result= float(first_number)+ float(second_number)
        speak(result)





