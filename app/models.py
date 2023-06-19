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

    def __json__(self):
        return {
            "id": self.id,
            "name": self.name,
            "contact_first_name": self.contact_first_name,
            "contact_last_name": self.contact_last_name,
            "telephone_number": self.telephone_number,
            "email_address": self.email_address,
        }


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

    def __json__(self):
        return {
            "id": self.id,
            "name": self.name,
            "packSize": self.pack_size,
            "price": self.price,
            "type": RawMaterialType.query.get(self.raw_material_type_id).name,
            "supplier": Supplier.query.get(self.supplier_id).__json__(),
        }


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

    def __json__(self):
        return {
            "id": self.id,
            "name": self.name,
            "imageUrl": self.image_url,
            "type": RecipeType.query.get(self.recipe_type_id).name,
            "ingredients": [ingredient.__json__() for ingredient in self.ingredients],
        }


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

    def __json__(self):
        return {
            "id": self.id,
            "category": IngredientCategory.query.get(self.ingredient_category_id).name,
            "quantity": self.quantity,
            "rawMaterial": RawMaterial.query.get(self.raw_material_id).__json__(),
        }
