import random

words=["apple","Upper","Raccoon"]
chosen_word=random.choice(words).lower()
print(f"WORD CHOSEN:{chosen_word} || {type(chosen_word)}")
lives=5
game_over=False

#Crear un HUD que muestre los espacios de la plaabra seleccionada y pedir una letra para adivinar
secret_word=[]
for letters in chosen_word:
    secret_word.append("_")

print_word="".join(secret_word)
#Comienza el ciclo de juego

while not game_over:
    print(f"Secret word:{print_word}")
    guess=input("Guess a letter:").lower()

#Checkear si la letra está en la palabra secreta y mostrar donde o bien quitar una vida

    i=0
    for letter in chosen_word:
        if letter==guess:
            secret_word[i]=letter
            print(f"Letter found!")
        i+=1
    
    print_word="".join(secret_word)

    if guess not in chosen_word:
        lives -=1
        print(f"Try again!\nLives left={lives}")
#Condiciones de finalizacion

        
    if print_word==chosen_word:
        print("YOU WIN!!")
        game_over=True

    if lives<1:
        print("YOU LOOSE!")
        game_over=True
    

print("GAME OVER")
