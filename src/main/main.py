
from cgi import print_arguments
import random
from re import finditer

players = []
players_in_round = []

table = []

pot = 0

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Clubs","Hearts","Diamonds","Spades"]
deck = []


def resetDeck():
    for rank in ranks:
        for suit in suits:
            deck.append([rank + " of " + suit])
    random.shuffle(deck)
    
def addPlayer():
    #[Name, Money, Card1, Card2, currentpot]
    player = []
    player.append(input("Please enter your name: "))
    player.append(int(input("Please enter your buy in £")))
    player.append("")
    player.append("")
    player.append(0)
    return player

def getPlayers():
    not_enough = True
    while(not_enough):
        players.append(addPlayer())
        if input("Is that all players? Y/N").upper() == "Y":
            not_enough = False
    print("Here is a list of all players")
    print(players)
    print("Lets begin")

def dealCards():
    for playa in players:
        playa[2] = deck.pop(0)
    #this is two loops to work around the poker dealing conventions
    for playa in players:
        playa[3] = deck.pop(0)

def playRound(first):
    current_pot = 0
    current_bid = 0
    table.append(deck.pop(0))
    if first:
        table.append(deck.pop(0))
        table.append(deck.pop(0))
    done = False
    while(not(done)):
        for playa in players_in_round:
            print("Cards on the table")
            print(table)
            print(" ")
            print(playa)
            finished = False
            while (not(finished)):
                i = input("Dear " + playa[0] + " how much would you like to bid?")
                if i.upper() == "F":
                    players_in_round.remove(playa)
                    finished = True
                else:
                    i = int(i)
                    if i > playa[1]:
                        print("you do not have enough money to bid that much")
                    elif i < current_bid:
                        print("You must bid more than" + str(current_bid))
                    else:
                        playa[1] = playa[1]- i
                        current_bid = i
                        current_pot = current_pot+ current_bid
                        finished = True
            print("player " + playa[0] + " bid " + str(current_bid) )
        
            
    print("Round over!")
    pot = pot + current_pot
        
            


if __name__ == '__main__':
    while(True):
        deck = []
        resetDeck()
        getPlayers()
        dealCards()
        print(players)
        players_in_round = players
        playRound(True)
        print(pot)
        playRound(False)
        print(pot)
        playRound(False)
        print(pot)
        input("")
        
    