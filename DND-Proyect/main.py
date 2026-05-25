
class Creature:
    "------------------------------------------------------------------------------"
    "Define a simple creature with a stat block and name                           "
    ""
    def __init__(self, name, str, dex, con, int, wis, cha):

        #Descriptive:
        self.name=name
       
        #Base stats
        self.str=str
        self.dex=dex
        self.CON=con
        self.int=int
        self.wis=wis
        self.cha=cha
              
        #Stats calculation
        #MOD

        self.strmod=0

    def stats(self):
        print(f"""
              

              """)







test1=Creature("Goblin",10,10,10,10,10)