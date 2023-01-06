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
            match rec.get_type():
                case "starter":
                    self.recipes_list["starter"].append(rec)
                case "lunch":
                    self.recipes_list["lunch"].append(rec)
                case "dessert":
                    self.recipes_list["dessert"].append(rec)
                    
                    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        #... Your code here ...

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        #... Your code here ...
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        #... Your code here ...