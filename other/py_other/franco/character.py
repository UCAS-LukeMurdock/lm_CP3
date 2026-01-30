# FB 1st Character manager
import sys
from support1 import editcharacters

def validate_input(text, kind='int'):
    s = str(text).strip().capitalize()
    if kind == 'int':
        try:
            int(s)
            return True
        except ValueError:
            return False
    elif kind == 'float':
        try:
            float(s)
            return True
        except ValueError:
            return False
    elif kind == 'alpha':
        return s.isalpha()
    else:
        return False
    
def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices}):\n").strip().capitalize()
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

def viewchars(data):
    characterkeys = data.keys()
    characternameandlistnum = {}

    count = 1
    for character in characterkeys:
        characternameandlistnum[count] = character
        char_race = data[character]["simpleinfo"][0]
        char_class = data[character]["simpleinfo"][1]
        char_level = data[character]["simpleinfo"][2]
        print(f"{count}. {character} : {char_race}, {char_class}, {char_level}")
        count += 1

    print("Would you like to:\n1. Select\n2. Sort\n3. Main menu")

    choice = inputchecker(3)
    
    match choice:
        case 1:
            select(data,characternameandlistnum)
        case 2:
            sortchoice(data)
        case 3:
            mainmenu(data)

def select(data, selectionmenu):
    print("Which character do you want to select? (Refer to the list above)")

    characternum = inputchecker(len(selectionmenu))
    character = selectionmenu[characternum]

    char_race = data[character]["simpleinfo"][0]
    char_class = data[character]["simpleinfo"][1]
    char_level = data[character]["simpleinfo"][2]
    print(f"{character} : {char_race}, {char_class}, {char_level}")

    for itemslot in data[character]["Items_Dictionary"].keys():
        item = data[character]["Items_Dictionary"][itemslot]

        try:
            print(f"{itemslot} : {item[0]} it is a {item[1]}, and {item[2]} can use it!")
        except:
            continue

    for skill in data[character]["skills"]:
        print(f"{skill[0]} it {skill[1]}")
    
    count = 0
    for attribute in data[character]["attributes"][0]:
        attr_value = data[character]["attributes"][1][count]
        print(f"{attribute} : {attr_value}")
        count += 1

    print("Would you like to:\n1. edit\n2. main menu?")

    answer = inputchecker(2)

    match answer:
        case 1:
            editcharacters(data)
        case 2:
            mainmenu(data)

def sortoptions(data, typeindex):
    characternames = data.keys()
    previoustypes = []
    typelist = {}

    count = 1
    for character in characternames:

        if data[character]["simpleinfo"][typeindex] not in previoustypes:
            previoustypes.append(data[character]["simpleinfo"][typeindex])
            print(f"{count}. {data[character]["simpleinfo"][typeindex]}")
            typelist[count] = data[character]["simpleinfo"][typeindex]
            count += 1
    
    return typelist

def sorter(data, choice, types, typeindex):
    characterkeys = data.keys()
    characternameandlistnum = {}

    count = 1
    for character in characterkeys:
        if data[character]["simpleinfo"][typeindex] == types[choice]:
            characternameandlistnum[count] = character

            print(f"{count}. {character} : {database[character]["simpleinfo"][0]}, {database[character]["simpleinfo"][1]}, {database[character]["simpleinfo"][2]}")
            count += 1

    print("Would you like to:\n1. Select\n2. Main menu")

    choice = inputchecker(2)

    match choice:
        case 1:
            select(data, characternameandlistnum)

def sortchoice(data):
    print("Will sort by:\n1. Race\n2. Class\n3. Level")

    sortchoice = inputchecker(3)

    match sortchoice:
        case 1:
            distinct = sortoptions(data, 0)
            choice = inputchecker(len(distinct))
            typeindex = 0
        case 2:
            distinct = sortoptions(data, 1)
            choice = inputchecker(len(distinct))
            typeindex = 1
        case 3:
            distinct = sortoptions(data, 2)
            choice = inputchecker(len(distinct))
            typeindex = 2
    
    sorter(data, choice, distinct, typeindex)

def createcharacters(data):
    while True:
        charactername = input("What is the name of this character?")

        if charactername not in data.keys():
            break
    
    characterrace = input("What is the race of this character?")
    characterclass = input("What is the class of this character?")
    characterlevel = input("What is the level of the characters?")

    attributeslist = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma", "health", "armor class"]
    attributesscores = []

    for attribute in attributeslist:
        while True:
            attributepoint = input(f"What is the {attribute} score of this character? ")

            if validate_input(attributepoint, 'int'):
                attributesscores.append(int(attributepoint))
                break
            else:
                print("Please enter a valid integer value.")
                continue
    
    specificdata = {charactername:{
        "simpleinfo":[characterrace, characterclass, int(characterlevel)],
        "Items_Dictionary": {"Weapon": ["None", "Weapon", "None"], "Armor": ["None", "Armor", "None"], "Inventory": []},
        "skills": set(),
        "attributes": [attributeslist, attributesscores]
    }}

    data.update(specificdata)
    mainmenu(data)
    
def mainmenu(database):
    while True:
        print("You may:\n1. View Characters\n2. Create Character\n3. edit characters\n4. Exit")

        functionchoice = inputchecker(4)
        if functionchoice == 1:
            print("\n")
            viewchars(database)
        elif functionchoice == 2:
            createcharacters(database)
        elif functionchoice == 3:
            editcharacters(database)
        else:
            sys.exit()


if __name__ == "__main__":
    print("Hello! This is a simple character management software")
    from main1 import database
    mainmenu(database)