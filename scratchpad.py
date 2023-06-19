from app.models import Recipe

recipes = Recipe.get_recipes()
print(recipes)
