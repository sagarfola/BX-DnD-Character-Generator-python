import random
import csv

print("Welcome to Sean's B/X Dungeons and Dragons Character Generator")
input("Let's roll your stats first. Press ENTER to continue")


# Stat Roller
# Rolls 3d6 in order for STR, INT, WIS, DEX, CON, and CHA
def roll_stats():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    dice_roll = [a, b, c]
    add = sum(dice_roll[0:])
    return add


# Ability modifiers
mel_atk_mod = 0
stuckdoor = 2


def str_mod():
    global mel_atk_mod, stuckdoor
    if strength > 17:
        mel_atk_mod = mel_atk_mod + 3
        stuckdoor = stuckdoor + 3
        a = "| Add " + str(mel_atk_mod) + " to melee attacks and damage. " + str(
            stuckdoor) + "-in-6 chance to open stuck doors"
        return a
    elif 17 >= strength > 15:
        mel_atk_mod = mel_atk_mod + 2
        stuckdoor = stuckdoor + 2
        a = "| Add " + str(mel_atk_mod) + " to melee attacks and damage. " + str(
            stuckdoor) + "-in-6 chance to open stuck doors"
        return a
    elif 15 >= strength > 12:
        mel_atk_mod = mel_atk_mod + 1
        stuckdoor = stuckdoor + 1
        a = "| Add " + str(mel_atk_mod) + " to melee attacks and damage. " + str(
            stuckdoor) + "-in-6 chance to open stuck doors"
        return a
    elif 8 >= strength > 5:
        mel_atk_mod = mel_atk_mod - 1
        stuckdoor = stuckdoor - 1
        a = "| Add " + str(mel_atk_mod) + " to melee attacks and damage. " + str(
            stuckdoor) + "-in-6 chance to open stuck doors"
        return a
    elif 5 >= strength >= 4:
        mel_atk_mod = mel_atk_mod - 2
        stuckdoor = stuckdoor - 2
        a = "| Add " + str(mel_atk_mod) + " to melee attacks and damage. " + str(
            stuckdoor) + "-in-6 chance to open stuck doors"
        return a
    elif strength == 3:
        mel_atk_mod = mel_atk_mod - 3
        stuckdoor = stuckdoor - 3
        a = "| Add " + str(mel_atk_mod) + " to melee attacks and damage. " + str(
            stuckdoor) + "-in-6 chance to open stuck doors"
        return a
    else:
        a = "| Add " + str(mel_atk_mod) + " to melee attacks and damage. " + str(
            stuckdoor) + "-in-6 chance to open stuck doors"
        return a


def int_mod():
    a = "| Literate and fluent in your native language plus 3 additional languages"
    b = "| Literate and fluent in your native language plus 2 additional languages"
    c = "| Literate and fluent in your native language plus 1 additional language"
    d = "| Basic literacy and fluent in your native language"
    e = "| Illiterate but fluent in your native language"
    f = "| Illiterate and have broken speech in your native language"
    g = "| Literate and fluent in your native language"
    if intelligence > 17:
        return a
    elif 17 >= intelligence > 15:
        return b
    elif 15 >= intelligence > 12:
        return c
    elif 8 >= intelligence > 5:
        return d
    elif 5 >= intelligence >= 4:
        return e
    elif intelligence == 3:
        return f
    else:
        return g


magic_save_mod = 0


def wis_mod():
    global magic_save_mod
    if wisdom > 17:
        magic_save_mod = magic_save_mod + 3
        a = "| Add " + str(magic_save_mod) + " to magic saving throws"
        return a
    elif 17 >= wisdom > 15:
        magic_save_mod = magic_save_mod + 2
        a = "| Add " + str(magic_save_mod) + " to magic saving throws"
        return a
    elif 15 >= wisdom > 12:
        magic_save_mod = magic_save_mod + 1
        a = "| Add " + str(magic_save_mod) + " to magic saving throws"
        return a
    elif 8 >= wisdom > 5:
        magic_save_mod = magic_save_mod - 1
        a = "| Add " + str(magic_save_mod) + " to magic saving throws"
        return a
    elif 5 >= wisdom >= 4:
        magic_save_mod = magic_save_mod - 2
        a = "| Add " + str(magic_save_mod) + " to magic saving throws"
        return a
    elif wisdom == 3:
        magic_save_mod = magic_save_mod - 3
        a = "| Add " + str(magic_save_mod) + " to magic saving throws"
        return a
    else:
        a = "| Add " + str(magic_save_mod) + " to magic saving throws"
        return a


ac_mod = 0
msl_atk_mod = 0


def dex_mod():
    global ac_mod, msl_atk_mod
    if dexterity > 17:
        ac_mod = ac_mod + 3
        msl_atk_mod = msl_atk_mod + 3
        a = "| Add " + str(ac_mod) + " to armour class and " + str(msl_atk_mod) + " to missile attacks"
        return a
    elif 17 >= dexterity > 15:
        ac_mod = ac_mod + 2
        msl_atk_mod = msl_atk_mod + 2
        a = "| Add " + str(ac_mod) + " to armour class and " + str(msl_atk_mod) + " to missile attacks"
        return a
    elif 15 >= dexterity > 12:
        ac_mod = ac_mod + 1
        msl_atk_mod = msl_atk_mod + 1
        a = "| Add " + str(ac_mod) + " to armour class and " + str(msl_atk_mod) + " to missile attacks"
        return a
    elif 8 >= dexterity > 5:
        ac_mod = ac_mod - 1
        msl_atk_mod = msl_atk_mod - 1
        a = "| Add " + str(ac_mod) + " to armour class and " + str(msl_atk_mod) + " to missile attacks"
        return a
    elif 5 >= dexterity >= 4:
        ac_mod = ac_mod - 2
        msl_atk_mod = msl_atk_mod - 2
        a = "| Add " + str(ac_mod) + " to armour class and " + str(msl_atk_mod) + " to missile attacks"
        return a
    elif dexterity == 3:
        ac_mod = ac_mod - 3
        msl_atk_mod = msl_atk_mod - 3
        a = "| Add " + str(ac_mod) + " to armour class and " + str(msl_atk_mod) + " to missile attacks"
        return a
    else:
        a = "| Add " + str(ac_mod) + " to armour class and " + str(msl_atk_mod) + " to missile attacks"
        return a


hp_mod = 0


def con_mod():
    global hp_mod

    if constitution > 17:
        hp_mod = 3
        a = "| Add " + str(hp_mod) + " to hit points"
        return a
    elif 17 >= constitution > 15:
        hp_mod = 2
        a = "| Add " + str(hp_mod) + " to hit points"
        return a
    elif 15 >= constitution > 12:
        hp_mod = 1
        a = "| Add " + str(hp_mod) + " to hit points"
        return a
    elif 8 >= constitution > 5:
        hp_mod = -1
        a = "| Add " + str(hp_mod) + " to hit points"
        return a
    elif 5 >= constitution >= 4:
        hp_mod = -2
        a = "| Add " + str(hp_mod) + " to hit points"
        return a
    elif constitution == 3:
        hp_mod = -3
        a = "| Add " + str(hp_mod) + " to hit points"
        return a
    else:
        a = "| Add " + str(hp_mod) + " to hit points"
        return a


npc_react = 0
max_retainer = 4
loyalty = 7


def cha_mod():
    global npc_react, max_retainer, loyalty
    a = "| Modify NPC reactions by " + str(npc_react) + ". You can hire up to " + str(
        max_retainer) + " retainer(s) with a loyalty of " + str(loyalty)
    if charisma > 17:
        npc_react = npc_react + 2
        max_retainer = max_retainer + 3
        loyalty = loyalty + 3
        a = "| Modify NPC reactions by " + str(npc_react) + ". You can hire up to " + str(
            max_retainer) + " retainer(s) with a loyalty of " + str(loyalty)
        return a
    elif 17 >= charisma > 15:
        npc_react = npc_react + 1
        max_retainer = max_retainer + 2
        loyalty = loyalty + 2
        a = "| Modify NPC reactions by " + str(npc_react) + ". You can hire up to " + str(
            max_retainer) + " retainer(s) with a loyalty of " + str(loyalty)
        return a
    elif 15 >= charisma > 12:
        npc_react = npc_react + 1
        max_retainer = max_retainer + 1
        loyalty = loyalty + 1
        a = "| Modify NPC reactions by " + str(npc_react) + ". You can hire up to " + str(
            max_retainer) + " retainer(s) with a loyalty of " + str(loyalty)
        return a
    elif 8 >= charisma > 5:
        npc_react = npc_react - 1
        max_retainer = max_retainer - 1
        loyalty = loyalty - 1
        a = "| Modify NPC reactions by " + str(npc_react) + ". You can hire up to " + str(
            max_retainer) + " retainer(s) with a loyalty of " + str(loyalty)
        return a
    elif 5 >= charisma >= 4:
        npc_react = npc_react - 1
        max_retainer = max_retainer - 2
        loyalty = loyalty - 2
        a = "| Modify NPC reactions by " + str(npc_react) + ". You can hire up to " + str(
            max_retainer) + " retainer(s) with a loyalty of " + str(loyalty)
        return a
    elif charisma == 3:
        npc_react = npc_react - 2
        max_retainer = max_retainer - 3
        loyalty = loyalty - 3
        a = "| Modify NPC reactions by " + str(npc_react) + ". You can hire up to " + str(
            max_retainer) + " retainer(s) with a loyalty of " + str(loyalty)
        return a
    else:
        return a


xp_mod = 0


def xp_mod():
    global xp_mod
    if profession == 3:
        if prime_req >= 16 and prime_req2 >= 13:
            xp_mod = 10
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif 15 >= prime_req > 13 and prime_req2 >= 13:
            xp_mod = 5
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif 8 >= prime_req > 5 and 8 >= prime_req2 > 5:
            xp_mod = -5
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif 5 >= prime_req >= 3 and 5 >= prime_req2 >= 3:
            xp_mod = -10
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        else:
            xp_mod = 0
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
    elif profession == 5:
        if prime_req >= 16 and prime_req2 >= 16:
            xp_mod = 10
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif prime_req >= 13 or prime_req2 >= 13:
            xp_mod = 5
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif 8 >= prime_req > 5 and 8 >= prime_req2 > 5:
            xp_mod = -5
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif 5 >= prime_req >= 3 and 5 >= prime_req2 >= 3:
            xp_mod = -10
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        else:
            xp_mod = 0
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
    else:
        if prime_req > 15:
            xp_mod = 10
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif 15 >= prime_req > 12:
            xp_mod = 5
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif 8 >= prime_req > 5:
            xp_mod = -5
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        elif 5 >= prime_req >= 3:
            xp_mod = -10
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a
        else:
            xp_mod = 0
            a = "Adjust XP by " + str(xp_mod) + "%."
            return a


# Roll stats and print results
strength = roll_stats()
str_mod = str_mod()
print("STR: " + str(strength) + str(str_mod))
intelligence = roll_stats()
int_mod = int_mod()
print("INT: " + str(intelligence) + str(int_mod))
wisdom = roll_stats()
wis_mod = wis_mod()
print("WIS: " + str(wisdom) + str(wis_mod))
dexterity = roll_stats()
dex_mod = dex_mod()
print("DEX: " + str(dexterity) + str(dex_mod))
constitution = roll_stats()
con_mod = con_mod()
print("CON: " + str(constitution) + str(con_mod))
charisma = roll_stats()
cha_mod = cha_mod()
print("CHA: " + str(charisma) + str(cha_mod))

# Choosing a class
input("Press ENTER to continue")
choice = 2  # 2 is no and will continue the loop until the choice of 1 (yes) is selected
# Prime requisite will be assigned to STR, INT, WIS, DEX, STR+INT, STR+DEX as 1,...,6
# respectively based on class chosen.
prime_req = 0
# Hit die number will be defined by the maximum sides of the die rolled (ie 6 for 1d6)
hit_die = 0
# profession initialized to -1 to begin the while loop
profession = -1
profession_list = {1: 'Cleric', 2: 'Dwarf', 3: 'Elf', 4: 'Fighter', 5: 'Halfling', 6: 'MagicUser', 7: 'Thief'}
profession_skills = {
    1: "Turn Undead, Divine Magic",
    2: "Detect construction tricks, Detect room traps, 60' infravision",
    3: "Arcane Magic, Detect secret doors, Ghoul paralysis immunity, 60' infravision",
    4: "Use any weapons or armour",
    5: "+2 to Armour Class vs large opponents, Hiding, +1 missile attack bonus",
    6: "Arcane Magic",
    7: "Back-stab, Read Languages, Scroll Use, Thief Skills"
}
prime_req_list = {
    1: "Wisdom",
    2: "Strength",
    3: "Intelligence and Strength",
    4: "Strength",
    5: "Dexterity and Strength",
    6: "Intelligence",
    7: "Dexterity"
}
while choice == 2:
    while profession == -1:
        try:
            print("Choose a class.\nYour choices are:\n1. Cleric\n2. Dwarf\n3. Elf\n4. Fighter\n5. Halfling"
                  "\n6. Magic-User\n7. Thief")
            profession = int(input("Enter the number of the class you'd like to choose: "))
            if profession < 1 or profession > 7:
                print("Select a value between 1 and 7")
                profession = -1
                continue
        except ValueError:
            # Ensure the right data type is entered.
            print("Sorry, I didn't understand that. Select a value between 1 and 7")
            profession = -1
            continue
        # Validating Demi-Human choices
        if profession == 3 and intelligence < 9:
            print("Intelligence is too low, pick another class")
            profession = -1
            continue
        elif profession == 2 and constitution < 9:
            print("Constitution is too low, pick another class")
            profession = -1
            continue
        elif profession == 5 and constitution < 9 or profession == 5 and dexterity < 9:
            print("Constitution or Dexterity is too low, pick another class")
            profession = -1
            continue
        else:
            break

    # Display class summary and confirming choice
    if profession == 1:  # Cleric
        prime_req = wisdom
        hit_die = 6
        max_level = 14
        print("Clerics are adventurers who have sworn to serve a diety.")
        print("Prime Requisite: " + prime_req_list[profession] + "\nHit Dice: 1d6\nMaximum Level: 14"
                                                                 "\nArmour: Any, including shields\nWeapons: Any "
                                                                 "blunt weapons \nLanguages: Alignment, Common\nClass "
                                                                 "Abilities: " + profession_skills[profession])
    elif profession == 2:  # Dwarf
        prime_req = strength
        hit_die = 8
        max_level = 12
        print("Dwarves are stout, bearded demi-humans who typically live underground.")
        print("Prime Requisite: " + prime_req_list[profession] + "\nHit Dice: 1d8\nMaximum Level: 12"
                                                                 "\nArmour: Any, including shields\nWeapons: Small or "
                                                                 "Normal sized \nLanguages: Alignment, Common, "
                                                                 "Dwarvish, Gnomish, Goblin, Kobold "
                                                                 "\nClass Abilities: " + profession_skills[profession])
    elif profession == 3:  # Elf
        prime_req = intelligence
        prime_req2 = strength
        hit_die = 6
        max_level = 10
        print("Elves are slender, fey demi-humans with pointed ears.")
        print("Prime Requisite: " + prime_req_list[profession] + "\nHit Dice: 1d6\nMaximum Level: 10"
                                                                 "\nArmour: Any, including shields\nWeapons: Any"
                                                                 "\nLanguages: Alignment, Common, Elvish, Gnoll, "
                                                                 "Hobgoblin, Orcish "
                                                                 "\nClass Abilities: " + profession_skills[profession])
    elif profession == 4:  # Fighter
        prime_req = strength
        hit_die = 8
        max_level = 14
        print("Fighters are adventurers dedicated to mastering the arts of combat and war.")
        print("Prime Requisite: " + prime_req_list[profession] + "\nHit Dice: 1d8\nMaximum Level: 14"
                                                                 "\nArmour: Any, including shields\nWeapons: Any"
                                                                 "\nLanguages: Alignment, Common")
    elif profession == 5:  # Halfling
        prime_req = dexterity
        prime_req2 = strength
        hit_die = 6
        max_level = 8
        print("Halflings are small, rotund demi-humans with furry feet and curly hair.")
        print("Prime Requisite: " + prime_req_list[profession] + "\nHit Dice: 1d6\nMaximum Level: 8"
                                                                 "\nArmour: Any appropriate to size, including shields"
                                                                 "\nWeapons: Any appropriate to size"
                                                                 "\nLanguages: Alignment, Common, Halfling"
                                                                 "\nClass Abilities: " + profession_skills[profession])
    elif profession == 6:  # Magic User
        prime_req = intelligence
        hit_die = 4
        max_level = 14
        print("Magic-Users are adventurers whose study of arcane secrets has taught them how to cast spells.")
        print("Prime Requisite: " + prime_req_list[profession] + "\nHit Dice: 1d4\nMaximum Level: 14"
                                                                 "\nArmour: None\nWeapons: Dagger"
                                                                 "\nLanguages: Alignment, Common\nClass Abilities: " +
              profession_skills[profession])
    elif profession == 7:  # Thief
        prime_req = dexterity
        hit_die = 4
        max_level = 14
        print("Thieves are adventurers who live by their skills of deception and stealth.")
        print("Prime Requisite: " + prime_req_list[profession] + "\nHit Dice: 1d4\nMaximum Level: 14"
                                                                 "\nArmour: Leather, no shields\nWeapons: Any"
                                                                 "\nLanguages: Alignment, Common"
                                                                 "\nClass Abilities: " + profession_skills[profession])
    # Confirm choice
    try:
        choice = input("Press Enter to Continue")
        choice == 1
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    if choice == 1:
        break
    else:
        choice == 2
        continue

# Enter character level to determine hit points
level = -1
while level == -1:
    try:
        level = int(input("Enter character level: "))
        if level > max_level:
            print(profession_list[profession] + " cannot exceed level " + str(max_level))
            level = -1
            continue
        elif level < 1:
            print("Level cannot be less than 1")
            level = -1
            continue
    except ValueError:
        print("Sorry I didn't understand that")
        level = -1
        continue
    else:
        break


# Roll function to roll hit points
def hitpoints():
    a = []  # creates a list to store values
    if level < 10:
        for x in range(0, level):
            a.append(random.randint(1, hit_die))
        add = sum(a[0:]) + hp_mod * level
        if add < 1:
            add = 1
    elif level >= 10:
        if profession == 1 or profession == 6:
            for x in range(0, 9):
                a.append(random.randint(1, hit_die))
            add = sum(a[0:]) + hp_mod * 9 + 1 * (level - 9)
        elif profession == 3 or profession == 4 or profession == 7:
            for x in range(0, 9):
                a.append(random.randint(1, hit_die))
            add = sum(a[0:]) + hp_mod * 9 + 2 * (level - 9)
        elif profession == 2:
            for x in range(0, 9):
                a.append(random.randint(1, hit_die))
            add = sum(a[0:]) + hp_mod * 9 + 3 * (level - 9)
    return add


hitpoints = hitpoints()

# Determine THAC0 and Saving Throws from a provided csv file
# Format is [Class,Level,Death,Wands,Paralysis,Breath,Spells,THAC0]
with open("SavingThrows_THAC0.csv", "r") as file:
    name = profession_list[profession]
    saving_throw = {(name, level): tuple(saves) for name, level, *saves in csv.reader(file)}
    death, wands, paralysis, breath, spells, thaco = saving_throw[(name, str(level))]

# Choose Alignment
alignment = -1
alignments = {1: "Law", 2: "Neutral", 3: "Chaos"}
while alignment == -1:
    try:
        alignment = int(input("Choose your alignment: \n1. Law\n2. Neutral\n3. Chaos\n"))
        if alignment < 1 or alignment > 3:
            print("Select a value between 1 and 3")
            alignment = -1
            continue
    except ValueError:
        print("Sorry, I didn't understand that. Select a value between 1 and 3.")
        alignment = -1
        continue

# Roll function for starting gold
gold = roll_stats() * 10
print("Your starting gold is " + str(gold))

# Buy Armour and Shield
armour = -1
shield = False
shield_choice = -1
# For both armour value and cost, 1 = Leather, 2 = Chain mail, 3 = Plate mail, 4 = No Armour
armour_value = {1: 7, 2: 5, 3: 3, 4: 9}
armour_cost = {1: 20, 2: 40, 3: 60, 4: 0}
ac_shield = 1
shield_cost = 10
while armour == -1:
    try:
        armour = int(input("Select Armour to Buy: \n1. Leather (AC 7), 20 gold\n2. Chain mail (AC 5), 40 gold"
                           "\n3. Plate mail (AC 3), 60 gold\n4. No Armour\n"))
        if armour < 1 or armour > 4:
            print("Select a value between 1 and 4")
            armour = -1
            continue
    except ValueError:
        print("Sorry, I didn't understand that. Select a value between 1 and 4.")
        armour = -1
        continue
    if gold < armour_cost[armour]:
        print("Not enough gold!")
        armour = -1
        continue

# Subtract armour costs from gold
gold = gold - armour_cost[armour]

while shield_choice == -1:
    try:
        shield_choice = int(input("Do you want to buy a shield? (+1 AC bonus, 10 gold)\n1. Yes\n2. No\n"))
        if shield_choice < 1 or shield_choice > 2:
            print("Enter 1 or 2")
            shield_choice = -1
            continue
    except ValueError:
        print("Sorry, I didn't understand that. Select a value between 1 and 4.")
        shield_choice = -1
        continue
    if gold < shield_cost:
        print("Not enough gold!")
        shield_choice = -1
        continue
    else:
        shield = True

# Subtract shield costs from gold
if shield:
    gold = gold - shield_cost

# Calculate AC
if profession == 7:  # Thief armour is limited to leather and no shields
    if armour != 1 and armour != 4:
        armour = 4
        armour_class = armour_value[4] - ac_mod
    else:
        armour_class = armour_value[armour] - ac_mod
elif profession == 6:  # Magic User cannot use armour or shields
    if armour != 4:
        armour = 4
        armour_class = armour_value[4] - ac_mod
    else:
        armour_class = armour_value[armour] - ac_mod
else:
    if shield:
        armour_class = armour_value[armour] - ac_mod - ac_shield
    else:
        armour_class = armour_value[armour] - ac_mod

# Character Name
name = str(input("Enter a name for your adventurer: "))

# Character Summary
print("\n---------CHARACTER SUMMARY--------------")
print("Character Name: " + name)
print("Class: " + profession_list[profession])
print("Level: " + str(level))
print("XP modifier: " + xp_mod())
print("Base Hit Die: 1d" + str(hit_die))
print("HP: " + str(hitpoints))
print("Armour Class: " + str(armour_class))
print("THAC0: " + str(thaco))
print("Saving Throws: D" + str(death) + " W" + str(wands) + " P" + str(paralysis) + " B" + str(breath) + " S" + str(
    spells))
print("STR: " + str(strength) + str(str_mod))
print("INT: " + str(intelligence) + str(int_mod))
print("WIS: " + str(wisdom) + str(wis_mod))
print("DEX: " + str(dexterity) + str(dex_mod))
print("CON: " + str(constitution) + str(con_mod))
print("CHA: " + str(charisma) + str(cha_mod))
print("Class Abilities: " + str(profession_skills[profession]))
print("Remaining gold: " + str(gold))
print("-----------------------------------------")
