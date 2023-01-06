class   Recipe:
    def __init__(self, name, lvl, time, ingredients, r_t, desc=""):
        self.name = name
        if lvl < 1 and lvl > 5:
            print('Level must be between 1 and 5')
            exit(1)
        self.cooking_lvl = lvl
        if time < 0:
            print('Time must be positve')
            exit(1)
        self.cooking_time = time
        self.ingredients = ingredients
        self.description = desc
        if r_t != 'starter' or r_t != 'lunch' or r_t != 'dessert':
            print('The type must be starter, lunch, dessert')
            exit(1)
        self.recipe_type = r_t
    
    def __str__(self):
        txt = f"""
        Name: {self.name}
        Cooking level: {self.cooking_lvl}
        Cooking time: {self.cooking_time}
        Ingredients: {self.ingredients}
        Description: {self.description}
        Recipe type: {self.recipe_type}
        """
        return txt
    
    def get_type(self) -> str:
        return self.recipe_type