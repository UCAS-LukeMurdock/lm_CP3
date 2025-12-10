#RC, 1st, Final game

import random


#set the list for beaten people
beaten = []
#set stat dictionary that will hold win lose and gold as well
stat = { "Charm": 8,
      "Wisdom": 8,
      "Strength": 8,
      "Roll": 2,
      "Win": 0,
      "Loss": 0,
      "Gold": 0,
      "Used": []}
#Set functions

# 1st function
#def stat_increase(stat, gain):
def stat_increase(stat, gain):
    #Create the stat gains for crocs, nerdy_glasses, and Suit. the first item.
    #Make sure that they must have gold and that we return new stats.
    if gain == "Crocs" and stat["Gold"] > 1 and gain not in stat["Used"]:
        stat["Charm"] -= 2
        stat["Wisdom"] -= 2
        stat["Strength"] += 4
        stat["Gold"] -=2
        stat["Used"].append(gain)
        return stat
    elif gain == "Nerdy Glasses" and stat["Gold"] > 1 and gain not in stat["Used"]:
        stat["Charm"] -= 2
        stat["Wisdom"] += 4
        stat["Strength"] -= 2
        stat["Gold"] -=2
        stat["Used"].append(gain)
        return stat
    elif gain == "Suit" and stat["Gold"] > 1 and gain not in stat["Used"]:
        stat["Charm"] += 4
        stat["Wisdom"] -= 2
        stat["Strength"] -= 2
        stat["Gold"] -=2
        stat["Used"].append(gain)
        return stat
    elif gain == "Dice" and stat["Gold"] > 1 and gain not in stat["Used"]:
        stat["Roll"] += 1
        stat["Gold"] -=2
        stat["Used"].append(gain)
        return stat
    elif gain == "Charm" and stat["Gold"] > 1:
        stat["Charm"] += 2
        stat["Gold"] -= 2
        return stat
    elif gain == "Wisdom" and stat["Gold"] > 1:
        stat["Wisdom"] += 2
        stat["Gold"] -= 2
        return stat
    elif gain == "Strength" and stat["Gold"] > 1:
        stat["Strength"] += 2
        stat["Gold"] -= 2
        return stat
    else:
        print("\nYou don't have enough money or its an already chosen item...")
        return stat

# 2nd function
#def lose(stat):
def lose(stat):
    #If your lose stats are greater than 3, return true to end the game
    if stat["Loss"] >= 3:
        return True
    #else:
    else:
        #return false and keep the game going.
        return False

# 3rd function
#def fight_room(stat, room)
def fight_room(stat,room,beaten):
    finished_game = False
    failed = False
    #if room == 1:
    if room == 1:
        #ask them if they want to by an upgrade/item
        yes = input("Would you like to purchase an item or a upgrade? If you do put Yes, else put No").strip().capitalize()
        if yes == "Yes":
            while True:
                gain = input("What would you like to buy? \nCrocs: +4 to strength, -2 to wisdom,-2 charm \nNerdy Glasses: +4 wisdom, -2 charm, -2 strength \nSuit: +4 charm, -2 wisdom, -2 strength \nDice: This adds one to your roll. This upgrade increase your chance of being chosen to pick the stat to fight with from 1/2 to 2/3\nYou can also purchase basic increases to eather Charm, Wisdom, or Strength that each +2 to their respective stat and don't give any decreases. (All items and stat increases cost two gold, if you don't have enough you just won" \
                "t get the item (You also won't lose your gold...))").strip().capitalize()
                if gain == "Crocs" or gain == "Nerdy Glasses" or gain == "Suit" or gain == "Dice" or gain == "Charm" or gain == "Strength" or gain == "Wisdom":
                    break
                else:
                    print("That is not a valid option...")
            stat_increase(stat, gain)
        #def stat_increase

        #Make sure not to allow them to buy the stats multiple times.
    #elif room == 2:
    elif room == 2:
        #if room isn't in beaten list:
        if 2 not in beaten:
            print("\nNerd - So I see you have come to fight, well I hope your calculashions were correct!")
            #write out all of the enemy stats here.
            b_strength = 5; b_wisdom = 10; b_charm = 2
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                #Roll for who gets to decide the attack.
                choice = random.randint(1,stat["Roll"])
                #if choice = 1:
                if choice == 1:
                    #set attack to the bots strongest
                    attack = "Wisdom"
                    chain = b_wisdom
                    print(f"The bot got chosen to pick, and he picked {attack}!")
                #else:
                else:
                    #While True:
                    while True:
                        #Ask the user what stat they would like to use.
                        attack = input("\nWhat stat would you like to attack with? Wisdom, Strength, or Charm?\n").strip().capitalize()
                        #check if its one of the three actual stats.
                        if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                            #Break to get out of loop
                            break
                        #Else:
                        else:
                            #tell them its not a choice
                            print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                print(f"The bot scored a {bot_roll} and you scored a {human_roll}")
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you have more aura!!!")
                #if you win, add gold and one win to your stats as well as adding the room to the beaten list                   
                    stat["Win"] += 1
                    stat["Gold"] +=1
                    beaten.append(room)
                    break
                #else and one loss to your stats and add the room to the 'beaten' list
                elif t_loss >= 3:
                    print("You did not have enough arua to vanquish the foe. In fact, your arua has gone down from loseing.")
                    stat["Loss"] += 1
                    beaten.append(room)
                    break
        #else:
        else:
            #Print of thing telling the person this room has already been concured or that the number is to high
            print("The battle has been fought and the winner has already been decided. There is nothing left to do here...")

    elif room == 3:
        #if room isn't in beaten list:
        if 3 not in beaten:
            #write out all of the enemy stats here.
            print("\nJock - Quite bold of you to come here, after all it is my home court!")
            b_strength = 11; b_wisdom = 4; b_charm = 7
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                #Roll for who gets to decide the attack.
                choice = random.randint(1,stat["Roll"])
                #if choice = 1:
                if choice == 1:
                    #set attack to the bots strongest
                    attack = "Strength"
                    chain = b_strength
                    print(f"The bot got chosen to pick, and he picked {attack}!")
                #else:
                else:
                    #While True:
                    while True:
                        #Ask the user what stat they would like to use.
                        attack = input("\nWhat stat would you like to attack with? Wisdom, Strength, or Charm?\n").strip().capitalize()
                        #check if its one of the three actual stats.
                        if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                            #Break to get out of loop
                            break
                        #Else:
                        else:
                            #tell them its not a choice
                            print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                print(f"The bot scored a {bot_roll} and you scored a {human_roll}")
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you have more aura!!!")
                #if you win, add gold and one win to your stats as well as adding the room to the beaten list                   
                    stat["Win"] += 1
                    stat["Gold"] +=1
                    beaten.append(room)
                    break
                #else and one loss to your stats and add the room to the 'beaten' list
                elif t_loss >= 3:
                    print("You did not have enough arua to vanquish the foe. In fact, your arua has gone down from loseing.")
                    stat["Loss"] += 1
                    beaten.append(room)
                    break
        #else:
        else:
            #Print of thing telling the person this room has already been concured or that the number is to high
            print("The battle has been fought and the winner has already been decided. There is nothing left to do here...")

    elif room == 4:
        #if room isn't in beaten list:
        if 4 not in beaten:
            print("\nClown - Hey were does the president keep his armies? 'hehe' In his sleevies... Come'on that was a good one, at least give me a little chuckle.")
            #write out all of the enemy stats here.
            b_strength = 6; b_wisdom = 10; b_charm = 9
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                #Roll for who gets to decide the attack.
                choice = random.randint(1,stat["Roll"])
                #if choice = 1:
                if choice == 1:
                    #set attack to the bots strongest
                    attack = "Wisdom"
                    chain = b_wisdom
                    print(f"The bot got chosen to pick, and he picked {attack}!")
                #else:
                else:
                    #While True:
                    while True:
                        #Ask the user what stat they would like to use.
                        attack = input("\nWhat stat would you like to attack with? Wisdom, Strength, or Charm?\n").strip().capitalize()
                        #check if its one of the three actual stats.
                        if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                            #Break to get out of loop
                            break
                        #Else:
                        else:
                            #tell them its not a choice
                            print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                print(f"The bot scored a {bot_roll} and you scored a {human_roll}")
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you have more aura!!!")
                #if you win, add gold and one win to your stats as well as adding the room to the beaten list                   
                    stat["Win"] += 1
                    stat["Gold"] +=1
                    beaten.append(room)
                    break
                #else and one loss to your stats and add the room to the 'beaten' list
                elif t_loss >= 3:
                    print("You did not have enough arua to vanquish the foe. In fact, your arua has gone down from loseing.")
                    stat["Loss"] += 1
                    beaten.append(room)
                    break
        #else:
        else:
            #Print of thing telling the person this room has already been concured or that the number is to high
            print("The battle has been fought and the winner has already been decided. There is nothing left to do here...")

    elif room == 5:
        #if room isn't in beaten list:
        if 5 not in beaten:
            print("Slacker - Buzz off! Unless you here to trade...")
            #write out all of the enemy stats here.
            b_strength = 10; b_wisdom = 7; b_charm = 7
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                #Roll for who gets to decide the attack.
                choice = random.randint(1,stat["Roll"])
                #if choice = 1:ss
                if choice == 1:
                    #set attack to the bots strongest
                    attack = "Strength"
                    chain = b_strength
                    print(f"The bot got chosen to pick, and he picked {attack}!")
                #else:
                else:
                    #While True:
                    while True:
                        #Ask the user what stat they would like to use.
                        attack = input("\nWhat stat would you like to attack with? Wisdom, Strength, or Charm?\n").strip().capitalize()
                        #check if its one of the three actual stats.
                        if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                            #Break to get out of loop
                            break
                        #Else:
                        else:
                            #tell them its not a choice
                            print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                print(f"The bot scored a {bot_roll} and you scored a {human_roll}")
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you have more aura!!!")
                #if you win, add gold and one win to your stats as well as adding the room to the beaten list                   
                    stat["Win"] += 1
                    stat["Gold"] +=1
                    beaten.append(room)
                    break
                #else and one loss to your stats and add the room to the 'beaten' list
                elif t_loss >= 3:
                    print("You did not have enough arua to vanquish the foe. In fact, your arua has gone down from loseing.")
                    stat["Loss"] += 1
                    beaten.append(room)
                    break
        #else:
        else:
            #Print of thing telling the person this room has already been concured or that the number is to high
            print("The battle has been fought and the winner has already been decided. There is nothing left to do here...")

    elif room == 6:
        #if room isn't in beaten list:
        if 6 not in beaten:
            print("Chill guy - You don't need to do this... Can't we all just be friends?")
            #write out all of the enemy stats here.
            b_strength = 8; b_wisdom = 8; b_charm = 8
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                while True:
                    #Talk about how chill the guy is
                    print("The chill guy is so chill, he lets you pick what to attack with. Your a monster for hurting someone who has done no wrong, he's just a chill guy!!!")
                    #Ask the user what stat they would like to use.
                    attack = input("What stat would you like to attack with (You monster!)? Wisdom, Strength, or Charm?").strip().capitalize()
                    #check if its one of the three actual stats.
                    if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                        #Break to get out of loop
                        break
                    #Else:
                    else:
                        #tell them its not a choice
                        print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                print(f"The bot scored a {bot_roll} and you scored a {human_roll}")
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you have more aura!!!")
                #if you win, add gold and one win to your stats as well as adding the room to the beaten list                   
                    stat["Win"] += 1
                    stat["Gold"] +=1
                    beaten.append(room)
                    print("Chill guy - What did I ever do to you..?")
                    break
                #else and one loss to your stats and add the room to the 'beaten' list
                elif t_loss >= 3:
                    print("He was to chill for you >:)")
                    stat["Loss"] += 1
                    beaten.append(room)
                    break
        #else:
        else:
            #Print of thing telling the person this room has already been concured or that the number is to high
            print("You already tried hurting the chill guy... you monster... theres no longer a chill guy here.")

    elif room == 7:
        #if room isn't in beaten list:
        if 7 not in beaten:
            print("Actor - 'Hide not thy poison with such sugar'd words; Lay not thy hands on me; forbear, I say! Their touch affrights me as a serpent's sting.'")
            #write out all of the enemy stats here.
            b_strength = 6; b_wisdom = 9; b_charm = 10
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                #Roll for who gets to decide the attack.
                choice = random.randint(1,stat["Roll"])
                #if choice = 1:
                if choice == 1:
                    #set attack to the bots strongest
                    attack = "Charm"
                    chain = b_charm
                    print(f"The bot got chosen to pick, and he picked {attack}!")
                #else:
                else:
                    #While True:
                    while True:
                        #Ask the user what stat they would like to use.
                        attack = input("\nWhat stat would you like to attack with? Wisdom, Strength, or Charm?\n").strip().capitalize()
                        #check if its one of the three actual stats.
                        if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                            #Break to get out of loop
                            break
                        #Else:
                        else:
                            #tell them its not a choice
                            print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                print(f"The bot scored a {bot_roll} and you scored a {human_roll}")
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you have more aura!!!")
                #if you win, add gold and one win to your stats as well as adding the room to the beaten list                   
                    stat["Win"] += 1
                    stat["Gold"] +=1
                    beaten.append(room)
                    break
                #else and one loss to your stats and add the room to the 'beaten' list
                elif t_loss >= 3:
                    print("You did not have enough arua to vanquish the foe. In fact, your arua has gone down from loseing.")
                    stat["Loss"] += 1
                    beaten.append(room)
                    break
        #else:
    

        else:
            #Print of thing telling the person this room has already been concured or that the number is to high
            print("The battle has been fought and the winner has already been decided. There is nothing left to do here...")
    
    elif room == 8:
        print("Bully - Heh, finally got enough courage to stand up to me? Probably just stupiditiy!")
        #if room isn't in beaten list:
        if 8 not in beaten:
            #write out all of the enemy stats here.
            b_strength = 12; b_wisdom = 5; b_charm = 4
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                #Roll for who gets to decide the attack.
                choice = random.randint(1,stat["Roll"])
                #if choice = 1:
                if choice == 1:
                    #set attack to the bots strongest
                    attack = "Strength"
                    chain = b_strength
                    print(f"The bot got chosen to pick, and he picked {attack}!")
                #else:
                else:
                    #While True:
                    while True:
                        #Ask the user what stat they would like to use.
                        attack = input("\nWhat stat would you like to attack with? Wisdom, Strength, or Charm?\n").strip().capitalize()
                        #check if its one of the three actual stats.
                        if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                            #Break to get out of loop
                            break
                        #Else:
                        else:
                            #tell them its not a choice
                            print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                print(f"The bot scored a {bot_roll} and you scored a {human_roll}")
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you have more aura!!!")
                #if you win, add gold and one win to your stats as well as adding the room to the beaten list                   
                    stat["Win"] += 1
                    stat["Gold"] +=1
                    beaten.append(room)
                    break
                #else and one loss to your stats and add the room to the 'beaten' list
                elif t_loss >= 3:
                    print("You did not have enough arua to vanquish the foe. In fact, your arua has gone down from loseing.")
                    stat["Loss"] += 1
                    beaten.append(room)
                    break
        #else:
    

        else:
            #Print of thing telling the person this room has already been concured or that the number is to high
            print("The battle has been fought and the winner has already been decided. There is nothing left to do here...")

    elif room == 9:
        #if room isn't in beaten list:
        if stat["Win"] >= 2:
            print("Student council president - I've been expecting you... now, show me why you should be the main character!!!")
            #write out all of the enemy stats here.
            b_strength = 10; b_wisdom = 14; b_charm = 12
            #Set base wins and losses to 0 as variables
            t_win = 0
            t_loss = 0
            #While True:
            while True:
                #Roll for who gets to decide the attack.
                choice = random.randint(1,stat["Roll"])
                #if choice = 1:
                if choice == 1:
                    #set attack to the bots strongest
                    attack = "Wisdom"
                    chain = b_wisdom
                    print(f"The bot got chosen to pick, and he picked {attack}!")
                #else:
                else:
                    #While True:
                    while True:
                        #Ask the user what stat they would like to use.
                        attack = input("\nWhat stat would you like to attack with? Wisdom, Strength, or Charm?\n").strip().capitalize()
                        #check if its one of the three actual stats.
                        if attack == "Wisdom" or attack == "Strength" or attack == "Charm":
                            #Break to get out of loop
                            break
                        #Else:
                        else:
                            #tell them its not a choice
                            print("That is not a choice...")

                #Set up bots stats for when the user picks the choice
                if attack == "Wisdom":
                    chain = b_wisdom
                elif attack == "Strength":
                    chain = b_strength
                else:
                    chain = b_charm

                #Set up the rolls based on the random library and the max is there stat.
                human_roll = random.randint(1, stat[attack])
                bot_roll = random.randint(1, chain)
                #Check to see which is greater and then add the win or loss.
                print(f"The bot scored a {bot_roll} and you scored a {human_roll}")
                if human_roll >bot_roll:
                    print("You have gained a point!")
                    t_win += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                elif bot_roll > human_roll:
                    print("You have sadly gained one loss...")
                    t_loss += 1
                    print(f"Your wins are: {t_win} \nYour losses are: {t_loss}")
                else:
                    print("It's a tie!!!")
                #Check to see if the round was one or lost by using t_wins and t_loss variables
                if t_win >= 3:
                    print("You have vanquished your foe, and now you are the main character!!! But at what cost...")
                    finished_game = True
                    beaten.append(room)
                    break
                #else and one loss to your stats and add the room to the 'beaten' list
                elif t_loss >= 3:
                    print("You did not have enough arua to vanquish the foe. In fact, your arua has gone down so much from loseing that you are being expelled. It's game over...")
                    failed = True
                    beaten.append(room)
                    break
        else:
            #CHeck to see if its number nine.
            print("You have not won enough battles to face off against the student council president... Come back when you have at least beaten two other enemies.")
    return stat, beaten, finished_game, failed

finished_game = False
failed = False
#Make a loop to go through the game
while True:
    if finished_game == True or failed == True:
        break
    #set the list for beaten people
    beaten = []
    #set stat dictionary that will hold win lose and gold as well
    stat = {"Charm": 9,
            "Wisdom": 9,
            "Strength": 9,
            "Roll": 2,
            "Win": 0,
            "Loss": 0,
            "Gold": 0,
            "Used": []}
    print("\nIn this game you have been reincarnated back to high school, but theres just one problem... You are a worthless side character who doesn't get anyone!:( With the realization of this you have begone on your journey to defeat the nobles, (people who are actually cool in their feild), and eventually defeat the final boss (Student concil presedent aka the main character) to becoming the main character. You will need to imploy your 3 main stats: Wisdom, Charm, and Strength to battle the enemy, be carefull though, because you will not always chose what stat to attack with. I wish you luck in your journey to become someone your mother would be proud of, but with your looks, brains, and charm that might be a bit hard...")
    while finished_game == False and failed == False:
    #while game_finished == Fales and failed == False (These are all of the different ways to win or lose.)
        check = lose(stat)
        #Check to see if they have lost to many times to continue to fight, if they have, exit the loop.
        if check == True:
            print("\nYou have failed in your conquest by failing to weak enemies to much. You will always be a lonely side character... (maybe)")
            break
        else:
            pass
        #Print a list of room numbers and there base purposes
        print("\nHere are all of your stats:")
        for key, value in stat.items():
            if isinstance(value, list):
                print(f"{key}: {', '.join(map(str, value))}")
            else:
                print(f"{key}: {value}")
        print(f"\nThere are 9 rooms you can go to. \n1. Dorms: This is were you will spend your gold from your hard earned wins to buy stat increases or there are our gucci items. Everything costs 2 gold, you have {stat['Gold']} gold. \n2. Computer lab: contains the nerd enemy \n3. Gym: Contains the Jock enemy. \n4. Lunchroom: contains class clown enemy. \n5. Bathroom: contains the slacker enemy. \n6. Hallway: contains THE CHILL GUY (Don't even think about fighting him). \n7. Auditorium: contains the actor enemy. \n8. Principle's office: contains the bully enemy. \n9. Student counsel room: Contains the final boss called, 'The Student Council President' or the MAIN CHARACTER. To fight him you must beat at least two others first.")
        print("\nThe rooms that have already been visited are:")
        beaten.sort()
        print(*beaten, sep=', ')
        #While true loop for room picking
        while True:
            #Ask them what room they want to go into.
            room = input("\nWhat room would you like to go to? (1-9)").strip()
            if room.isdigit() == False or int(room) > 9:
                print("That is not a number/option available...")
            else:
                room = int(room)
                break
        #Run the fight function as well as the lose function to start the game.
        stat, beaten, finished_game, failed = fight_room(stat,room,beaten)
    begin_again = input("\nWould you like to reincarnate and restart? if you do please type Yes, otherwise put No.").strip().capitalize()
    if begin_again == "Yes":
        finished_game = False; failed = False
        ("\nThe journey is being repeated... good luck...")
    else:
        break