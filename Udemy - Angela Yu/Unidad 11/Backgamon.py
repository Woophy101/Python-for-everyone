import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

#####--------------------------------------------------------------------------------------
def display_cards(cards,player):
    print("CARTAS DE",player)
    for card in cards:
        if card <10:       
            print(" ________________\n|                |\n|  ",card,"           |\n|                |\n|                |\n|                |\n|                |\n|                |\n|                |\n|          ",card,"   |\n|________________|")
        else:  
            print(" ________________\n|                |\n|  ",card,"          |\n|                |\n|                |\n|                |\n|                |\n|                |\n|                |\n|         ",card,"   |\n|________________|")

#####--------------------------------------------------------------------------------------

def deal_card():
    card=random.choice(cards)
    return card

#####--------------------------------------------------------------------------------------

def calculate_score(hand):
    score=0
    for value in hand:
        score=score+value
    return score

#####-------------------------------------------------------------------------------------- 



#inicio loop juego
while True:

    player_cards=[]
    dealer_cards=[]
    player_score=0
    player_score_temp=0
    dealer_score=0
    dealer_score_temp=0
    game_over=False

    #Dealer toma sus cartas
    public_card=deal_card()
    dealer_cards.append(public_card)
    dealer_cards.append(deal_card())
    print("Las cartas de dealer son: ", public_card,", X")
    

    #Loop del jugador para sacar cartas

    while True:
    

        new_card=deal_card()   
        player_cards.append(new_card)

        if new_card == 11:
            player_score_temp=player_score_temp+1
            player_score=player_score+11
        else:
            player_score_temp=player_score_temp+new_card
            player_score=player_score+new_card
    
        display_cards(player_cards,"PLAYER")
        print("El puntaje del jugador es: ",player_score)
        
        if player_score>21:
            #print("puntaje ",player_score," cambiado por ",player_score_temp)
            player_score=player_score_temp
        
        if player_score>21:
            print("Te pasaste!")
            game_over=True
            break

        i=input("Sacar otra carta? y/n: ")
        if i=="y":
            continue
        else:
            break

    #Loop game over

    if game_over==False: 

        #Checkear si el dealer tiene que sacar otra carta

        dealer_score=calculate_score(dealer_cards)
        print("El puntaje del dealer es de ", dealer_score)
        while dealer_score <= 16:
            print("El dealer toma otra carta")
            dealer_cards.append(deal_card())
            dealer_score=calculate_score(dealer_cards)
            print("El nuevo puntaje del dealer es ", dealer_score)
            if dealer_score>21:

                print("BUSTED! El JUGADOR gana!!!")
                game_over=True
            
        if game_over==False:
            
            print("La mano de la casa es:")
            display_cards(dealer_cards,"DEALER")
            print("El puntaje de la casa es: ", dealer_score)

            #Checkear valores de puntakes
            if player_score>dealer_score:
                print("El JUGADOR Gana!")
            elif player_score<dealer_score:
                print("La CASA gana!")
            else:
                print("EMPATE! juega denuevo")
    else:
        print("GAME OVER")

    #reinicio de ciclo   
    i=input("Jugar otra ronda? y/n: ")
    if i == "n":
        break
    else:
        continue