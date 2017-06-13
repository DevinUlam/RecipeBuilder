
#initalized vars 
restart = "Y"
yes = set(['yes','y','Y',''])
no = set(['no','n','N'])
choice = 'yes'
i=0
j=0
k=0
import random

RecipeCatalog = {
	1: 'Chicken Fried Rice \n',
	2: 'Pad Thai \n',
	3: 'Chili \n'}
	
Ingredients = {
	1:
    "1 egg \n"
	"1 tbsp h2o \n"
	"1 tbsp vegetable oil \n"
	"1 onion, chopped \n"
	"2 cups cooked white rice, cold \n"
	"2 tbsp soy sauce \n"
	"1 tsp ground black pepper \n"
	"1 cup cooked, chopped chicken meat \n",
    
    	2:"1 (12 ounce) package of rice noodles \n"
	"2 tbsp butter \n"
	"1/4 cup vegetable oil \n"
	"1 lb boneless chicken breast \n"
	"4 eggs \n"
	"2 tbsp soy sauce \n"
	"1 tbsp white wine vinegar \n"
	"2 cups bena sprouts \n",
    
    3:"1 1/2 pounds lean ground beef \n"
    "1 onion, chopped \n"
    "1 small green bell pepper, chopped \n"
    "2 garlic cloves, minced \n"
    "2 (16-ounce) cans red kidney beans, rinsed and drained \n"
    "2 (14-1/2-ounce) cans diced tomatoes \n"
    "2 to 3 tablespoons chili powder \n"
    "1 teaspoon salt \n"
    "1 teaspoon pepper \n"
    "1 teaspoon ground cumin \n"

}

Steps = {
	1:"1) In a small bowl, beat egg with water \n"
	"2) Melt butter in a large skillet over medium low heat. \n"
	"3) Add egg and leave flat for 1 to 2 minutes. \n"
	"4) Remove from skillet and cut into shreds. \n"
	"5) Heat oil in same skillet; add onion and saute until soft. \n"
	"6) Add rice, soy sauce, pepper and chicken. \n"
	"7) Stir fry together for about 5 minutes, then stir in egg. Serve hot. \n",

    2:"1) Soak rice noodles in cold water 30 to 50 minutes, or until soft. Drain, and set aside.\n"
    "2) Heat butter in a wok or large heavy skillet. Saute chicken until browned. \n"
    "3) Remove, and set aside. Heat oil in wok over medium-high heat. \n"
    "4) Crack eggs into hot oil, and cook until firm. \n"
    "5) Stir in chicken, and cook for 5 minutes. \n"
    "6) Add softened noodles, and vinegar, fish sauce, sugar and red pepper. Adjust seasonings to taste. \n"
    "7) Mix while cooking, until noodles are tender. \n"
    "8) Add bean sprouts, and mix for 3 minutes. \n",

    3:"1) Cook first 4 ingredients in a large skillet over medium-high heat. \n"
    "2) Stir until beef crumbles and is no longer pink; drain. \n"
    "3) Place mixture in 5-quart slow cooker; stir in beans and remaining ingredients. \n" 
    "4) Cook at HIGH 3 to 4 hours or at LOW 5 to 6 hours. \n"
    "Notes: If you want to thicken this saucy chili, stir in finely crushed saltine crackers until the desired thickness is achieved. \n"
}
    
#While loop to continue on user request
while (choice in yes):
    input('Press Enter to Generate a Random Recipe... \n')
    recipenum = random.randint(1,3)
    print("Recipe:\n",RecipeCatalog[recipenum])
    print("Ingredients: \n", Ingredients[recipenum], "\n")
    print("Steps: \n", Steps[recipenum], "\n")

#Favorite Recipe Counting
    
    if recipenum == 1:
        i=i+1
    elif recipenum == 2:
        j=j+1
    else:
        k=k+1
    
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

#Favorite Recipe Determination

countArray=(i,j,k) #would use a loop to load this array if had more recipes... Maybe I will do this before Sunday
countFavRecipe = max(countArray)
numFavRecipe = 1 + countArray.index(max(countArray)) #add one due to indexing starting at 0

print("\nYour favorite recipe was: ", RecipeCatalog[numFavRecipe])
