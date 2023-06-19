from app import app, db
from flask import jsonify, request
from app.models import *


@app.route("/recipes")
def api_recipes():
    recipes = db.session.execute(db.select(Recipe)).scalars().all()
    if recipes:
        return [recipe.__json__() for recipe in recipes], 200


@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe_by_id(recipe_id):
    recipe = db.session.execute(db.select(Recipe).filter_by(id=recipe_id)).scalar_one()
    return recipe.__json__(), 200


@app.route("/recipes/delete/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = db.session.execute(db.select(Recipe).filter_by(id=recipe_id)).scalar_one()
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        recipes = db.session.execute(db.select(Recipe)).scalars().all()
        return [recipe.__json__() for recipe in recipes], 200
    else:
        return jsonify({"error": "recipe not found"}), 404


@app.route("/raw_materials", methods=["GET"])
def get_raw_materials():
    type_in = request.args.get("type-in")
    if type_in:
        types = type_in.split(",")
        raw_material_types = (
            db.session.execute(
                db.select(RawMaterialType).filter(RawMaterialType.name.in_(types))
            )
            .scalars()
            .all()
        )
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


@app.route("/recipes/new", methods=["POST"])
def create_recipe():
    recipe_type = db.session.execute(
        db.select(RecipeType).filter_by(name=request.json["type"])
    ).scalar_one()
    recipe = Recipe(name=request.json["name"], recipe_type=recipe_type, image_url="")
    db.session.add(recipe)
    db.session.commit()
    return recipe.__json__(), 200


@app.route("/ingredients/new", methods=["POST"])
def create_ingredient():
    print(request.json)
    ingredient_category = db.session.execute(
        db.select(IngredientCategory).filter_by(name=request.json["category"])
    ).scalar_one()
    ingredient = Ingredient(
        recipe_id=request.json["recipe"]["id"],
        raw_material_id=request.json["rawMaterial"]["id"],
        ingredient_category=ingredient_category,
        quantity=request.json["quantity"],
    )
    db.session.add(ingredient)
    db.session.commit()
    return ingredient.__json__(), 200


# http://localhost:8080/recipes/new
# http://localhost:8080/ingredients/new
