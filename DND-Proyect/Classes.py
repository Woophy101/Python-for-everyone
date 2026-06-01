from Functions import *
from GUI import *


#-----------------------------------------------------------------------------------#



#------------------------------------------CREATURE/CHARACTER-----------------------------------------#
class Creature:
    "----------------------------------------------"
    "Define a simple creature:"
    "   Name:"
    "   HP:"
    "   AC"
    "   STATS: "
    "   STAT MODS:                          "
    "---------------------------------------------"
    def __init__(self,NAME,HP,AC,SPEED,STR,DEX,CON,INT,WIS,CHA):

        #Descriptive:
        self.NAME=NAME
        self.HP=HP        
        self.AC=AC
        self.SPEED=SPEED
        self.role=""
        self.level=1
       
        #Base stats
        self.STR=STR
        self.DEX=DEX
        self.CON=CON
        self.INT=INT
        self.WIS=WIS
        self.CHA=CHA

        #Stats calculation
            
            #MODIFIERS
        self.strmod=ability_score_modifier(STR)
        self.dexmod=ability_score_modifier(DEX)
        self.conmod=ability_score_modifier(CON)
        self.intmod=ability_score_modifier(INT)
        self.wismod=ability_score_modifier(WIS)
        self.chamod=ability_score_modifier(CHA)

        #Inventory initialization
        
        self.inv=Inventory()
        self.eqp=Equipement()

        #CREATION MENSSAGE

        print("----DEBUGGING----------------------✅✅✅--")
        print("----CREATURE CREATED-------------------🗿--")
        print("Creature Name:", self.NAME)
        print("Hit points:", self.HP)
        print("Armor class:", self.AC)
        print("Speed:",self.SPEED,"ft")
        statblock_gui(self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA)

        #print("----EQUIPEMENT-------------------------⚔️--")
        equipement_gui(self.eqp)
        

        print("----INVENTORY--------------------------🎒--")
        print("Weapons:",self.inv.weapons)
        print("Armor:",self.inv.armors)
        print("Consumable:",self.inv.consumables)
        print("Misc:", self.inv.misc)
        print("-------------------------------------------\n")
    
    def check_creature(self):
        "Show creature stats, inventory and general info. Debugging use"
        print(f"-----------------{self.NAME}---------------")
        print("Hit points:", self.HP)
        print("Armor class:", self.AC)
        print("Speed:",self.SPEED,"ft")
        statblock_gui(self.STR, self.DEX, self.CON, self.INT, self.WIS, self.CHA)
        equipement_gui(self.eqp)
        inventory_gui(self.inv)

    
#-----------------------------DEBUGGING-------------------------------------



#--------------------------INVENTORY MANAGMENET ----------------------
class Equipement:
    "Equipement class for a creature. Hold items equiped to activate bonuses and calculate new stats"
    def __init__(self):

        self.head= None
        self.chest=None
        self.main_hand=None
        self.second_hand=None
        self.legs=None
        self.feet=None

    def equip_item(self,item):
        self.chest=item
        print(item.name,"equiped on chest")


class Inventory:
    "Create dict for diferent items on the Creature() inventory" 
    def __init__(self):

        self.weapons={}
        self.armors={}
        self.consumables={}
        self.misc={}

    

    def add_item(self,item):
        if item.tag == "weapon":
            if item in self.weapons:
                self.weapons[item]+=1
                #print("Weapon", item.name,"added. Currently",self.weapons[item],"on inventory")
            else:
                self.weapons[item]=1
                #print("NEW WEAPON!",item.name,"added to inventory! ")

        if item.tag == "armor":
            if item in self.armors:
                self.armors[item]+=1
            else:
                self.armors[item]=1

    def print_inventory(self):
        inventory_gui(self.weapons)



#---------------------------ITEM CLASES---------------------------------
class Weapon:
    "----------------------------------------------"
    "Create an item with the ""weapon"" tag:"
    "   NAME:"
    "   DAMAGE:"
    "   REACH"
    "   BONUS: "
    "---------------------------------------------"

    def __init__(self,name, dmg, reach, bonus):
        
        #MAIN STATS
        self.tag="weapon"
        self.name=name
        self.dmg=dmg
        self.reach=reach
        
        #FLAVOR STATS

        self.bonus=bonus
        self.dmg_type=""    
        self.rarity=""
        self.properties=""
        self.weight=""


        #DESCRIPTION DICTIONARY (FOR GUI)
        self.description={self.name:{
                          "damage":dmg,
                          "reach":reach,
                          "bonus":bonus
                         }}
        
        #CREATION MENSSAGE
        print("----DEBUGGING----------------------✅✅✅--")
        print("----WEAPON CREATED---------------------🗡️--")
        print("Weapon Name:", self.name)
        print("Damage:", self.dmg)
        print("Bonus:",self.bonus)
        print("-------------------------------------------\n")


class Armor:
    "----------------------------------------------"
    "Create an item with the ""armor"" tag:"
    "   NAME:"
    "   ARMOR:"
    "   WEIGHT"
    "   BONUS: "
    "---------------------------------------------"

    def __init__(self,name, armor, bonus):
        
        #MAIN STATS
        self.tag="armor"
        self.name=name
        self.armorclass=armor
        
        #FLAVOR STATS

        self.bonus=bonus
        self.dmg_type=""    
        self.rarity=""
        self.properties=""
        self.weight=""
        
        #CREATION MENSSAGE

        print("----DEBUGGING----------------------✅✅✅--")
        print("----ARMOR CREATED----------------------🛡️--")
        print("Weapon Name:", self.name)
        print("Armor:", self.armorclass)
        print("Bonus:",self.bonus)
        print("-------------------------------------------\n")
#-----------------------------DEBUGGNG---------------------------------

