# https://www.codewars.com/kata/525c65e51bf619685c000059
def cakes(recipe, available):
    # Check if all ingredients in the recipe are available, if not return 0
    # If all ingredients are available, return the minimum floor division out of all ingredients available
    return 0 if not all(ingredient in available for ingredient in recipe) else min([available[ingredient] // recipe[ingredient] for ingredient in recipe])