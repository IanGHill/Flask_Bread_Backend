from app import app
from app.models import *


@app.route("/recipes")
def api_recipes():
    recipes = Recipe.query.all()

    return [recipe.__json__() for recipe in recipes]


@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe_by_id(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    return recipe.__json__()
