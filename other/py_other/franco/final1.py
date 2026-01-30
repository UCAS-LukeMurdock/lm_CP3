import time, sys, random

def startup_room():
    tun = [5, 10, ["sample 1", "sample 2", "sample 3", "sample 4", "sample 5"]]
    nan = [5, 50, ["sample 1", "sample 2", "sample 3", "sample 4", "sample 5"]]

    wrldr = False

    print("You should wake up!\nNo! You should keep sleeping, just a bit longer!")

    if wrldr == False:
        print("1) wake up\n2) keep sleeping?")
        wrldr = inputchecker(2)

    if wrldr == 1:
        player = {"state":{"alive":True},
                  "stats":{"sleepiness":0, "adrenaline":10, "memory":10},
                  "statmax":{"sleepiness":50, "adrenaline":10, "memory":10},
                  "inventory":{},
                  "collected items":{},
                  "usable items":{"coffee":"decreases sleepiness by 10", "cheat sheet":"when you use the cheat sheet you answer a random amount of questions with a random chance of getting caught-losing the battle",
                                  "energy drink":"gives you 2 adrenaline and -15 sleepiness", "candy bag":"gives you 3 memory", "burrito":"decreases sleep by 10 and increases adrenaline by 3"},
                  "skills":{"slap":"Costs 2 adrenaline, but heals 15 sleepiness."},
                  "unacquired skills":{"random recollection":"costs 5 adrenaline, you do 15 questions", "save the hardest for last":"costs 2 adrenaline, you do 5 questions", "guess":"costs 2 adrenaline, answer 3 questions, heal 5 sleep."},
                  }

        winlossrealworld = tun_fight(player, tun)
        winlossrealworld = winlossrealworld[1]
        winlossdreamworld = False
    elif wrldr == 2:
        player = {"state":{"alive":True},
                  "stats":{"lucidity":0, "social battery":10},
                  "statmax":{"lucidity":50, "social battery":10},
                  "miscish stats":{"charm":5, "imagination":0},
                  "inventory":{},
                  "Collected items":{},
                  "usable items":{"sleep tea":"decreases lucidity by 10", "big rock":"-20 lucidity",
                                  "frying pan":"You make yourself eggs--you recharge 5 social batter", "PSPC":"recharge 10 social batter"},
                  "skills":{"pretend nap":"You pretend to sleep! Keeping up the fascade costs 2 social battery but you lose 15 lucidity!"},
                  "unacquired skills":{"dramatic lie":"costs 10 social battery and does 30 charm", "puppy dog eyes":"Costs 2 social batter, does 7 charm", "disassociate":"gain 3 social battery, skip a turn"}, 
                  "battles":[]
                  }
        winlossdreamworld = nan_fight(player, nan)
        winlossdreamworld = winlossdreamworld[1]
        winlossrealworld = False
    
    if winlossdreamworld == True:
        nice_forest(player)
    elif winlossrealworld == True:
        bedroom(player)

def bedroom(player):
    print("You woke up, your alarm blared on your table")
    print("After getting up, you look around")
    while True:
        print("1) Check desk\n2) Find glasses\n3) Go to the kitchen")
        choice = inputchecker(3)

        if choice == 1:
            if "phone" not in player["collected items"]:
                print("You found your phone")
                player["collected items"]["phone"] = "It has precious memories on it"
            else: 
                print("You aready have your phone")
        elif choice == 2:
            if "glasses" not in player["collected items"]:
                print("You found your glasses")
                print("Your maximum memory increased by 5!")
                player["statmax"]["memory"] = player["statmax"]["memory"] + 5
                player["collected items"]["glasses"] = "It helps you see better, and makes you look smarter"
            else:
                print("You already have your glasses.")
        elif choice == 3:
            print("You went to the kitchen.")
            kitchen(player)

def kitchen(player):
    print("Your kitchen, as always is somewhat messy, especially with finals coming up.")
    print("Oh, right... FINALS! Hurriedly, you look around and check what you need to do.")
    while True:
        print("1) Make Coffee\n2) Look outside\n3) Go to college")
        choice = inputchecker(3)

        if choice == 1:
            if "coffee" not in player["collected items"]:
                print("You made yourself coffee")
                player["collected items"]["coffee"] = player["usable items"]["coffee"]
                player["inventory"]["coffee"] = player["usable items"]["coffee"]
            else: 
                print("You've already made your morning coffee")
        elif choice == 2:
            print("You look outside your window... there is stuff.")
        elif choice == 3:
            print("You went out the door and walked to school")
            campus(player)

def campus(player):
    print("You have a few moments before you have to go to class and start your remaining finals")
    while True:
        print("1) Go to the bleachers\n2) Go to the library\n3) Go to the food court")
        choice = inputchecker(3)

        if choice == 1:
            print("You go to the bleachers")
            bleachers(player)
        elif choice == 2:
            print("You go to the library")
            library(player)
        elif choice == 3:
            print("You got to the food court")
            food_court(player)

def bleachers(player):
    print("As you get there, you see a couple distinct groups of people littered around the field and bleachers.")
    while True:
        print("1) Talk to the sketchy kids behind the bleachers\n2) Look around the seats\n3) Talk to the popular kids\n4) Go to the library\n5) Go to the food court\n6) Go to class")
        choice = inputchecker(6)

        if choice == 1:
            if "energy drink" not in player["collected items"]:
                print("You go and talk to the sketchy kids.")
                print("They gave you an energy drink, they've been banned for years now.")
                player["inventory"]["energy drink"] = player["usable items"]["energy drink"]
                player["collected items"]["energy drink"] = player["usable items"]["energy drink"]
            else:
                print("You've already talked to them.")
        elif choice == 2:
            if "candy bag" not in player["collected items"]:
                print("You look around the seats and find a bag full of smarties")
                print("You got the candy bag!")
                player["inventory"]["candy bag"] = player["usable items"]["candy bag"]
                player["collected items"]["candy bag"] = player["usable items"]["candy bag"]
            else:
                print("Unfortunately there wasn't anything else...")
        elif choice == 3:
            if "phone" in player["collected items"]:
                if "cheat sheet" not in player["collected items"]:
                    print("You talk to one of the cheerleaders and she adds you to a group chat with other well know schoolers.")
                    print("You look at it and see that theres a cheat sheet on it.")
                    print("You got the cheat sheet! Don't get caught!")
                    player["inventory"]["cheat sheet"] = player["usable items"]["cheat sheet"]
                    player["collected items"]["cheat sheet"] = player["usable items"]["cheat sheet"]
                else:
                    print("You talk to the cheerleader, but since you've already been added to the group chat, she just thinks you're hitting on her.")
            else:
                print("You talk to the cheerleader, although, you don't have your phone so you can't give her your number. ")
        elif choice == 4:
            print("You went to the library next, you had enough of trying to be popular")
            library(player)
        elif choice == 5:
            print("You went to the food court, after all that 'excercising' you felt famished")
            food_court(player)
        elif choice == 6:
            while True:
                starttestsq = input("Are you sure you want to start your finals now?(Y/N):")

                if starttestsq == "Y":
                    print("You go into your classroom")
                    math_t(player)
                elif starttestsq == "N":
                    print("You change your mind")
                    break
                else:
                    print("Stop being so indecisive!")

def library(player):
    print("It's mostly quiet with the occasional 'NO WAY!' sprinkled here and there.\n It's either a really good book or crazy gossip.")
    while True:
        print("1) Study your classes\n2) Study how to take tests\n3) Look around\n4) Go to the bleachers\n5) Go to the food court\n6) Go to class")
        choice = inputchecker(6)

        if choice == 1:
            if player["statmax"]["memory"] < 20:
                print("You spend a while reading through your notes and practicing active recall.")
                print("You hate it.")
                time.sleep(1)
                print("You got 1 whole maximum memory")
                player["statmax"]["memory"] = player["statmax"]["memory"] + 1
            else:
                print("NO! Enough studying this STUPID chem and STUPID math and STUPID history.")
        elif choice == 2:
            if player["unacquired skills"]:
                print("You find a book about test taking skills")
                print("It's much more manageable than studying the actual material")
                skill = str(random.choice(list(player["unacquired skills"].keys())))
                player["skills"][skill] = player["unacquired skills"][skill]
                del player["unacquired skills"][skill]
                print(f"You got:\n{skill}")
            else:
                print("There's not really anything else to learn")
        elif choice == 3:
            print("Super duper awesome and cool flavor text")
        elif choice == 4:
            print("You went to the bleachers next, because studying is for nerds")
            bleachers(player)
        elif choice == 5:
            print("You went to the food court, using your brain spends a lot of energy.")
            food_court(player)
        elif choice == 6:
            while True:
                starttestsq = input("Are you sure you want to start your finals now?(Y/N):")

                if starttestsq == "Y":
                    print("You go into your classroom")
                    math_t(player)
                elif starttestsq == "N":
                    print("You change your mind")
                    break
                else:
                    print("Stop being so indecisive!")

def food_court(player):
    print("Chatter fills the air as people understandably big back on delicious... fast food... actually maybe not too understandable.")
    while True:
        print("1) Go to the Chipotle\n2) Relax\n3) Spontaneosly break out into dance and song\n4) Go to the bleachers\n5) Go to the library\n6) Go to class")
        choice = inputchecker(6)

        if choice == 1:
            if "burrito" not in player["collected items"]:
                print("You enter the chipotle line.")
                print("The cute cashier asks for your order, so while you would normally order a taco, you accidentally just said burrito instead because you were nervous.")
                player["inventory"]["burrito"] = player["usable items"]["burrito"]
                player["collected items"]["burrito"] = player["usable items"]["burrito"]
            else:
                print("You don't have the guts to try asking for a refund and ordering a taco instead.")
        elif choice == 2:
            print("Since for some reason the food court has some massage chairs, you sit in one.")
            if player["statmax"]["sleepiness"] >= 80:
                print("You try to take a nap but you feel rested enough")
            else:
                print("You take a nap in a massage bed.")
                time.sleep(1)
                print("Your maximum sleepiness increased by 15!")
                player["statmax"]["sleepiness"] = player["statmax"]["sleepiness"] + 15
        elif choice == 3:
            if player["statmax"]["adrenaline"] < 15:
                print("You earned 5 adrenaline!\n... and +100 embarrasment points")
                player["statmax"]["adrenaline"] = player["statmax"]["adrenaline"] + 5
            else:
                print("At this point theres not much of a reason to because you're already super fired up!")
        elif choice == 4:
            print("You went to the bleachers, excercise is probably good on a full stomache...")
            bleachers(player)
        elif choice == 5:
            print("You went to the library, studying is very important")
            library(player)
        elif choice == 6:
            while True:
                starttestsq = input("Are you sure you want to start your finals now?(Y/N):")

                if starttestsq == "Y":
                    print("You go into your classroom")
                    math_t(player)
                elif starttestsq == "N":
                    print("You change your mind")
                    break
                else:
                    print("Stop being so indecisive!")

def nice_forest(player):
    print("This route is WIP")

    print("You find yourself in the nicer part of the forest.")
    boar = ["boar", 10, ["Wow! so flavor", "text two", "even more flavor"], 75]
    while True:
        print("1) Look in the bush nearby\n2) Go deeper inside\n3) Go into the deep dark cave nearby\n4) Have a picnic\n")
        choice = inputchecker(4)

        if choice == 1:
            if "boar" not in player["battles"]:
                print("You ruffle the bush VERY rudely.")
                print("A gigantic boar--as in three times the size of the bush--somehow jumps out of the bush and attacks you!!.")
                fight = combat(boar, player)
                player = fight[1]
                if fight[0] == "WIN":
                    print("You charmed the wild boar! It gave you a Portable SoundProof Chamber... don't ask how.")
                    player["inventory"]["PSPC"] = player["usable items"]["PSPC"]
                    player["Collected items"]["PSPC"] = player["usable items"]["PSPC"]
            else:
                print("You already charmed the boar there so it would be rude to disturb it again.")
        elif choice == 2:
            print("You go deeper into the forest.")
            evil_forest(player)
        elif choice == 3:
            print("For SOME reason you decided to go into the deep DARK CAVE")
            cave(player)
        elif choice == 4:
            print("You decided to just relax in a open part of the forest for a while...")
            time.sleep(2)
            print("It did absolutely nothing")

def evil_forest(player):
    print("You go into the obviously closer to progressing the game area.")
    tree = ["tree", 15, ["Wow! so flavor", "text two", "even more flavor"], 100]
    while True:
        print("1) Assault a tree\n2) Go EVEN deeper\n3) Go BACK to the NICE and GOOD part of the forest\n4) Go for a stroll... In the forest with horrors within your comprehension...\n")
        choice = inputchecker(4)
        if choice == 1:
            if "tree" not in player["battles"]:
                print("You kick some random tree, probably because you thought the option would be funny.")
                print("The tree REALLY didn't think it was funny.")
                fight = combat(tree, player)
                player = fight[1]
                if fight[0] == "WIN":
                    print("You charmed the angry tree! It gave you a wooden ring..... You'd rather not think about the implications")
                    print("You put the ring on, it increased your charm by 5!")
                    player["miscish stats"]["charm"] = player["miscish stats"]["charm"] + 5
            else:
                print("You already hit the tree why would you want to hit it again??")
        elif choice == 2:
            print("You find a HUT. \nSince theres definitely never been stories about why you shouldn't go into houses in creepy haunted forests, you head inside.")
            hut(player)
        elif choice == 3:
            print("Because you know what's good for you, you go back to the lighter part of the forest.")
            nice_forest(player)
        elif choice == 4:
            print("You walk around and to your surprise, all of the HWIYC are very kind and dont murder you.")
            time.sleep(2)
            print("They're still scary though...")

def hut(player):
    print("You go into the hut... It has an old lady in it, she wont eat you maybe...")
    oldlady = ["old lady", 20, ["Wow! so flavor", "text two", "even more flavor"], 125]
    while True:
        print("1) Insult the lady\n2) Go into the creepydiki cellar\n3) Go BACK to the EVIL and BAD part of the forest\n4) Talk to the lady without insulting her\n")
        choice = inputchecker(4)
        if choice == 1:
            if "old lady" not in player["battles"]:
                print("You tell the old lady that she looks like a wrinkly sack of eggs.")
                print("She gets out her cane and starts trying to smack you with it!")
                fight = combat(oldlady, player)
                player = fight[1]
                if fight[0] == "WIN":
                    print("She ended up giving you some sleep tea...... You'd rather not think about the implications")
                    player["inventory"]["sleep tea"] = player["usable items"]["sleep tea"]
                    player["Collected items"]["sleep tea"] = player["usable items"]["sleep tea"]
            else:
                print("You already insulted her, you really shouldn't do it again.")
        elif choice == 2:
            print("You find a door that leads to some kind of dark and depressed cellar.")
            cellar(player)
        elif choice == 3:
            print("You head out of the surprisingly pleasant hut, uneaten.")
            evil_forest(player)
        elif choice == 4:
            print("You talk to her and realize that the old lady isn't actually all that bad.")
            time.sleep(2)
            print("She does say some mildly concerning things though... \n'grumble grumble... new gens... grumble grumble...\nThe haters will hate you guess.")

def cellar(player):
    print("You see a lot of chains... and more chains... You wonder what they're for.")
    ogre = ["Ogre", 40, ["Wow! so flavor", "text two", "even more flavor"], 150]
    while True:
        print("1) Look around a little bit  \n2) Free the weirdly complacent looking ogre \n3) Go back upstairs, where there isn't just piles on piles of chains.")
        choice = inputchecker(3)
        if choice == 1:
            print("You look around the cellars, and notice that it's not just chains, it's cuffs as well.")
            print("It seems as though there used to be many confined here.")
        elif choice == 2:
            print("You found a weird looking ogre and decide to free it from it's chains.\n As soon as you unlock the last cuff, it uppercuts your jaw!")
            time.sleep(2)
            print("Well that was rude.")
            fight = combat(ogre, player)
            player = fight[1]
            if fight[0] == "WIN":
                print("The ogre gives you a smooch on the top of your head. It's probably just some sort of Ogre custom")
                print("BEEP BEEP BEEP")
                print("You woke up and oh right... finals are today, then you check the time and see that they WERE today.")
                print("Oh well.. you'll figure out a way to get that car.")
                DW_route_parents(player)
        elif choice == 3:
            print("You go uptairs to the nicer part of the hut house")
            hut(player)
        elif choice == 4:
            print("You look around the cellar, trying to ignore the ogre in the corner of your vision... surely it has nothing to do with you.")

def cave(player):
    print("It's really really really dark... One might say you could describe it as 'dark, darker yet darker")
    bat = ["bat", 15, ["Wow! so flavor", "text two", "even more flavor"], 125]
    wisp = ["wisp", 20, ["Wow! so flavor", "text two", "even more flavor"], 150]
    while True:
        print("1) Try to stumble further into the cave  \n2) Go into the glowing chamber of light you see a ways away \n3) Go back into the light.\n4) let out an earpeircing scream")
        choice = inputchecker(4)
        if choice == 1:
            print("You try to reach into the darkness and take a few steps...")
            time.sleep(2.5)
            print(f"Unfortunately, you walk straight first into a wall... That will leave a mark.")
        elif choice == 2:
            if "wisp" not in player["battles"]:
                print("You decide that the slightly lit up path that leads to what seemed like a glowing room was the best option.")
                print("In side was a glowing ball of fire that immediately started flaming around menacingly.")
                time.sleep(1.5)
                print("It doesn't seem to like you.")
                fight = combat(wisp, player)
                player = fight[1]
            if fight[0] == "WIN":
                print("After convincing the wisp it left you alone and opened the a hidden path to a deeper part of the cave.")
                if "frying pan" not in player["Collected items"]:
                    print("It also gave you a frying pan!")
                    player["Collected items"]["frying pan"] = player["usable items"]["frying pan"]
                    player["inventory"]["frying pan"] = player["usable items"]["frying pan"]
                while True:
                    deep = input("Would you like to go deeper?(Y/N):\n")
                    if deep == "Y":
                        print("You walk deeper into the cave.")
                        deeper_cave(player)
                    elif deep == "N":
                        print("You decide to look around a little more before going deeper.")
                        break
                    else:
                        continue
        elif choice == 3:
            if "sun glasses" not in player["Collected items"]:
                print("You go back to the forest, the light blinds you for a few moments before you regain your senses.")
                nice_forest(player)
            else:
                print("Your sun glasses shield your eyes from the sun, so you're eyes aren't blinded.")
        elif choice == 4:
            if "bat" not in player["battles"]:
                print("For some reason, you decide that the current moment would be a great time to shriek at the top of your lungs.")
                print("Your... lovely voice startles a flock of bats that were on the ceiling and the flock out.")
                print("One of them knocks into you!")
                fight = combat(bat, player)
                if fight[0] == "WIN":
                    print("You pacify the bat and it gives you a pair of sunglasses!")
                    print("You put them on and gain 5 charm!")
                    print("Although now you wonder how the bat will fair in the bright sun...")
                    player["Collected items"]["sun glasses"] = "They do sun glass stuff... on that note, why are they called SUN-GLASSES, if they BLOCK the sun and glasses are supposed to help you see BETTER or MORE? Shouldn't they make the sun like ten times brighter instead or something?"
            else:
                print("You shriek again but theres no more bats in the cave")

def deeper_cave(player):
    rockguy = ["Igneous Rock Spirit", 30, ["Wow! so flavor", "text two", "even more flavor"], 200]
    print("It's surprisingly gotten REALLY hot in here... There's even streams of flowy lava here and there.")
    while True:
        print("Will you:\n1) lay down and take a toasty nap\n2) Kick the wierdly large looking rock\n3) Go back to the darker part of the cave.")
        choice = inputchecker(3)
        if choice == 2:
            if "Igneous Rock Spirit" not in player["battles"]:
                print("You kick some random rock.")
                print("I don't even know why you did that, maybe you knew it would be a combat encounter?")
                fight = combat(rockguy, player)
                player = fight[1]
                if fight[0] == "WIN":
                    print("The giant rock gives you a big rock!")
                    if "tree" in player["battles"]:
                        print("What's with animate-inanimate objects and giving you parts of themselves?")
                    player["inventory"]["big rock"] = player["usable items"]["big rock"]
                    player["Collected items"]["big rock"] = player["usable items"]["big rock"]
            else:
                print("The rock hast already been kicked... the creator says you're not allowed to try winning against it twice...")
        elif choice == 1:
            print("You find that the heat of the lava makes for a pretty good source of heat and take nap.")
            print("Although the lack of cushioning in there makes it hard to actually sleep.")
        elif choice == 3:
            print("You walk back on the path to the darker area of the cave.")
            cave(player)

def tun_fight(playerchar, tunlytun):
    # add some sleep statements around here
    turn = 0

    while True:
        if playerchar["stats"]["sleepiness"] >= playerchar["statmax"]["sleepiness"]:
            contq = cont()
            if contq == True:
                update = playerregen(playerchar)
                playerchar = update
                return playerchar, False
            else: 
                sys.exit()
        if turn >= tunlytun[1]:
            print("You won!")
            update = playerregen(playerchar)
            playerchar = update
            return playerchar, True

        print("This is your chance to show what you can do!") # lowkey make a flavor text randomizer here pls
        print("You will be able to use your Memory to 'recall'-- your skills and items do a variety of things!")
        print(f"You currently have:")
        print(f"Sleepiness:{playerchar["stats"]["sleepiness"]}/{playerchar["statmax"]["sleepiness"]}\nAdrenaline:{playerchar["stats"]["adrenaline"]}/{playerchar["statmax"]["adrenaline"]}\nMemory:{playerchar["stats"]["memory"]}/{playerchar["statmax"]["memory"]}")
        while True:
            turnchoice = input("Would you like to\n1) Recall\n2) Skills\n3) Items:\n")
            if turnchoice == "1":
                if playerchar["stats"]["memory"] > 0:
                    print("You tried to remember something you forgot!")
                    playerchar["stats"]["memory"] = playerchar["stats"]["memory"]-1
                    break
                else:
                    print("You don't have enough memory!")
            elif turnchoice == "2":
                if playerchar["stats"]["adrenaline"] >= 2:
                    RW_skills(0, playerchar)
                    break
                else:
                    print("You don't even have enough adrenaline to use a single skill try something else!")
            elif turnchoice == "3":
                print("You don't have any items, sorry XD")
                break
            else:
                print("That is NOT an option sadly")
            
        direction = random.randint(1, 2)
        change = random.randint(0, 5)

        if direction == 1:
            damage = tunlytun[0] + change
        elif direction == 2:
            damage = tunlytun[0] - change

        print(random.choice(tunlytun[2]))

        print(f"Your sleepiness increased by {damage}")

        playerchar["stats"]["sleepiness"] = playerchar["stats"]["sleepiness"] + damage

        turn += 1
        
def math_t(player):
    questions = 35
    panic = 0
    panicchance = [1 , 0 , 0 , 0 , 0]
    player = playerregen(player)
    print("Listen up! Today I will hand out your math tests!")
    print("That means that you must NOT use cheat, speak or peak!")
    time.sleep(1.5)
    print("Understood?!?")
    time.sleep(.75)
    print("\nYeah, sure.\n ")
    time.sleep(.5)
    print("Alright, I'll hand out your tests now!")
    while True:
        
        if panic == 0:
            print(f"You have:\n{questions} questions left\n{player["stats"]["memory"]}/{player["statmax"]["memory"]} memory\n{player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness\n{player["stats"]["adrenaline"]}/{player["statmax"]["adrenaline"]} adrenaline")

            print("what will you do?\n1) answer questions\n2)use a skill\n3) use an item?:\n")
            turnch = inputchecker(3)

            if turnch == 1:
                if player["stats"]["memory"] > 0:
                    questions = questions - 3
                    player["stats"]["memory"] = player["stats"]["memory"] - 1
                else:
                    print("You can't remember it right now!")
            elif turnch == 2:
                update = RW_skills(questions, player)
                questions = update[0]
                player = update[1]
            elif turnch == 3:
                item = RW_items(questions, player)
                questions = item[0]
                player = item[1]
            
            panicquestion = random.choice(panicchance)
            
            if panicquestion == 1:
                panic = random.randint(1, 3)
        else:
            panic = panic - 1
            print(f"You have {player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness")

        print("You gained 5 sleepiness!")
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] + 5

        if player["stats"]["sleepiness"] >= player["statmax"]["sleepiness"]:
            contq = cont()
            if contq == True:
                math_t(player)
        if questions <= 0:
            print("you survived!")
            chem_t(player)

def chem_t(player):
    questions = 30
    playerupdate = playerregen(player)
    player = playerupdate
    print("Alright class! Backpacks to the front!\n Time for the chem test I guess...")
    while True:
        
        print(f"You have:\n{questions} questions left\n{player["stats"]["memory"]}/{player["statmax"]["memory"]} memory\n{player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness\n{player["stats"]["adrenaline"]}/{player["statmax"]["adrenaline"]} adrenaline")

        print("what will you do?\n1) answer questions\n2)use a skill")
        turnch = inputchecker(2)

        if turnch == 1:
            if player["stats"]["memory"] > 0:
                questions = questions - 3
                player["stats"]["memory"] = player["stats"]["memory"] - 1
            else:
                print("You can't remember it right now!")
        elif turnch == 2:
            update = RW_skills(questions, player)
            questions = update[0]
            player = update[1]

        damage = random.randint(5, 10)

        print("You gained 10 sleepiness!")
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] + damage

        if player["stats"]["sleepiness"] >= player["statmax"]["sleepiness"]:
            contq = cont()
            if contq == True:
                chem_t(player)
        if questions <= 0:
            print("you survived!")
            history_t(player)

def history_t(player):
    questions = 75
    playerupdate = playerregen(player)
    player = playerupdate
    print("Open up your laptops gang!\n The code is kjrepsdjfgvvcLFJA")
    while True:

        print(f"You have:\n{questions} questions left\n{player["stats"]["memory"]}/{player["statmax"]["memory"]} memory\n{player["stats"]["sleepiness"]}/{player["statmax"]["sleepiness"]} sleepiness\n{player["stats"]["adrenaline"]}/{player["statmax"]["adrenaline"]} adrenaline")

        print("what will you do?\n1) answer questions\n2)use a skill\n3) use an item?:\n")
        turnch = inputchecker(3)

        if turnch == 1:
            if player["stats"]["memory"] > 0:
                questions = questions - 3
                player["stats"]["memory"] = player["stats"]["memory"] - 1
            else:
                print("You can't remember it right now!")
        elif turnch == 2:
            update = RW_skills(questions, player)
            questions = update[0]
            player = update[1]
        elif turnch == 3:
            item = RW_items(questions, player)
            questions = item[0]
            player = item[1]

        damage = random.randint(5, 10)

        print(f"You gained {damage} sleepiness!")
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] + damage

        if player["stats"]["sleepiness"] >= player["statmax"]["sleepiness"]:
            contq = cont()
            if contq == True:
                history_t(player)
        if questions <= 0:
            print("you survived!")
            RW_route_parents(player)

def nan_fight(playerchar, nanlynan):
    charmcount = 0

    while True:
        if playerchar["stats"]["lucidity"] > playerchar["statmax"]["lucidity"]:
            contq = cont()
            if contq == True:
                update = playerregen(playerchar)
                playerchar = update
                return playerchar, False
    
        if charmcount >= nanlynan[1]:
            print("You won!")
            update = playerregen(playerchar)
            playerchar = update
            return playerchar, True

        print("You still need to convince Nan to let you sleep!") # lowkey make a flavor text randomizer here pls
        print("Use your CHARM to CHARM the enemy into letting you do what you want!")
        print(f"The charm gauge is currently at {charmcount}!")
        print(f"You currently have:")
        print(f"Lucidity:{playerchar["stats"]["lucidity"]}/{playerchar["statmax"]["lucidity"]}\nSocial Battery:{playerchar["stats"]["social battery"]}/{playerchar["statmax"]["social battery"]}")

        print("You can:\n1) Charm\n2) Use a Social Skill\n3) Use an item:\n")
        while True:
            turnchoice = inputchecker(3)
            if turnchoice == 1:
                charmcount += playerchar["miscish stats"]["charm"]
                print(f"You did {playerchar["miscish stats"]["charm"]} charm!")
                break
            elif turnchoice == 2:
                if "disassociate" in playerchar["skills"] or playerchar["stats"]["social battery"] >= 2:
                    DW_skills(charmcount, playerchar)
                    break
                else:
                    print("You don't even have enough adrenaline to use a single skill try something else!")
            elif turnchoice == 3:
                print("You don't have any items... hmm maybe you could convince someone to give you one?")
                time.sleep(2)
                print("Not Nan or Tun though, the creator was too lazy to give them item drops...")
        
        direction = random.randint(1, 2)
        change = random.randint(0, 5)

        if direction == 1:
            damage = nanlynan[0] + change
        elif direction == 2:
            damage = nanlynan[0] - change

        print(random.choice(nanlynan[2]))

        print(f"Your lucidity increased by {damage}!")
        playerchar["stats"]["lucidity"] = playerchar["stats"]["lucidity"] + damage

def combat(enemy, player):
    charmcount = 0
    disassociate = 0

    while True:
        if player["stats"]["lucidity"] >= player["statmax"]["lucidity"]:
            contq = cont()
            if contq == True:
                playerupdate = playerregen(player)
                player = playerupdate
                return "LOSS", player
        elif enemy[3] <= charmcount:
            player["battle"] = player["battles"].append(enemy[0])
            player["miscish stats"]["imagination"] = player["miscish stats"]["imagination"] + 1
            if player["miscish stats"]["imagination"]//3 == 1:
                playerupdate = levelup(player)
                player = playerupdate
                player["miscish stats"]["imagination"] = player["miscish stats"]["imagination"] - 3
            return "WIN", player
            
        print(f"The charm gauge is currently at {charmcount}/{enemy[1]}!")
        print(f"You currently have:")
        print(f"Lucidity:{player["stats"]["lucidity"]}/{player["statmax"]["lucidity"]}\nSocial Battery:{player["stats"]["social battery"]}/{player["statmax"]["social battery"]}")

        if disassociate <= 0:
            while True:
                print("Would you like to:\n1) Charm\n2) Use Skills\n3) Use Items")
                turnch = inputchecker(3)
                if turnch == 1:
                    print("You used your Charm on the enemy!")
                    charmcount += player["miscish stats"]["charm"]
                    break
                elif turnch == 2:
                    if "disassociate" in player["skills"] or player["stats"]["social battery"] >= 2:
                        skilly = DW_skills(charmcount, player)
                        charmcount = skilly[0]
                        player = skilly[1]
                        disassociate = skilly[2]
                        break
                    else:
                        print("You don't even have enough adrenaline to use a single skill try something else!")
                elif turnch == 3:
                    if player["inventory"]:
                        itemmy = DW_items(player)
                        player = itemmy
        else:
            print("You're still disassociating!")
        
        direction = random.randint(1, 2)
        change = random.randint(0, 3)

        if direction == 1:
            damage = enemy[1] + change
        elif direction == 2:
            damage = enemy[1] - change

        textrand(enemy[2])

        print(f"Your lucidity increased by {damage}!!")
        player["stats"]["lucidity"] = player["stats"]["lucidity"] + damage

def RW_route_parents(player):
    parents = [10, ["flavor text list"]]
    evidencegauge = 0
    arguloss = 0

    while True:
        player = playerregen(player)

        if arguloss >= 100:
            contq = cont()
            DW_route_parents(player)
        elif evidencegauge >= 100:
            completion()

        print("Would you like to:\n1) Use Memory")
        turnch = inputchecker(1)

        if turnch == 1 and player["stats"]["memory"] > 0:
            print("You tried to remember a good reason why they should buy you a car!")
            evidencegauge += player["stats"]["memory"]
        
        direction = random.randint(1, 2)
        change = random.randint(0, 3)

        if direction == 1:
            damage = parents[0] + change
        elif direction == 2:
            damage = parents[0] - change

        print(random.choice(parents[1]))

        print(f"The loss counter increased by {damage}!!")

def DW_route_parents(player):
    # WAITERRRR, flavor text please :)
    charmcounter = 0
    losscounter = 0
    disassociate = 0
    parents = [10, ["flavor text list"]]
    player = playerregen(player)

    while True:
        if losscounter >= 100:
            contq = cont()
            DW_route_parents(player)
        elif charmcounter >= 100:
            completion()
        
        if disassociate == 0:
            print("Would you like to:\n1) Charm\n2) Use Skills")
            turnch = inputchecker(2)

            if turnch == 1:
                print("You used your Charm on your parents!")
                charmcount += player["miscish stats"]["charm"]
            elif turnch == 2:
                skilly = DW_skills(charmcount, player)
                charmcount = skilly[0]
                player = skilly[1]
                disassociate = skilly[2]
        else:
            print("You are still disassociating!")
        
        direction = random.randint(1, 2)
        change = random.randint(0, 3)

        if direction == 1:
            damage = parents[0] + change
        elif direction == 2:
            damage = parents[0] - change

        print(random.choice(parents[1]))

        print(f"The loss counter increased by {damage}!!")

def levelup(player):
    print("You gained enough imagination to level up!")
    print("You will now get a random SKILL and a STAT BONUS of your choice")

    newskill = random.choice(list(player["unacquired skills"].keys()))
    player["skills"][newskill] = player["unacquired skills"][newskill]
    del player["unacquired skills"][newskill]

    print(f"You got the {newskill} skill!")
    print(f"{newskill}: {player["skills"][newskill]}")

    print("You may now choose a stat to upgrade by 10, 50 in the case of lucidity!")
    print("Would you like to upgrade your:\n1) Charm\n2) Social Battery\n3) Lucidity Cap")
    statinc = inputchecker(3)
        
    if statinc == 1:
        player["miscish stats"]["charm"] = player["miscish stats"]["charm"] + 10
        print(f"Your Charm increased by 5!")
    elif  statinc == 2:
        player["statmax"]["social battery"] = player["statmax"]["social battery"] + 10
    elif  statinc == 3:
        player["statmax"]["lucidity"] = player["statmax"]["lucidity"] + 50

    return player

def RW_items(queleft, player):
    # ADD FLAVOR TEXT
    count = 0
    for specitem in player["inventory"].keys():
        count += 1
        print(f"{count}) {specitem} : {player["inventory"][specitem]}")

    itemch = inputchecker(count)

    inventorylist = list(player["inventory"].keys())
    item = inventorylist[itemch-1]

    if item == "coffee":
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 10
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
        del player["inventory"][item]
            
    elif item == "energy drink":
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] + 2
        if player["stats"]["adrenaline"] > player["statmax"]["adrenaline"]:
            player["stats"]["adrenaline"] = player["statmax"]["adrenaline"]
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 15
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
        del player["inventory"][item]

    elif item == "candy bag":
        player["stats"]["memory"] = player["stats"]["memory"] + 3
        if player["stats"]["memory"] > player["statmax"]["memory"]:
            player["stats"]["memory"] = player["statmax"]["memory"]
        del player["inventory"][item]

    elif item == "burrito":
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] + 4
        if player["stats"]["adrenaline"] > player["statmax"]["adrenaline"]:
            player["stats"]["adrenaline"] = player["statmax"]["adrenaline"]
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 7
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
        del player["inventory"][item]

    elif item == "cheat sheet":
        caughtq = random.randint(1, 10)
        if caughtq == 1:
            print("You got caught! Whelp, guess you lost :c")
            player["stats"]["sleepiness"] = player["statmax"]["sleepiness"]
        else:
            damage = random.randint(5, 10)
            queleft = queleft - damage
    
    return queleft, player

def DW_items(player):
    # ADD FLAVOR TEXT
    count = 1
    for specitem in player["inventory"].keys():
        print(f"{count}) {specitem} : {player["inventory"][specitem]}")
        count += 1

    itemch = inputchecker(count-1)

    inventorylist = list(player["inventory"].keys())
    item = inventorylist[itemch-1]

    if item == "sleep tea":
        player["stats"]["lucidity"] = player["stats"]["lucidity"] - 10
        if player["stats"]["lucidity"] < 0:
            player["stats"]["lucidity"] = 0
        del player["inventory"][item]
            
    elif item == "big rock":
        player["stats"]["lucidity"] = player["stats"]["lucidity"] - 20
        if player["stats"]["lucidity"] < 0:
            player["stats"]["lucidity"] = 0
        del player["inventory"][item]

    elif item == "frying pan":
        player["stats"]["social battery"] = player["stats"]["social battery"] + 5
        if player["stats"]["social battery"] < player["statmax"]["social battery"]:
            player["stats"]["social battery"] = player["statmax"]["social battery"]
        del player["inventory"][item]
    elif item == "PSPC":
        player["stats"]["social battery"] = player["stats"]["social battery"] + 5
        if player["stats"]["social battery"] < player["statmax"]["social battery"]:
            player["stats"]["social battery"] = player["statmax"]["social battery"]
        del player["inventory"][item]
    
    return player

def RW_skills(queleft, player):
    # ADD FLAVOR TEXT!!!!!!
    count = 1
    for specskill in player["skills"].keys():
        print(f"{count}) {specskill} : {player["skills"][specskill]}")
        count += 1

    sklcho = inputchecker(count-1)

    skilllist = list(player["skills"].keys())
    skill = skilllist[sklcho-1]

    if skill == "random recollection" and player["stats"]["adrenaline"] >= 5:
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] - 5
        queleft = queleft - 10
    elif skill == "save the hardest for last" and player["stats"]["adrenaline"] >= 2:
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] - 2
        queleft = queleft - 3
    elif skill == "guess" and player["stats"]["adrenaline"] >= 2:
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] - 1
        queleft = queleft - 1
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 5
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
    elif skill == "slap" and player["stats"]["adrenaline"] >= 2:
        player["stats"]["adrenaline"] = player["stats"]["adrenaline"] - 2
        player["stats"]["sleepiness"] = player["stats"]["sleepiness"] - 15
        if player["stats"]["sleepiness"] < 0:
            player["stats"]["sleepiness"] = 0
        
    
    return queleft, player

def DW_skills(charmco, player):
    # ADD FLAVOR TEXT!!!!!!!!!!!1111!!!11!!!1!1
    count = 1
    dissassociate = 0
    for specskill in player["skills"].keys():
        print(f"{count}) {specskill} : {player["skills"][specskill]}")
        count += 1

    sklcho = inputchecker(count-1)

    skilllist = list(player["skills"].keys())
    skill = skilllist[sklcho-1]

    if skill == "dramatic lie" and player["stats"]["social battery"] >= 10:
        player["stats"]["social battery"] = player["stats"]["social battery"] - 10
        charmco = charmco + 30
    elif skill == "puppy dog eyes" and player["stats"]["social battery"] >= 2:
        player["stats"]["social battery"] = player["stats"]["social battery"] - 2
        charmco = charmco + 7
    elif skill == "disassociate":
        dissassociate = dissassociate + 1
        player["stats"]["social battery"] = player["stats"]["social battery"] + 3
        if player["stats"]["social battery"] < player["statmax"]["social battery"]:
            player["stats"]["social battery"] = player["statmax"]["social battery"]
    elif skill == "pretend nap" and player["stats"]["social battery"] >= 2:
        player["stats"]["social battery"] = player["stats"]["social battery"] - 2
        player["stats"]["lucidity"] = player["stats"]["lucidity"] - 15
        if player["stats"]["lucidity"] < 0:
            player["stats"]["lucidity"] = 0
    
    return charmco, player, dissassociate

def playerregen(player):
    for stat in player["stats"]:
        player["stats"][stat] = player["statmax"][stat]
    if "sleepiness" in player["stats"]:
        player["stats"]["sleepiness"] = 0
    if "lucidity" in player["stats"]:
        player["stats"]["lucidity"] = 0
    return player

def cont():
    print("You unfortunately failed...")
    while True:
        contq = input("Will you try again?Y/N")
        if contq == "Y":
            print("Very well, you decided to perservere.")
            return True
        elif contq == "N":
            print("Ok then, unfortunately, you rage quitted.")
            sys.exit()
        else:
            print("Sorry, is that an option I gave you?")

def completion():
    # Make COOLER please :)
    print("WOW! You made it all the way to the end and got your car!")
    while True:
        restart = input("Would you like to play from the beginning all over again?(Y/N)")
        if restart == "Y":
            intro()
        elif restart == "N":
            print("Insert REALLY cool credits here:")
        else:
            print("What? Can you say that again? I don't think that was the letter Y OR N...")

def intro():
    count = 0
    print("Hello, this is a TBAG--Text Based Adventure Game. (insert better intro text here)")
    while True:
        if count < 10:
            start = input("Would you like to play?(Y/N):\n")
        elif count > 10:
            start = input("CHOOSE A VALID OPTION ALREADY PLEASE!:\n")
            if count > 30:
                print("Right so you didn't choose for too many times so I'm just going to terminate the program for you.")
                sys.exit()
        if start == "Y":
            startup_room()
        elif start == "N":
            sys.exit()
        else:
            count += 1
            continue

def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices})")
            try:
                choicevar = int(choicevar)
                if choicevar in range(1, rangeofchoices+1):
                    break
                else:
                    print("That's not an option :(")
                    continue
            except:
                    continue
            
    return choicevar

def textrand(textlist):
    print(random.choice(textlist))

intro()