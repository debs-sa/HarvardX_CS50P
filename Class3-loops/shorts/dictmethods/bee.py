WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    
    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")
        
        # TODO: Check if guess in dictionary
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {WORDS[guess]} points.")
    
    print("That's the game!")

main()

########################################################################

WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

def main():
    print("Welcome to Spelling Bee!")
    for word, points in WORDS.items():
        print(f"{word} was worth {points} points.")
    print("That's the game!")

main()