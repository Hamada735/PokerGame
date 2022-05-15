
from cgi import print_arguments
from dis import dis
import random
from re import finditer

players = []
small_blind = 10
big_blind = 20
table = []
pot = 0
ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Clubs","Hearts","Diamonds","Spades"]
deck = []
display = ["Name: ", "Money: ", "Card 1: ", "Card 2: ", "Current bid: "]


def resetDeck():
    for rank in ranks:
        for suit in suits:
            deck.append(rank + " of " + suit)
    random.shuffle(deck)
    
def addPlayer():
    #[Name, Money, Card1, Card2, currentbid]
    player = []
    player.append(input("Please enter your name: "))
    buyIn = int(input("Please enter your buy in £"))
    while not buyIn.is_integer():
        print("Error: Enter an integer value")
        buyIn = int(input("Please enter your buy in £"))
    player.append(buyIn)
    player.append("")
    player.append("")
    player.append(0)
    return player

def getPlayers():
    #This code is for getting user input. temp comment to save time
    #not_enough = True
    #while(not_enough):
    #    players.append(addPlayer())
    #    if input("Is that all players? Y/N: ").upper() == "Y":
    #        if len(players) < 2:
    #            print("At least 2 players are requred to start")
    #        else:    
    #            not_enough = False
    
    #temp code, uncomment to save time

    players.append(["Hammy", 100, "", "", 0, True])
    players.append(["Matthew", 100, "", "", 0, True])
    players.append(["George", 100, "", "", 0, True])
    players.append(["Kamil", 100, "", "", 0, True])

    print("Here is a list of all players")
    print("\n")
    for playa in players:
        playerToDisplay(playa)
    print("Lets begin!")
    print("#####################")
    print("\n")

def playerToDisplay(player):

    for x in range(len(display)):        # display = ["Name: ", "Money: ", "Card 1: ", "Card 2: ", "Current bid: "]
        print(display[x], player[x])
    print("\n")

def dealCards():
    for playa in players:
        playa[2] = deck.pop(0)
    #this is two loops to work around the poker dealing conventions
    for playa in players:
        playa[3] = deck.pop(0)
    print("cards dealt")

def blinds():
    players[0][4]=small_blind
    print("player ", players[0][0] ," is small blind")
    players[1][4]=big_blind
    

def playRound(first):
    global pot
    current_pot = 0
    current_bid = 20
    if first:
        table.append(deck.pop(0))
        table.append(deck.pop(0))
        table.append(deck.pop(0))
    else:
        table.append(deck.pop(0))
        print(table)
    done = False
    message = " how much would you like to bid? "
    while(not done):
        for playa in players:
            if playa[5] == True:
                if not first:
                    print("Cards on the table")
                    print(table)
                    print("\n")
                playerToDisplay(playa)
                finished = False
                while (not finished):
                    if playa[4]<current_bid:
                        i = input("Dear " + playa[0] + message)
                        if i.upper() == "F":
                            playa[5] = False
                            finished = True

                            checkWinner()
                            
                        else:
                            try:
                                i = int(i)
                            except:
                                print("Error: Enter an integer value or 'F' to fold") 
                                continue
                            if i > playa[1]:
                                print("You do not have enough money to bid that much")
                            elif i < current_bid:
                                print("You must bid more than ", current_bid)
                            else:
                                current_bid = i
                                playa[4] = i
                                current_pot = current_pot+ current_bid
                                finished = True
                    else:
                        finished = True
                        print(playa[0] + " bid " + str(current_bid))
                        print("\n")
                    
        for playa in players:
            if playa[5] == True:
                if(playa[4]!= current_bid):
                    done = False
                    break
                else:
                    done = True
            
    print("Round over!")

    for playa in players:
        playa[1] -= playa[4]
        playa[4] = 0
    current_bid = 0
    pot += current_pot

def resetPlayers():
    for player in players:
        player[4] = 0
        player[5] = True

def checkWinner():
    nonFoldPlayers = []
    for player in players:
        if player[5] == True:
            nonFoldPlayers.append(player)
    if len(nonFoldPlayers) == 1:
        print("Player ", nonFoldPlayers[0][0], " has won!")
        return nonFoldPlayers[0]
    return

        
def sort(hand):
    handy = []


def whoWon():      # < gotta check hand rankings :(
    hands=[]
    for player in players:
        if player[5] == True:
            hands.append([table[0],table[1],table[2],table[3],table[4],player[2],player[3]])
    for hand in hands:
        hand = sort(hand)

    won("bruh")
            
def won(name):
    for player in players:
        if player[0] == name:
            player[1]+= pot
            exit()
            


if __name__ == '__main__':
    while(True):

        pot = 0
        deck = []
        resetDeck()
        getPlayers()
        dealCards()
        blinds()
        playRound(True)
        print(pot)
        playRound(False)
        print(pot)
        playRound(False)
        print(pot)
        whoWon()
        resetPlayers()
        input("")
        