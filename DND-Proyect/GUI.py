from prettytable import PrettyTable
from Functions import *

def statblock_gui(STR, DEX, CON, INT, WIS, CHA):
    "Create a basic statbloc table with base stats and modifiers"
    "Note: info just for GUI, not for calculations"

    table=PrettyTable(["STATS","STR","DEX","CON","INT","WIS","CHA"])
    table.add_row(["",STR,DEX,CON,INT,WIS,CHA,])
    table.add_row(["MOD:",ability_score_modifier(STR),ability_score_modifier(DEX),ability_score_modifier(CON),ability_score_modifier(INT),ability_score_modifier(WIS),ability_score_modifier(CHA)])
    print(table)
    return table

def inventory_gui(inventory):
    "Create a table GUI for items on the inventory. Used by the check_inventory() function"
    wepapons_table=PrettyTable(["°","Name","Damage","Reach","Bonus"])
    armor_table=PrettyTable(["°","Name","Armor","Weight","Bonus"])
    print("----INVENTORY--------------------------🎒--")
    for weapon in inventory.weapons:
        wepapons_table.add_row([inventory.weapons[weapon],weapon.name,weapon.dmg, weapon.reach,weapon.bonus])
    print("----WEAPONS-----------------------⚔️--")
    print (wepapons_table)

    for armor in inventory.armors:
        armor_table.add_row([inventory.armors[armor],armor.name,armor.armorclass, armor.weight,armor.bonus])

    print("----ARMOR-------------------------🛡️--")
    print (armor_table)
   
def equipement_gui(equipement):
    head=equipement.head
    chest=equipement.chest
    mhand=equipement.main_hand
    shand=equipement.second_hand
    legs=equipement.legs
    feet=equipement.feet
    
    print("-----EQUIPEMENT-------------------------⚔️--")
    print(f"""
            _____
           (     )     {head}
            \___/
           __| |__
         /         \   {chest}
        / /|     |\ \ 
       /_/  \   /  \_\ 
      |__|  |   |  |__|
            |   |
            | | |      {legs}
            | | |
           _| | |_
          /___|___ \   {feet}                    

          """)
        
#-----------------------------DEBUGGING-------------------------------------

