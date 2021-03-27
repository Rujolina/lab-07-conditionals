move = input(" Does it move? (yes/no) ")
if (move == "yes"):
    should = input(" Should it? (yes/no) ")
    if (should == "yes"):
        print(" No problem ")
    elif (should == "no"):
        print(" Then use duct tape!!! ")
    else:
        print(" Answer my question! You didn't type yes or no. " )
elif (move == "no"):
    did = input(" Did you try to move it? (yes/no) " )
    if (did == "yes"):
        print(" You did it! Good job!!! " )
    elif (did == "no"):
        print(" Well then try moving it. duh ")
    else:
        print(" Answer my question! You didn't type yes or no. ")
else:
    print(" Answer my question! You didn't type yes or no. ")
