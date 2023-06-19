from app import db, app
from app.models import (
    Supplier,
    RawMaterial,
    RawMaterialType,
    Recipe,
    RecipeType,
    IngredientCategory,
    Ingredient,
)

with app.app_context():
    sourdough_type = db.session.execute(
        db.select(RecipeType).filter_by(name="Sourdough")
    ).scalar_one()
    print(sourdough_type)

    types = ["Liquid", "Starter", "Yeast"]
    rmts = (
        db.session.execute(
            db.select(RawMaterialType).filter(RawMaterialType.name.in_(types))
        )
        .scalars()
        .all()
    )
    print(rmts)

    recipes = db.session.execute(db.select(Recipe)).scalars().all()
    print(recipes)
    # stmt = select(RawMaterialType).where(RawMaterialType.type.in_(types))
    #     raw_material_types = db.session.execute(stmt).scalars().all()

    recipe_1 = db.session.execute(db.select(Recipe).filter_by(id=1)).scalar_one()

    print(recipe_1)
