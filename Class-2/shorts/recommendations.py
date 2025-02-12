#### CONDITIONALS ####

def main():
    difficulty = input("Difficult or casual? ")
    players = input("Multiplayer or Single-Player? ")
    
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        else:
            recommend("Klondike")
    else:
        if players == "Multiplayer":
            recommend("Hearts")
        
        else:
            recommend("Clock")     

def recommend(game):
    print("You might like", game)

main()


### OR ###

def main():
    difficulty = input("Difficult or casual? ")
    players = input("Multiplayer or Single-Player? ")
    
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-Player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")

def recommend(game):
    print("You might like", game)

main()