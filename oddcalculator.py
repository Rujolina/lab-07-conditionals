firstnum = input("Give me a number, any number... ")
secondnum = input("Wonderful, and give me another number... ")
operation = input("And what operation do you want? (mul/div/mod) ")
if operation == "mul":
    print(int(firstnum) * int(secondnum))
elif operation == "div":
    print(int(firstnum) / int(secondnum))
elif operation == "mod":
    print(int(firstnum) % int(secondnum))
else:
    print("**** Invalid operation *****")
