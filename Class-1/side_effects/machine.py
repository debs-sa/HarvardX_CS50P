emoticon = "v.v"

def main():
    global emoticon                     # to change a global statement
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")

def say(phrase):
    print(phrase + " " + emoticon)
    
main()