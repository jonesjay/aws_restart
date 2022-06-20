myString = "This is a string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

firststring="water"
secondstring="fall"
thirdstring=firststring + secondstring
print(thirdstring)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color?  ")
car = input("What is your favorite car?  ")

print("{}, you like a {} {}",format(name,color,car))