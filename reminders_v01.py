currenthour = input("What is the current hour? (Military Hour:0 - 23) ")
currenthourfloat = float(currenthour)
if currenthourfloat <= 5:
    print("It's early. You should be sleeping!")
elif currenthourfloat <=7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast...")
elif currenthourfloat <= 9:
    print("Time to go to work.")
elif currenthourfloat <= 12:
    print("You should be working!")
elif currenthourfloat <= 13:
    print("Take your lunch break!")
elif currenthourfloat <= 17:
    print("Do you feel that afternoon lull?")
elif currenthourfloat <= 19:
    print("Time to hit the gym...")
elif currenthourfloat <= 21:
    print("Gotta eat that dinner.")
elif currenthourfloat <= 23:
    print("Get that SLEEP. And rePEAT!")
else:
    print("You didn't type an acceptable value!(0-23)")
