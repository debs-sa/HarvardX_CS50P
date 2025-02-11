#creating variable "name" and "print" function
# () = parentesis are parameters or arguments to the function
# arguments holds values

name = input("What's your name? ")
# remove whitespace from the str (but not between the middle - l and r strips should be used instead)
name = name.strip()

name = name.title() #capitalize every word in the string
#or name = name.strip().title()

print(f"hello, {name}")

#or
print("hello, " + name)

#or
print("hello,", name) 

# the comma separate/space the variables -- the + signal concatenated string and variable

#or
print("hello, ", end="")
print(name)




#FINAL CODE
# Ask user for their name
name = input("What's your name? ").strip().title()
#split user's name into first name and last name
first, last = name.split(" ")

#say hello to user
print(f"hello, {first}")




# princt function - documentation
# #print(*objects, sep=' ', end='\n') // *objects means can take any number of objects, separators, \n means new line


#########################################################################################

# SECOND PART

name = input("What's your name? ")
hello()
print(name)
# this code will not work because is missing the def = define the hello()

def hello():
    print("Hello")
name = input("What's your name? ")
hello()
print(name)

# or

def hello(to):
    print("Hello,", to)
    
name = input("What's your name? ")
hello(name)

#or

def hello(to="world"):
    print("Hello,", to)

hello()    
name = input("What's your name? ")
hello(name)



# RIGHT WAY: MAIN CODE AT THE TOP

def main():
    name = input("What's your name? ")
    hello(name)
    
def hello(to="world"):
    print("Hello,", to)
    
main()



#or

def main():
    name = input("What's your name? ")
    hello(name)
    
def hello():
    print("Hello,", name)
    
main()

#or

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))
    
def square(n):
    return n * n 
    #or return pow(n, 2) // pow(number, exponent)

main()




"""
Este também é um comentário de várias linhas
usando uma string tripla.


What this indicates as follows is this--
the name of this function is, of course print.
Then there's a parenthesis over here and another close parenthesis way
over there.
Everything inside of those parentheses are
the arguments, the potential arguments, to the function.
However, when we're looking at these arguments
in the documentation like this, there's technically a different term
that we would use.
These are technically the parameters to the function.
So when you're talking about what you can pass to a function
and what those inputs are called, those are parameters.
When you actually use the function and pass
in values inside of those parentheses, those inputs,
those values are arguments.
So we're talking about the exact same thing-- parameters and arguments are
effectively the same thing, but the terms you
use from looking at the problem from different directions.


"""

# checking terminal
# python hello.py