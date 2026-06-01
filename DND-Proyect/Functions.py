import random

#---------------------------Mechanics------------------------------------

def ability_score_modifier(stat):
    "Quick calculation of an ability score modifier"
    score=(stat-10)//2
    return score

def dice_roll():
    roll=random.randint(1,20)
    return roll

def dice_roll_advantage():
    roll1=random.randint(1,20)
    roll2=random.randint(1,20)
    if roll1 < roll2:
        roll=roll2
    if roll2 < roll1:
        roll=roll1
    else:
        roll=roll1
    return roll
#-----------------------------DEBUGGING-------------------------------------

