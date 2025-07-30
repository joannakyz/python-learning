#Simple black jack game

from random import seed
from random import randrange
from datetime import datetime


numbers = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
kind = {"Heart", "Spade", "Diamond", "Club"}

deck = {(k, n) for k in kind for n in numbers}

def hand_value(hand):
    card_points = 0 
    ace = False
    for card in hand:
        n = card[1]        
        if n == "J" or n == "Q" or n == "K":
            card_points += 10
        elif n == "ace":
            ace = True
            card_points += 1
        else:
            card_points += n

    if ace:
        if card_points + 10 <= 21:
            card_points += 10
    
    return card_points


def player(hand):
    hand.add(deck.pop())
    hand.add(deck.pop())


    while True:
        print(hand)
        choice = input("H - Hit or S - Stand:  ").strip().lower()
        if choice == "h":
            hand.add(deck.pop())
            value = hand_value(hand)
            if value >= 21:
                return value
        elif choice == "s":
            return hand_value(hand)
        

def computer(value_player, hand):
    hand.add(deck.pop())
    hand.add(deck.pop())

    while True:
        value = hand_value(hand)

        if value >= 21:
            return value 
        elif value >= value_player:
            return value
        else:
            hand.add(deck.pop())


#main function 
def main():
    seed()
    rounds = 1
    score = [0, 0]

    while True:
        print("=" * 15)
        print("Round" + str(rounds))

        player_hand = set()
        player_value = player(player_hand)


        print(player_hand)
        print(hand_value(player_hand))

        print(f"{player_hand} with value: {player_value}")

        if player_value == 21:
            print("Won!")
            result = "player"
        elif player_value > 21:
            print("Lost!")
            result = "computer"
        else:
            print("Computer plays..")
            computer_hand = set()
            computer_value = computer(player_value, computer_hand)
            print(f"{computer_hand} with value: {computer_value}")

            if computer_value > 21:
                print("You won!")
                result = "player"
            else:
                print("You lost!")
                result = "computer"

        if result == "player":
            score[0] += 1
        else:
            score[1] += 1
        
        print(f"Score: {score[0]} - {score[1]}")
        choice = input("Do you want to continue?(y - n):  ").strip().lower()
        if choice == "n":
            break


    

main()
