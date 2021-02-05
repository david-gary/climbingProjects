# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:07:05 2020

@author: dgary
"""

#! python3
from tkinter import *

root = Tk()
root.title("Climbing Log - Record Your Session!")
root.geometry("500x500")

boulder_grade_options = [
     "None", "V0", "V1", "V2", "V3", 
     "V4", "V5", "V6", "V7", "V8", 
     "V9", "V10", "V11", "V12", "V13", 
     "V14", "V15", "V16", "V17"
    ]

sport_grade_options = [
    "None", 
    "5.0", "5.1,", "5.2", "5.3", "5.4", 
    "5.5", "5.6", "5.7", "5.8", "5.9", 
    "5.10a", "5.10b", "5.10c", "5.10d", 
    "5.11a", "5.11b", "5.11c", "5.11d", 
    "5.12a", "5.12b", "5.12c", "5.12d", 
    "5.13a", "5.13b", "5.13c", "5.13d", 
    "5.14a", "5.14b", "5.14c", "5.14d", 
    "5.15a", "5.15b", "5.15c", "5.15d"
    ]

boulders = [
    "V5", "V6", "V7", "V8", 
     "V9", "V10", "V11", "V12", "V13", 
     "V14", "V15", "V16", "V17"]
routes = [
    "5.13a", "5.13b", "5.13c", "5.13d", 
    "5.14a", "5.14b", "5.14c", "5.14d", 
    "5.15a", "5.15b", "5.15c", "5.15d"]
#clicked = StringVar()
#clicked.set("None")

#drop1 = OptionMenu(root, clicked, "None", "Sport", "Boulder")
#dropBoulders = OptionMenu(root, clicked, *boulder_grade_options)
#dropSport = OptionMenu(root, clicked, *sport_grade_options)

def boulder_points(problems):
    boulder_point_total = 0 
    for problem in problems:
        grade_value = 2 * int(problem[1:])
        boulder_point_total += grade_value
    return boulder_point_total

def sport_points(route_list):
    sport_point_total = 0
    for route in route_list:
        try:
            grade_value = int(route[2:])
            sport_point_total += grade_value
        except ValueError:
            grade_value = int(route[2:-1])
            if route[-1] == 'a':
                grade_value += 0.2
            elif route[-1] == 'b':
                grade_value += 0.4
            elif route[-1] == 'c':
                grade_value += 0.6
            elif route[-1] == 'd':
                grade_value += 0.8
            sport_point_total += grade_value
    return sport_point_total

#drop1.pack()
'''if drop1.get() == "Boulder":
    while "None" not in boulders:
        dropBoulders
        dropBoulders.pack()
elif drop1 == "Sport":
    kggkgkg
else: 
    pass'''

boulder_point_total = boulder_points(boulders)
sport_point_total = sport_points(routes)

myBoulders = Label(root, text="Your bouldering point total from today is: "+ str(boulder_point_total))
myRoutes = Label(root, text="Your sport climbing point total from today is: "+ str(sport_point_total))
myBoulders.grid(row=0)
myRoutes.grid(row=1)

root.mainloop()


