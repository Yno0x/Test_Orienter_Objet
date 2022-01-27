class Player:
    def __init__ (self, name):
        self.Nom=name
        self.meilleurscore = best

class Score:
    def __init__ (self, nombre):
        self.chanson = choixchanson

def play():
    pseudo=str(input("qui êtes vous?"))
    choixchanson=int("il y a 5 chanson, choisissez en une avec 0,1,2,3 ou 4")
    print("partie en cour...")
    Newscore = int(input("Quel score venez vous de faire?"))

def look():
    choicelook=str(input("voulez vous regarder la moyenne de vos score ou votre meilleur ou pire?"))
    if choicelook == "meilleur":
        for i in range (chanson):
            highest=0
            if i >= highest:
                highest=i
            print (highest)
    elif choicelook == "pire":
        for i in range (chanson):
            lowest=0
            if i >= lowest:
                lowest=i
            print (lowest)

    elif choicelook == "moyenne":
        total=chanson[0]+chanson[1]+chanson[2]+chanson[3]+chanson[4]
        moyenne=total/len(chanson)



chanson=[0,1,2,3,4]
Newscore=0
best=0
choixchanson = 0


choice = str(input("voulez vous jouer ou regarder vos score? veuillez répondre avec regarder ou jouer!"))

while choice != "jouer" and choice != "regarder":
    choice = str(input("je n'ai pas compris, veuillez rééssayer. N'oubliez pas de répondre avec REGARDER ou JOUER sinon cela ne fonctionnera pas!"))
    
if choice == "jouer":
    play()
elif choice == "regarder":
    look()