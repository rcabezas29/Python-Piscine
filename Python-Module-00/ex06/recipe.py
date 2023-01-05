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
    print(cookbook[name])
    
def delete_recipe(name):
    cookbook.pop(name)
    
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
