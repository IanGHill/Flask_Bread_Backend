from app import db


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    contact_first_name = db.Column(db.String(64))
    contact_last_name = db.Column(db.String(64))
    telephone_number = db.Column(db.String(20))
    email_address = db.Column(db.String(30))
    raw_materials = db.relationship("RawMaterial", backref="supplier", lazy="dynamic")

    def __repr__(self):
        return "<Supplier {}>".format(self.name)


class RawMaterialType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    raw_materials = db.relationship(
        "RawMaterial", backref="raw_material_type", lazy="dynamic"
    )

    def __repr__(self):
        return "<Raw Material Type {}>".format(self.name)


class RawMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    pack_size = db.Column(db.Integer)
    price = db.Column(db.Float)
    raw_material_type_id = db.Column(db.Integer, db.ForeignKey("raw_material_type.id"))
    supplier_id = db.Column(db.Integer, db.ForeignKey("supplier.id"))
    ingredients = db.relationship("Ingredient", backref="raw_material", lazy="dynamic")

    def __repr__(self):
        return "<Raw Material {}>".format(self.name)


class RecipeType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    recipes = db.relationship("Recipe", backref="recipe_type", lazy="dynamic")

    def __repr__(self):
        return "<Recipe Type {}>".format(self.name)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    image_url = db.Column(db.String(255))
    recipe_type_id = db.Column(db.Integer, db.ForeignKey("recipe_type.id"))
    ingredients = db.relationship("Ingredient", backref="recipe", lazy="dynamic")

    def __repr__(self):
        return "<Recipe {}>".format(self.name)


class IngredientCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    ingredients = db.relationship(
        "Ingredient", backref="ingredient_category", lazy="dynamic"
    )

    def __repr__(self):
        return "<Ingredient Category {}>".format(self.name)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"))
    ingredient_category_id = db.Column(
        db.Integer, db.ForeignKey("ingredient_category.id")
    )
    raw_material_id = db.Column(db.Integer, db.ForeignKey("raw_material.id"))
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return "<Ingredient {}>".format(self.id)
