GradeList = ["5.10a or 6a", "5.10b or 6a", "5.10c or 6b", "5.10d or 6b",
             "5.11a or 6c", "5.11b or 6c", "5.11c or 6c+", "5.11c or 6c+", "5.11d or 7a", "5.12- or 7a",
             "5.12a or 7a+", "5.12a or 7a+", "5.12b or 7b", "5.12b or 7b",
             "5.12c or 7b+", "5.12c or 7b+", "5.12d or 7c","5.12d or 7c",
             "5.13a or 7c+", "5.13a or 7c+", "5.13b or 8a", "5.13b or 8a",
             "5.13c or 8a+", "5.13c or 8a+", "5.13d or 8b", "5.13d or 8b",
             "5.14a or 8b+", "5.14a or 8b+", "5.14b or 8c", "5.14b or 8c",
             "5.14c or 8c+", "5.14c or 8c+", "5.14d or 9a", "5.14d or 9a",
             "5.15a or 9a+", "5.15a or 9a+", "5.15b or 9b", "5.15b or 9b",
             "5.15c or 9b+", "5.15d or 9c", ]

Bodyweight = ["100%", "110%", "120%", "130%", "140%",
              "150%", "160%", "180%", "200%", "220%",]

def GetMaxHang():
    while True:
        try: 
            maxhang = int(input("What bodyweight percentage did you hit for your hang? \n"))
            100 <= maxhang <= 220
        except ValueError:
            print("Enter a valid percentage, please!")
            continue
        else:
            break
    if maxhang <= 150:
        maxhangindex = str(maxhang)
        return int(maxhangindex[1]) + 1
    elif 160 <= maxhang < 180:
        return 7
    elif 180 <= maxhang < 200:
        return 8
    elif 200 <= maxhang < 220:
        return 9
    elif 220 <= maxhang:
        return 10
    
def GetMaxPull():
    while True:
        try: 
            maxpull = int(input("What bodyweight percentage was your pull-up max? \n"))
            100 <= maxpull <= 220
        except ValueError:
            print("Enter a valid percentage, please!")
            continue
        else:
            break
    if maxpull <= 150:
        maxpullindex = str(maxpull)
        return int(maxpullindex[1]) + 1
    elif 160 <= maxpull < 180:
        return 7
    elif 180 <= maxpull < 200:
        return 8
    elif 200 <= maxpull < 220:
        return 9
    elif 220 <= maxpull:
        return 10

def GetAbWork():
    abWorkouts = ["Knee raise", "L sit", "Front lever"]
    while True:
        try: 
            style = input("What type of ab workout did you complete? (Knee raise, L sit, or Front lever) \n")
            style in abWorkouts
        except ValueError:
            print("Only select between 'Knee raise', 'L sit' or 'Front lever'")
            continue
        else:
            break
    time = int(input("How long did you do your ab workout for? Answer this in number of seconds. \n"))
    if style == "Knee raise":
        if 10 <= time < 20:
            return 1
        if 20 <= time < 30:
            return 2
        if 30 <= time:
            return 3
    if style == "L sit":
        if 10 <= time < 15:
            return 4
        if 15 <= time < 20:
            return 5
        if 20 <= time:
            return 6
    if style == "Front lever":
        if 5 <= time < 10:
            return 7
        if 10 <= time < 20:
            return 8
        if 20 <= time < 30:
            return 9
        if 30 <= time:
            return 10
    else:
        return 0

def GetHangTime():
    while True:
        try:
            hangtime = int(input('How many seconds were you able to dead hang on the bar for? \n'))
        except ValueError:
            print("Enter a valid number of seconds that you hung for")
            continue
        else:
            break
    if 30 <= hangtime < 60:
        return 1
    if 60 <= hangtime < 90:
        return 2
    if 90 <= hangtime < 120:
        return 3
    if 120 <= hangtime < 150:
        return 4
    if 150 <= hangtime < 180:
        return 5
    if 180 <= hangtime < 210:
        return 6
    if 210 <= hangtime < 240:
        return 7
    if 240 <= hangtime < 300:
        return 8
    if 300 <= hangtime < 360:
        return 9
    if 360 <= hangtime:
        return 10
    else:
        return 0

score1 = GetMaxHang()
score2 = GetMaxPull()
score3 = GetAbWork()
score4 = GetHangTime()

def ConvertScore():
    print("Max Hang: " + str(score1))
    print("Max Pull: " + str(score2))
    print("Ab Workout: " + str(score3))
    print("Dead Hang: " + str(score4))
    score = score1 + score2 + score3 + score4 - 1
    print("Total Score: " + str(score+1))
    if score > 0:
        return GradeList[score]
    else:
        return "You might want to train some more before taking this test"

print(ConvertScore())
