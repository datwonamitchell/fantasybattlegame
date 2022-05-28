
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150
elf = "Elf"
elf_hp = 100
elf_damage = 100
human = "Human"
human_hp = 150
human_damage = 20
orc = "Orc"
orc_hp = 250
orc_damage = 200
dragon_hp = 300
dragon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")
    player_choice = input("Choose your character: ").lower()
    if (player_choice == "1" or player_choice == wizard.lower()):
        my_character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if (player_choice == "2" or player_choice == elf.lower()):
        my_character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if (player_choice == "3" or player_choice == human.lower()):
        my_character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    if (player_choice == "4" or player_choice == "orc"):
        my_character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    print("Unknown Character")
print("You have chosen the character: ", my_character)
print("Health: ", my_hp)
print("Damage: ", my_damage)

while True:
    dragon_hp = dragon_hp - my_damage
    print("Dragon took", my_damage, "points of damage from",my_character, "!", "(", "Dragon", "HP:", dragon_hp, ")")
    if(dragon_hp <= 0):
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp - dragon_damage
    print(my_character, "took", dragon_damage,"points of damage from Dragon! ", "(", my_character, "HP:", my_hp, ")")
    if(my_hp <= 0):
        print(my_character, "has lost the battle.")
        break
