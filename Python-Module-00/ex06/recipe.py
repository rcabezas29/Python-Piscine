cookbook = {}

def initialize():
    cookbook['Sandwich'] = {
        "ingredients": ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal": "lunch",
        "prep_time": 10
    }
    
    cookbook['Cake'] = {
        "ingredients": ['flour', 'sugar', 'eggs'],
        "meal": "dessert",
        "prep_time": 60
    }
    
    cookbook['Salad'] = {
        "ingredients": ['avocado', 'arugula', 'tomatoes'],
        "meal": "lunch",
        "prep_time": 15
    }
    
def print_recipes_names():
    for r in cookbook:
        print(r)
        
def print_recipe(name):
    try:
        recipe = cookbook[name]
        print(f'Ingredients list: {recipe["ingredients"]}')
        print(f'To be eaten for {recipe["meal"]}.')
        print(f'Takes {recipe["prep_time"]} minutes of cooking.\n')
    except:
        print("Recipe not found")
    
def delete_recipe(name):
    try:
        cookbook.pop(name)
    except:
        print("Recipe not found")
    
def add_recipe():
    try:
        name = input("Enter a name: ")
        ingredients = input("Enter ingredients (separated by commas): ").split(',')
        meal = input("Enter meal type: ")
        prep_time = int(input("Enter a preparation time: "))
    except ValueError:
        print("Wrong input")
        return
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }

if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    initialize()
    while True:
        print("List of available option:\n \
        1: Add a recipe\n \
        2: Delete a recipe\n \
        3: Print a recipe\n \
        4: Print the cookbook\n \
        5: Quit\n")

        option = input("Select an option: \n")
        try:
            assert option.isnumeric() and int(option) > 0 and int(option) < 6, "Sorry, this option does not exist."
        except AssertionError as msg:
            print(msg)

        if int(option) == 1:
            add_recipe()
        elif int(option) == 2:
            name = input("Please enter a recipe name to delete it:\n")
            delete_recipe()
        elif int(option) == 3:
            name = input("Please enter a recipe name to get its details:\n")
            print_recipe(name)
        elif int(option) == 4:
            print_recipes_names()
        elif int(option) == 5:
            print("Cookbook closed. Goodbye!")
            exit(0)