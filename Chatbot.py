#!/usr/bin/env python
# coding: utf-8


import math
import random
import webbrowser
import multiprocessing
import sys
import playsound


college = "Dr Dy Patil Institute of Management and Research"
mood = "Smiley"
name = "Friday"
hello = "Hello"
teachers = [
    "Sandhya Mam",
    "Mily Mam",
    "Prateek Sir",
    "Naleeni Mam",
    "Pooja Mam"
]


resp = {
    "what's your name?" : [
        "They call me {0}".format(name),
        "I usually go by {0}".format(name), 
        "My name is the {0}".format(name)
        ],
    "How is your mood" : [
        "My mood is {0}".format(mood),
        "I'm feeling {0}".format(mood)
    ],
    "What is our college name" : [
        "Our college name is {0}".format(college),
        "Our College name is {0}".format(college),
        
    ],
    "how are you?": [
      "I am Great! I must ask, How are you? "  
    ],
    "List our faculty members": [
            "Our Faculty members are {0}".format(teachers)
    ],
    "hi" : [
        "Hello there! How can I help you?"
    ],
    "Open Instagram":[
        "Opening Instagram"
    ],
    "Open Twitter":[
        "Opening Twitter"
    ],
    "Open Whatsapp":[
        "Opening Whatsapp"
    ],
   "Play Music":[
        "Playing faded by Alan Walker, press q to Stop music"
    ],
    "greetings":[
        "I am happy to hear that! "
    ],
    'q':[
        "Thankyou for Playing"
    ],
    "default":[
        "This is a default message"
    ]
    
}

    


    
def res(message):
    if message in resp:
        return_message = random.choice(resp[message])
    else:
        return_message = random.choice(resp["default"])
    return return_message
        
def real(xtext):
    if "name" in xtext: 
        ytext = "what's your name?"
    elif "monsoon" in xtext: 
            ytext = "what's today's weather?"
    elif "mood" in xtext: 
            ytext = "How is your mood"
    elif "how are" in xtext: 
            ytext = "how are you?"
    elif "college" in xtext:
            ytext="What is our college name"
    elif "teacher" in xtext:
            ytext="List our faculty members"
    elif "instagram" in xtext:
            ytext="Open Instagram"
            webbrowser.open("https://www.instagram.com/")
    elif "twitter" in xtext:
            ytext="Open Twitter"
            webbrowser.open("https://www.twitter.com/")
    elif "whatsapp" in xtext:
            ytext="Open Whatsapp"
            webbrowser.open("https://web.whatsapp.com/")
    elif "music" in xtext:
            p = multiprocessing.Process(target=playsound, args=("abc.mp3",))
            p.start()
            T2.delete("1.0", "end")
            T1.insert(1.0, "Playing faded by Alan Walker, press q to Stop music" + '\n')
            ytext = "Play Music"
    elif "hi" in xtext:
            ytext = "hi"
    elif "q" == xtext:
            p.terminate()
            ytext = "q"
    elif "good" in xtext:
            ytext = "greetings"
    
            
    else: 
            ytext = ""
    return ytext

def send_message(message): 
#     print((message)) 
    response = res(message)
    response = "Friday : " + response
    message = "Me : " + message
    return response



from tkinter import *
root = Tk()
root.title('Chatbot')
root.geometry("400x400")
label1 = Label(root, text = "Chatbot",font=("Arial", 25))
label2 = Label(root, text = "Messsage",font=("Arial", 10))


def printInput():
    inp = T2.get(1.0, "end-1c")
    my_input = inp
    my_input = my_input.lower() 
    related_text = real(my_input) 
    response = send_message(related_text)
    imp = "Me : " + inp
    T2.delete("1.0", "end")
    T1.insert(1.0, imp + '\n')
    T1.insert(2.0, response + '\n')


    if my_input == "exit" or my_input == "stop": 
        sys.exit()


T1 = Text(root, height = 14, width = 52)
T2 = Text(root, height = 2, width = 52)
button = Button(root, text="Send text", command=printInput)
label1.pack()
T1.pack()
label2.pack()
T2.pack()
button.pack()

root.mainloop()






