from prettytable import PrettyTable as PT

print("\033[H\033[J", end="")
"""
data = {
    'Weapons': {'Short Sword': {"Damage":10,"reach":5,"Bonus":"No bonus"}},
    'Armor': {"Shield":{"Bonus armor":2,"weight":10}},
}

table = PrettyTable()
table.field_names = ["Type", "Item", "//","///"]

for type_of_item, item in data.items():
    print("TYPE:",type_of_item)
    for stats in item:
        print("ITEM:", item)
        for values in stats:
            print("Stat:",stats,"has the value:",values)
"""


def loop_nests(inventory):

    for type_of_item, objects in inventory.items():
        
        #Weapons table
        if type_of_item=="Weapons":
            weapon_table=PT(["Weapon","Damage","Reach","Bonus"])  #Create header

            for weapon, stats in objects.items():
                w_list=[]                                   #Rest Entry
                w_list.append(str(weapon))                  #Add weapon name
            
                for key, value in stats.items():
                    w_list.append(str(value))               #Add diferent stats (dmg, reach,bonus)

                weapon_table.add_row(w_list)                #Add entry to table

        #Armor table
        if type_of_item=="Armor":
            armor_table=PT(["Armor","Armor class","Weight","Bonus"])  #Create header

            for armor, stats in objects.items():
                a_list=[]                                   #Rest Entry
                a_list.append(str(armor))                  #Add weapon name
            
                for key, value in stats.items():
                    a_list.append(str(value))               #Add diferent stats (dmg, reach,bonus)

                armor_table.add_row(a_list)                #Add entry to table

    print(weapon_table)
    print(armor_table)

   

inventory = {
    "Weapons": {
        "Short Sword": {
            "Damage": 10,
            "Reach":5,
            "Bonus":"no bonus"
        },
        "Dagger":{
            "Damage": 2,
            "Reach": 1,
            "Bonus": "Sneak attack"
        }
    },
    "Armor":{
        "Shield":{
            "Armor class": 1,
            "Weight": 5,
            "Bonus":"No bonus"
        },
        "Plate armor":{
            "Armor class": 5,
            "Weight": 10,
            "Bonus": "Disadvantage on Stealth"
        }

    },
}

loop_nests(inventory)




