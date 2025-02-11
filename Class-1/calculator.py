x = input("What's x?")
y = input("What's y?")

z = int(x) + int(y)

print (z)

#or

x = int(input("What's x? "))
y = int(input("What's y? "))


print (x + y)

#or

print(int(input("What's x? ")) + int(input("What's y? ")))


#or

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}") #including commas to the number

# round(number[, ndigits]) // you can use this formula to round numbers / ndigits means the number of digits you want to round



#########################################################

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2) # you can use this formula to round numbers to a 2 digits result

print(f"{z:.2f}")   #the way you specify using a string how much digits you want to round

