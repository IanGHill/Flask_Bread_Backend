from app import app, db
from flask import jsonify, request
from app.models import *


@app.route("/recipes")
def api_recipes():
    recipes = Recipe.query.all()
    if recipes:
        return [recipe.__json__() for recipe in recipes], 200


@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe_by_id(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    return recipe.__json__(), 200


@app.route("/recipes/delete/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        recipes = Recipe.query.all()
        return [recipe.__json__() for recipe in recipes], 200
    else:
        return jsonify({"error": "recipe not found"}), 404


@app.route("/raw_materials", methods=["GET"])
def get_raw_materials():
    type_in = request.args.get("type-in")
    if type_in:
        types = type_in.split(",")
        raw_material_types = RawMaterialType.query.filter(
            RawMaterialType.name.in_(types)
        ).all()
        if raw_material_types:
            raw_materials = [
                material
                for type in raw_material_types
                for material in type.raw_materials
            ]
            return [material.__json__() for material in raw_materials], 200
        else:
            return (
                jsonify({"error": "No raw materials found for the given types."}),
                404,
            )
    else:
        return jsonify({"error": "No type parameter provided."}), 400


# http://localhost:8080/recipes/new
# http://localhost:8080/ingredients/new
