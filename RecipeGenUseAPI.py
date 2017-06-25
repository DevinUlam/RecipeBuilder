import operator
import random
import requests
import json
#initalized vars 

yes = set(['yes','y','Y',''])
no = set(['no','n','N'])
#yes, no and choice used to restart program
newfoodchoice = 'yes'

def outputRecipe(food):
	randint= random.randint(0,10)
	file = open("reciperesults.txt","w")

	#output simple JSON request to recipe API
	response=requests.get("https://api.edamam.com/search?q={0}&app_id=2876e49a&app_key=523091b1d1951ab568a7a2c496c85447&from={1}&to={2}".format(food, randint, randint+1))
	data=response.json()
	while data['hits'] == []:
		response=requests.get("https://api.edamam.com/search?q={0}&app_id=2876e49a&app_key=523091b1d1951ab568a7a2c496c85447&from={1}&to={2}".format(food, randint, randint+1))
		data=response.json()

	#finds recipe name
	Recipe = data['hits'][0]['recipe']['label']
	print("\nRecipe: \n\n", Recipe)
	file.write("\nRecipe: \n\n")
	file.write(Recipe)
	file.write("\n")

	#loops through ingredients
	ingredientList = data['hits'][0]['recipe']['ingredients']
	print("\nIngredients: \n")
	file.write("\nIngredients: \n")
	for i in ingredientList:
		print(i['text'])
		file.write(i['text'])
		file.write("\n")
	file.close()

#While loop to continue on user request
while (newfoodchoice in yes):
    

	#allows user to input a type of food they want in recipe
    foodinput = input('\nWant a recipe? Well, what kind of food would you like to eat? \n')

    redo = 'yes'
    while (redo in yes):

    	outputRecipe(foodinput);

    	redo = input('\nWould you like to see another {0} recipe? (Y/N)'.format(foodinput))
    	if (redo in no):
    		break
    			
    	elif (redo in yes):
        	redo in yes
        		
    	else:
        	print("\nPlease respond with 'Y' or 'N'")
        	while (redo not in yes & redo not in no):
        		redo = input('\nLet''s ask again... Would you like to see another {0} recipe? (Y/N)'.format(foodinput))

    newfoodchoice = input('\nWould you like to search another food group? (Y/N)\n')
    if (newfoodchoice in no):
        break
    elif (newfoodchoice in yes):
    	newfoodchoice in yes
    else:
        print("\nPlease respond with 'Y' or 'N'\n")
        redo = input('\nLet''s ask again... search another food group? (Y/N)\n')

#End of While Loop





