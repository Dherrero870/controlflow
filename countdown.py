number = 10
hasPaintedPoints = False 
while number >= 0:
    if(number >= 8 or number <=2):
        print(number)
    elif not hasPaintedPoints:
        print("...")
        hasPaintedPoints = True 
    number -= 1
print ("Boom!")


