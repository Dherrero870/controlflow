number = [10,9,8,7,6,5,4,3,2,1,0]
for number in range (10,0,-1):
    print (number)
    cable = input("¿De qué color es el cable que quieres cortar?")
    if cable == "rojo" or number == 0:
        print ("BOOM!!")
        break
    elif cable == "verde":
        print ("VIVIMOS!")
        break
    else:
        continue