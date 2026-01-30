def editcharacters(database):
    print("Which character would you like to edit?")
    for i, character in enumerate(database.keys()):
        print(f"{i+1}. {character}")
    choice = int(input("Enter the number of the character you want to edit: ")) - 1
    character_name = list(database.keys())[choice]
    while True:
        print(f"Editing {character_name}")
        print("1. Edit Skills")
        print("2. Edit Inventory")
        print("3. Return to Main Menu")
        action = input("Choose an option: ").strip()
        if action == "1":
            EditSkills(database, character_name)
        elif action == "2":
            inventory_management(database, character_name, database[character_name]["simpleinfo"][1])
        elif action == "3":
            break
        else:
            print("Invalid option.")

def EditSkills(database, character_name):
        action = input("Would you like to add or remove a skill? ").lower().strip()
        if action == "add":
            skillname = input("Enter the name of the skill you want to add: ").capitalize().strip()
            skilldesc = input("Enter a description for the skill: ").strip()
            database[character_name]["skills"].add((skillname, skilldesc))
            print(f"Skill '{skillname}' has been added.")
                
        elif action == "remove":
            for i in database[character_name]["skills"]:
                print(f"- {i[0]}")
            skillToRemove = input("Enter the name of the skill you want to remove: ").capitalize().strip()
            skill_to_remove = next((skill for skill in database[character_name]["skills"] if skill[0] == skillToRemove), None)
            if skill_to_remove:
                database[character_name]["skills"].remove(skill_to_remove)
                print(f"Skill '{skillToRemove}' has been removed.")
            else:
                print(f"Skill '{skillToRemove}' not found in your skills.")


def inventory_management(database, character_name, player_class):
    Items_Dictonaties = database[character_name]["Items_Dictionary"]
    print(f"Your charaters weapon is a {Items_Dictonaties["Weapon"][0]}")
    print(f"Your charaters is wearing {Items_Dictonaties["Armor"][0]} ")
    print(f"This is your inventory:")
    val = 0
    for x in Items_Dictonaties["Inventory"]:
        val += 1
        if val == 1:
            print(x)
        if val == 3:
            val = 0
    Player_answer = input("Would you like to Edit you inventory(1.Yes 2.No):").capitalize().strip()
    if Player_answer == "1" or Player_answer == "Yes":
        asking = True
        while asking:
            players_selected_action = input("Would you like to (1.edit your inventory 2.Add a item to your inventory 3.To exit):").capitalize().strip()
            if players_selected_action == "1":
                answering = True
                while answering:
                    for x in Items_Dictonaties["Inventory"]:
                        val += 1
                        if val == 1:
                            print(x)
                        if val == 3:
                            val = 0
                    Edit_item = input("What item in your inventory do you want to edit:").capitalize().strip()
                    if Edit_item in Items_Dictonaties["Inventory"]:
                        Item_index = Items_Dictonaties["Inventory"].index(Edit_item)
                        Item_slot = Items_Dictonaties["Inventory"][Item_index + 1]
                        Item_class = Items_Dictonaties["Inventory"][Item_index + 2]
                        if Item_class == player_class or Item_class == "None":
                            for x in range(0,3):
                                    Items_Dictonaties["Inventory"].pop(Item_index) 
                            for x in range(0,3):
                                if Items_Dictonaties[Item_slot][0] != "None":
                                    Items_Dictonaties["Inventory"].append(Items_Dictonaties[Item_slot][x]) 
                            Items_Dictonaties[Item_slot] = [Edit_item,Item_slot,Item_class]
                            print(f"Your charaters weapon is a {Items_Dictonaties["Weapon"][0]}")
                            print(f"Your charaters is wearing {Items_Dictonaties["Armor"][0]} ")
                            print(f"This is your inventory:")
                            val = 0
                            for x in Items_Dictonaties["Inventory"]:
                                val += 1
                                if val == 1:
                                    print(f"- {x}")
                                if val == 3:
                                    val = 0
                            answering = False
                        else:
                            print(f"Your charater class is incorect. you need to be a {Item_class}, but you are a {player_class}")
                    else:
                        print("that is not an item in your inventory")
            if players_selected_action == "2":
                player_item_name = input("What is the name of the item:").capitalize().strip()
                Items_Dictonaties["Inventory"].append(player_item_name)
                player_item_slot = input("What is the slot of the item(Inventory,Weapon,Armor):").capitalize().strip()
                Items_Dictonaties["Inventory"].append(player_item_slot)
                player_item_class = input("What is the required class of the item(If no required one then type None):").capitalize().strip()
                Items_Dictonaties["Inventory"].append(player_item_class)
                for x in Items_Dictonaties["Inventory"]:
                        val += 1
                        if val == 1:
                            print(x)
                        if val == 3:
                            val = 0
            if players_selected_action == "3":
                asking = False


def editing(database, character_name):


    def displaystat(num):
        oldstat = database[character_name]["attributes"][1][num]
        try:
            database[character_name]["attributes"][1][num] = int(newStatValue)
        except ValueError:
            database[character_name]["attributes"][1][num] = newStatValue
        print(f"{statToEdit.capitalize()} has been updated from {oldstat} to {database[character_name]["attributes"][1][num]}.")

    while True:
        editC = input("Are you editing  1. Stats, 2. Skills, or 3. Inventory, or do you want to  4. quit:  ").lower().strip()
        if editC == "stats" or editC == "1":
            changableStats = database[character_name]["attributes"][0]
            print("available stats are as follows")
            for x in changableStats:
                print (f" - {x}")
            statToEdit = input("Which stat would you like to edit? ").lower().strip()
            if statToEdit in changableStats or statToEdit in [s[:3] for s in changableStats]:
                newStatValue = input(f"What would you like to change {statToEdit} to? ").strip()

                    
                match statToEdit:
                    case "strength" | "str":
                        displaystat(0)
                    case "dexterity" | "dex":
                        displaystat(1)
                    case "constitution" | "con":
                        displaystat(2)
                    case "intelligence" | "int":
                        displaystat(3)
                    case "wisdom" | "wis":
                        displaystat(4)
                    case "charisma" | "cha":
                        displaystat(5)
                    case "health" | "hel":
                        displaystat(6)
                    case "armor class" | "ac":
                        displaystat(7)
            else:
                print("Invalid stat name. Please try again.")


        elif editC == "skills" or editC == "2":
            EditSkills(database, character_name)
        elif editC == "inventory" or editC == "3":
            inventory_management(database, character_name, "None")
        else:
            break