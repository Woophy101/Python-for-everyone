print("\033[H\033[J", end="") #clrscr

class User:
    def __init__(self, username, id):
        #Esta funcion de la clase da los atributos iniciales de la clase. Todo lo que esté aqui sera
        #procesado al momento de crear un objeto.
        self.username= username
        self.id=id
####        print("new user creted:",username)
####        print("ID assigned:", id)
####        self.password=input("Escriba su contraseña: ") #con este codigo cada usuario puede
####        print("Contraseña: ", self.password,"creada")  #colocar su propia contraseña al ser creado
        self.password="1234"
        self.following=0   
        self.followers=0
        self.l_followers=[]
        self.l_following=[]
        self.loged=False     

    def login(self): #al colocar Self podemos callear los atributos propios. 
####       i=input("Enter password:")
        if "1234"==self.password:
            print(self.username+": 🟢CONECTED🟢")
            self.loged=True
        else:
            print("Wrong password❌")
    
    def logoff(self):
        print(self.username+": 🔴DISCONECTED🔴")
        self.loged=False

    def follow(self,user):
        if self.loged == True:
            if user.username not in self.l_following:
                user.followers +=1
                user.l_followers.append(self.username)
                self.following +=1
                self.l_following.append(user.username)
                print(self.username,"follows", user.username)
            else:
                print(self.username, "already following", user.username,"❌")
        else:
            print("Not logged in as", self.username)

    def not_follow(self, user):
        if self.loged == True:
            if user.username in self.l_following:
                user.followers -=1
                user.l_followers.remove(self.username)
                self.following -=1
                self.l_following.remove(user.username)
                print(self.username,"stopped following", user.username)
            else:
                print(self.username, "already NOT following", user.username,"❌")                
        else:
            print("Not logged in as", self.username)

    def followers_list(self):
        if self.loged == True:
            print(self.username,"is followed by ",self.l_followers)
        else:
            print("Not logged in as", self.username)

    def following_list(self):
        if self.loged == True:
            print(self.username,"follows",self.l_following)
        else:
            print("Not logged in as", self.username)


marianita=User("Marianita",1)
gebito=User("Gebito", 2)
lolita=User("Lolita",3)
brendan=User("Brendan",4)
braulio=User("Braulio",5)
monita=User("Monita",6)
canito=User("Canito",7)

print("🔹Loggin as gebito")
gebito.login()
print("🔹try to check marianita followers (private)")
marianita.followers_list()
print("🔹gebito followsers list")
gebito.followers_list()
print("🔹gebito follows other profiles")
gebito.follow(marianita)
gebito.follow(lolita)
gebito.follow(brendan)
gebito.follow(canito)
print("🔹gebito tries to follow marianita twice cuz she cute")
gebito.follow(marianita)
print("🔹gebito updated following list")
gebito.following_list()
print("🔹gebito stopped following brendan")
gebito.not_follow(brendan)
print("🔹gebito tries to unfollow a profile not in his following list")
gebito.not_follow(monita)
print("🔹gebito following list")
gebito.following_list()
print("🔹a lot of profiles follow gebito back")
marianita.login()
marianita.follow(gebito)
marianita.logoff()
brendan.login()
brendan.follow(gebito)
brendan.logoff()
canito.login()
canito.follow(gebito)
canito.logoff()
lolita.login()
lolita.follow(gebito)
lolita.logoff()
print("🔹gebito followers list updated")
gebito.followers_list()