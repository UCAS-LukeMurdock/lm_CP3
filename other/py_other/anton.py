
while True:
    name = input("[Enter 0 to exit]\nwhat is your name: ").strip()
    if name == "0":
        break
    if name.lower() == "anton":
        print(f"You are the best {name}")
        
    else:
        choice = input("are you a robot: ")
        if choice == "no":
            print("you are not a hacker for now :)")
        elif choice == "yes":
            print("you hacker get out of here!!!!!!!!!!!!")
        else:
            print("you are trying to hack me, well ai is to strong,")
            print("i am going to tell the whole internit that your name is "+ name)   
            print ("and you are so like why this is my computer not yours")
        choice = input("1 + 1 = ")
        if choice == "2":
            print ("nice you are actually smart")
        else:
            print("you are so not smart it is easy math the fact that you are reading thist means you should be smart")