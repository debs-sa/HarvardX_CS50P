print("meow")
print("meow")
print("meow")

## or ##

i = 3

while i != 0:
    print("meow")
    i = i - 1
    
## OR ##

i = 0

while i < 3:
    print("meow")
    i = i + 1    # or --> i += 1 
    
    
    ##### FOR LOOP ######
    

for i in [0, 1 , 2]:
    print("meow loop")

##or##

for i in range(3): #we use range for numbers
    print("meow loop")


##or##

for _ in range(3):          # if you are using a number and don't care about its value
    print("meow loop")
    

## or just ##

print("meow\n" * 3)

print("meow\n" * 3, end="") # remove additional blank lines



###############################

## asking input from user ##

while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
    
    
###############################

def main():
    number = get_number()
    meow(number)
    
def  get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
    
def meow(n):
    for _ in range(n):
        print("meow")

main()