import os
from calci import *
from Hello import *
from websearch import *
from clock import *
from shutdown import *
from caleendar import *
from climate import *
i=1
usnamme=input("Greeting!Enter your name : ")
f=open("E:log.txt","a")
while i!=0 :
    ui=input("Type a message : ")
    v=[]
    uii=ui.split()
    dct={"add":"+","sum":"+","subtract":"-","difference":"-","multiply":"*","product":"*","divide":"/","remainder":"%","quotient":"/","power":"**","square":"**2","cube":"**3","square root":22,"cube root":33,"root":22,"convert":"c"}
    for z in uii:
        if z in dct:
            v.append(dct[z])
    if ui=="":
        print("empty input")
    elif "hi" in ui or "hello" in ui:
        hello(usnamme)
    elif "ok" in ui or "sure" in ui:
        continue
    elif len(v)>0 or "calculate" in ui:
        calci(ui)
    elif ui=="\n":
        print("please provide an input")
    elif "exit" in ui or "bye" in ui:
        print("Thank you for using me! Have a nice time.")
        i=0
    elif "time" in ui and "date" in ui:
        tim()
        date()
    elif "weather" in ui or "climate" in ui:
        weather()
    elif "time" in ui:
        tim()
    elif "date" in ui:
        date()
    elif "shut down" in ui or "shutdown" in ui or "power off" in ui or "poweroff" in ui:
        print("Exitting the assistant")
        print("Thankyou for using me, See you again")
        shutdown()
    elif "search" in ui or "google" in ui or "net" in ui or "internet" in ui:
        if "search" in ui or "google" in ui:
            ui=ui[7:]
        print("I found these on web")
        search(ui)
    else:
        f.write(ui+"\n")
        print("your input '{}' is new to us \nWe shall develop our software and make sure your input will get appropriate output ".format(ui))
f.close()
