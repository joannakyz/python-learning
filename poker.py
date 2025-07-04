from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now().timestamp()) 

kind = {"heart", "spade", "diamond", "club"}
nums = {"ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}

deck = {(k,n) for k in kind for n in nums}
print("Deck: ", deck)
print("Number of cards: ", len(deck))

deck_list = list(deck)

player1 = set()
player2 = set()

#gives random cards to players
for i in range(5):
    card1 = randrange(len(deck_list))
    player1.add(deck_list.pop(card1))
    card2 = randrange(len(deck_list))
    player2.add(deck_list.pop(card2))

print("player 1: ", player1)
print("player 2: ", player2)

#checks if player 1 has 4 aces
count = 0
for card in player1:
    if card[1] == "ace":
        count = count + 1

if count == 4:
    print("Player 1 has 4 aces.")

#checks if player 2 has 4 aces
count = 0
for card in player2:
    if card[1] == "ace":
        count = count + 1

if count == 4:
    print("Player 2 has 4 aces.")

#checks if player 1 has ascending numbers
player1_list = []
for card in player1:
    player1_list.append(card[1])
for num in range(len(player1_list)):
    if player1_list[num] == "J":
        player1_list[num] = 11
    if player1_list[num] == "Q":
        player1_list[num] = 12
    if player1_list[num] == "K":
        player1_list[num] = 13
    if player1_list[num] == "ace":
        player1_list[num] = 1
player1_list.sort()
print(player1_list)

for i in range(4):
    if player1_list[i] != player1_list[i + 1] - 1:
        break
else:
    print("Player 1 has 5 ascending cards.")

#checks if player 2 has ascending numbers
player2_list = []
for card in player2:
    player2_list.append(card[1])
for num in range(len(player2_list)):
    if player2_list[num] == "J":
        player2_list[num] = 11
    if player2_list[num] == "Q":
        player2_list[num] = 12
    if player2_list[num] == "K":
        player2_list[num] = 13
    if player2_list[num] == "ace":
        player2_list[num] = 1

player2_list.sort()
print(player2_list)


for i in range(4):
    if player2_list[i] != player2_list[i + 1] - 1:
        break
else:
    print("Player 2 has 5 ascending cards.")
