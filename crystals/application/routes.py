from random import randint
 
def crystal generator():
    listOfCrystals = ["Dolomite", "Blue Opal", "Green Apatite", "Manganoan Calcite", "Agni Gold Danburite", "Ajoite", "Ametrine", "Astrophyllite" , "Azurite" , "Tiger's Eye", "Angelite", "Blue Lace" ]
    random_number = randint(0,len(listOfCrystals))
    print (random_number)
    crystal = listOfCrystals[random_number]
    return crystal
