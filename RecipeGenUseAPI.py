import operator
import random
import requests
import json
#initalized vars 

yes = set(['yes','y','Y',''])
no = set(['no','n','N'])
choice = 'yes' #yes, no and choice used to restart program


#Build countArray
countArray = {} #initialize array that counts # of recipes chosen
for key in RecipeCatalog:
	countArray[key] = 0 #builds array that has keys of recipe and values(times eaten) of 0 b/c starting with 0 
	 

#While loop to continue on user request
while (choice in yes):
    input('Press Enter to Generate a Random Recipe... \n')

    #generates random int for use in the URL
    randint= random.randint(0,100)

    #allows user to input a type of food they want in recipe
    foodinput = input('Want a recipe? Well, what kind of food would you like to eat? \n')

    #output simple JSON request to recipe API
    response=requests.get("https://api.edamam.com/search?q={0}&app_id=2876e49a&app_key=523091b1d1951ab568a7a2c496c85447&from={1}&to={2}".format(foodinput, randint, randint+1))
    data=response.json()

    while data['hits'] == []:
    	response=requests.get("https://api.edamam.com/search?q={0}&app_id=2876e49a&app_key=523091b1d1951ab568a7a2c496c85447&from={1}&to={2}".format(foodinput,randint, randint+1))
    	data=response.json()

    #finds recipe name
    Recipe = data['hits'][0]['recipe']['label']
    print("\nRecipe: \n\n", Recipe)

    #loops through ingredients
    ingredientList = data['hits'][0]['recipe']['ingredients']
    print("\nIngredients: \n")
    for i in ingredientList:
    	print(i['text'])
	
	#Below is the validation to restart the recipe generation
    choice = input('Would you like to restart? (Y/N)')
	
    if (choice in no):
        break 
    elif (choice in yes):
        choice in yes
    else:
        print("Please respond with 'Y' or 'N'")
        choice = input('Let''s ask again... Would you like to restart? (Y/N)')


#End of While Loop




