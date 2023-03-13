from datetime import datetime
import recipe

class   Book:
    def __init__(self, name: str, recipes_list):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }
        for rec in recipes_list:
            if rec.get_type() == "starter":
                self.recipes_list["starter"].append(rec)
            elif rec.get_type() == "lunch":
                self.recipes_list["lunch"].append(rec)
            elif rec.get_type() == "dessert":
                self.recipes_list["dessert"].append(rec)
                    
                    
    def get_recipe_by_name(self, name) -> recipe:
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for recipe_type in self.recipes_list:
            if name in recipe_type:
                print(str(recipe_type[name]))
                return recipe_type[name]
            

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list:
            return self.recipes_list[recipe_type]
        else:
            print('Recipe type not found')
    
    def add_recipe(self, rec: recipe):
        """Add a recipe to the book and update last_update"""
        self.recipes_list[rec.get_type()].append(rec)