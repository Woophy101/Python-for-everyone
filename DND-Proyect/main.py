from Classes import *
from Functions import *


print("\033[H\033[J", end="")

goblin=Creature("Goblin",7,14,30,10,14,12,8,12,6)
short_sword=Weapon("Short sword",7,5,"No bonus")
club=Weapon("Wooden club",4,5,"No bonus")
plate_armor=Armor("Plate armor",1,"Disadvantage on Stealth")
shield=Armor("Small shield",2,"No bonus")

goblin.inv.add_item(short_sword)
goblin.inv.add_item(club)
goblin.inv.add_item(short_sword)
goblin.inv.add_item(plate_armor)
goblin.inv.add_item(shield)
goblin.eqp.equip_item(plate_armor)

goblin.check_creature()
