from random import randint
 
def crystal_generator():
    listOfCrystals = ["Dolomite", "Blue Opal", "Astrophyllite" , "Azurite" , "Tiger's Eye", "Blue Lace" ]
    random_number = randint(0,len(listOfCrystals))
    print (random_number)
    crystal = listOfCrystals[random_number]
    return crystal
