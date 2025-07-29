#CARD GAME!!! Cards are thrown in the air and when they land each player must collect as many cards as possible. Whoever picks the most wins. 
#I have used randrange in order to make each player choose not in turns. 

from random import seed
from random import randrange
from datetime import datetime

seed()

#functions for random card picks from players
def player1_pick():
    player1.add(deck.pop())


def player2_pick():
    player2.add(deck.pop())


#function that chooses randomly which player will collect a card
def play():
    print(f"START")
    for card in range(len(deck)):
        if randrange(2) == 0:
            player1_pick()
        else:
            player2_pick()
    print("Player1: ", len(player1))
    print("Player2: ", len(player2))

    if len(player1) > len(player2):
        print("Player1 won!")
    elif len(player1) == len(player2):
        print("It's a tie!")
    else:
        print("Player2 won!")

kind = {"heart", "diamond", "spade", "club"}
number = {"ace", 2, 3, 4 , 5, 6, 7, 8, 9, 10, "J", "Q", "K"}

deck = {(k,n) for k in kind for n in number}

player1 = set() 
player2 = set()

play()
