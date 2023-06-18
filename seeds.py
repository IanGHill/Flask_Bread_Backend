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
    Ingredient.query.delete()
    IngredientCategory.query.delete()
    Recipe.query.delete()
    RecipeType.query.delete()
    RawMaterial.query.delete()
    RawMaterialType.query.delete()
    Supplier.query.delete()

    shipton_mill = Supplier(
        name="Shipton Mill",
        contact_first_name="Bob",
        contact_last_name="Miller",
        telephone_number="07999123456",
        email_address="orders@shiptonmill.co.uk",
    )
    mungoswells = Supplier(
        name="Mungoswells",
        contact_first_name="Alison",
        contact_last_name="Miller",
        telephone_number="07999123456",
        email_address="orders@mungoswells.co.uk",
    )
    morrisons = Supplier(
        name="Morrisons",
        contact_first_name="Don",
        contact_last_name="Morrison",
        telephone_number="07999123456",
        email_address="orders@morrisons.co.uk",
    )
    wholefoods = Supplier(
        name="Wholefoods Online",
        contact_first_name="Max",
        contact_last_name="Davidson",
        telephone_number="07999123456",
        email_address="orders@wholefoods.co.uk",
    )
    notapplicable = Supplier(
        name="Not Applicable",
        contact_first_name="N/A",
        contact_last_name="N/A",
        telephone_number="N/A",
        email_address="N/A",
    )
    db.session.add(shipton_mill)
    db.session.add(mungoswells)
    db.session.add(morrisons)
    db.session.add(wholefoods)
    db.session.add(notapplicable)
    db.session.commit()

    flour = RawMaterialType(name="Flour")
    liquid = RawMaterialType(name="Liquid")
    other = RawMaterialType(name="Other")
    salt = RawMaterialType(name="Salt")
    yeast = RawMaterialType(name="Yeast")
    starter = RawMaterialType(name="Sourdough Starter")

    db.session.add(flour)
    db.session.add(liquid)
    db.session.add(other)
    db.session.add(salt)
    db.session.add(yeast)
    db.session.add(starter)
    db.session.commit()

    ciabatta_flour = RawMaterial(
        name="Flour - Ciabatta (T00)",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=1000,
        price=1.30,
    )
    einkorn_flour = RawMaterial(
        name="Flour - Einkorn",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=1000,
        price=2.10,
    )
    emmer_flour = RawMaterial(
        name="Flour - Emmer",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=1000,
        price=1.75,
    )
    granary_flour = RawMaterial(
        name="Flour - Granary",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=1000,
        price=1.30,
    )
    khorasan_flour = RawMaterial(
        name="Flour - Khorasan",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=1000,
        price=1.75,
    )
    light_rye_flour = RawMaterial(
        name="Flour - Rye (Light)",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=1000,
        price=1.30,
    )
    white_spelt_flour = RawMaterial(
        name="Flour - Spelt (White)",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=1000,
        price=2.00,
    )
    wholemeal_spelt_flour = RawMaterial(
        name="Flour - Spelt (Wholemeal)",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=1000,
        price=2.23,
    )
    dark_rye_flour = RawMaterial(
        name="Flour - Rye (Dark)",
        raw_material_type=flour,
        supplier=mungoswells,
        pack_size=16000,
        price=12.17,
    )
    wholewheat_flour = RawMaterial(
        name="Flour - Wholewheat",
        raw_material_type=flour,
        supplier=mungoswells,
        pack_size=16000,
        price=14.86,
    )
    extra_strong_flour = RawMaterial(
        name="Flour - Extra Strong",
        raw_material_type=flour,
        supplier=mungoswells,
        pack_size=16000,
        price=13.55,
    )
    strong_bread_flour = RawMaterial(
        name="Flour - Strong Bread",
        raw_material_type=flour,
        supplier=mungoswells,
        pack_size=16000,
        price=16.09,
    )
    t85_flour = RawMaterial(
        name="Flour - T85",
        raw_material_type=flour,
        supplier=mungoswells,
        pack_size=16000,
        price=15.40,
    )
    yq_flour = RawMaterial(
        name="Flour - YQ",
        raw_material_type=flour,
        supplier=shipton_mill,
        pack_size=3000,
        price=4.99,
    )
    ale = RawMaterial(
        name="Ale",
        raw_material_type=liquid,
        supplier=morrisons,
        pack_size=500,
        price=1.25,
    )
    water = RawMaterial(
        name="Water",
        raw_material_type=liquid,
        supplier=notapplicable,
        pack_size=0,
        price=0.00,
    )
    salt_rm = RawMaterial(
        name="Salt",
        raw_material_type=salt,
        supplier=morrisons,
        pack_size=350,
        price=0.80,
    )
    rye_starter = RawMaterial(
        name="Starter - Rye",
        raw_material_type=starter,
        supplier=notapplicable,
        pack_size=0,
        price=0.00,
    )
    wheat_starter = RawMaterial(
        name="Starter - Wheat",
        raw_material_type=starter,
        supplier=notapplicable,
        pack_size=0,
        price=0.00,
    )
    sugar = RawMaterial(
        name="Granulated Sugar",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=1000,
        price=0.80,
    )
    yeast_rm = RawMaterial(
        name="Yeast - Fresh",
        raw_material_type=yeast,
        supplier=morrisons,
        pack_size=100,
        price=0.50,
    )
    blend = RawMaterial(
        name="5 Grain Blend",
        raw_material_type=other,
        supplier=shipton_mill,
        pack_size=1000,
        price=1.30,
    )
    beetroot = RawMaterial(
        name="Beetroot - Roasted",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=200,
        price=1.70,
    )
    sesame_oil = RawMaterial(
        name="Sesame Oil",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=250,
        price=1.80,
    )
    olive_oil = RawMaterial(
        name="Olive Oil",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=750,
        price=2.39,
    )
    dried_sweet_potato = RawMaterial(
        name="Sweet Potato - Dried",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=500,
        price=1.00,
    )
    fresh_sweet_potato = RawMaterial(
        name="Sweet Potato - Fresh",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=1000,
        price=1.00,
    )
    green_olives = RawMaterial(
        name="Olives - Green",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=340,
        price=0.69,
    )
    kalamata_olives = RawMaterial(
        name="Olives - Kalamata",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=335,
        price=1.90,
    )
    pearl_barley = RawMaterial(
        name="Pearl Barley",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=500,
        price=0.53,
    )
    rosemary = RawMaterial(
        name="Rosemary",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=31,
        price=0.72,
    )
    cumin = RawMaterial(
        name="Seeds - Cumin",
        raw_material_type=other,
        supplier=morrisons,
        pack_size=37,
        price=0.80,
    )
    flax_seeds = RawMaterial(
        name="Seeds - Flax",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=1000,
        price=3.89,
    )
    chia_seeds = RawMaterial(
        name="Seeds - Chia",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=1000,
        price=5.89,
    )
    black_sesame_seeds = RawMaterial(
        name="Seeds - Sesame (Black)",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=100,
        price=1.50,
    )
    white_sesame_seeds = RawMaterial(
        name="Seeds - Sesame (White)",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=1000,
        price=4.91,
    )
    pumpkin_seeds = RawMaterial(
        name="Seeds - Pumpkin",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=1000,
        price=6.47,
    )
    sunflower_seeds = RawMaterial(
        name="Seeds - Sunflower",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=1000,
        price=3.67,
    )
    walnuts = RawMaterial(
        name="Walnuts",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=1000,
        price=8.99,
    )
    caraway_seeds = RawMaterial(
        name="Seeds - Caraway",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=100,
        price=3.67,
    )
    miso = RawMaterial(
        name="Miso Paste",
        raw_material_type=other,
        supplier=wholefoods,
        pack_size=300,
        price=3.00,
    )

    db.session.add(ciabatta_flour)
    db.session.add(einkorn_flour)
    db.session.add(emmer_flour)
    db.session.add(granary_flour)
    db.session.add(khorasan_flour)
    db.session.add(light_rye_flour)
    db.session.add(dark_rye_flour)
    db.session.add(white_spelt_flour)
    db.session.add(wholemeal_spelt_flour)
    db.session.add(t85_flour)
    db.session.add(extra_strong_flour)
    db.session.add(strong_bread_flour)
    db.session.add(wholewheat_flour)
    db.session.add(yq_flour)
    db.session.add(ale)
    db.session.add(water)
    db.session.add(salt_rm)
    db.session.add(yeast_rm)
    db.session.add(rye_starter)
    db.session.add(wheat_starter)
    db.session.add(sugar)
    db.session.add(blend)
    db.session.add(beetroot)
    db.session.add(sesame_oil)
    db.session.add(olive_oil)
    db.session.add(dried_sweet_potato)
    db.session.add(fresh_sweet_potato)
    db.session.add(green_olives)
    db.session.add(kalamata_olives)
    db.session.add(pearl_barley)
    db.session.add(rosemary)
    db.session.add(cumin)
    db.session.add(black_sesame_seeds)
    db.session.add(white_sesame_seeds)
    db.session.add(flax_seeds)
    db.session.add(chia_seeds)
    db.session.add(caraway_seeds)
    db.session.add(pumpkin_seeds)
    db.session.add(sunflower_seeds)
    db.session.add(miso)
    db.session.add(walnuts)
    db.session.commit()

    levain = IngredientCategory(name="Levain")
    dough = IngredientCategory(name="Dough")

    db.session.add(levain)
    db.session.add(dough)
    db.session.commit()

    sourdough = RecipeType(name="Sourdough")
    preferment = RecipeType(name="Preferment")
    straight = RecipeType(name="Straight Dough")
    db.session.add(sourdough)
    db.session.add(preferment)
    db.session.add(straight)
    db.session.commit()

    fifty_fifty_ww = Recipe(
        name="50:50 Wholewheat Sourdough",
        recipe_type=sourdough,
        image_url="5050wholewheat.jpg",
    )
    db.session.add(fifty_fifty_ww)
    db.session.commit()
    ingredient1 = Ingredient(
        recipe=fifty_fifty_ww,
        raw_material=wholewheat_flour,
        ingredient_category=levain,
        quantity=1000,
    )
    ingredient2 = Ingredient(
        recipe=fifty_fifty_ww,
        raw_material=water,
        ingredient_category=levain,
        quantity=600,
    )
    ingredient3 = Ingredient(
        recipe=fifty_fifty_ww,
        raw_material=rye_starter,
        ingredient_category=levain,
        quantity=100,
    )
    ingredient4 = Ingredient(
        recipe=fifty_fifty_ww,
        raw_material=wholewheat_flour,
        ingredient_category=dough,
        quantity=2500,
    )
    ingredient5 = Ingredient(
        recipe=fifty_fifty_ww,
        raw_material=strong_bread_flour,
        ingredient_category=dough,
        quantity=3500,
    )
    ingredient6 = Ingredient(
        recipe=fifty_fifty_ww,
        raw_material=water,
        ingredient_category=dough,
        quantity=4700,
    )
    ingredient7 = Ingredient(
        recipe=fifty_fifty_ww,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=140,
    )
    db.session.add(ingredient1)
    db.session.add(ingredient2)
    db.session.add(ingredient3)
    db.session.add(ingredient4)
    db.session.add(ingredient5)
    db.session.add(ingredient6)
    db.session.add(ingredient7)
    db.session.commit()

    focaccia = Recipe(
        name="Focaccia",
        recipe_type=preferment,
        image_url="focaccia.jpg",
    )
    db.session.add(focaccia)
    db.session.commit()

    chia_flax_sd = Recipe(
        name="Chia & Flaxseed Sourdough",
        recipe_type=sourdough,
        image_url="chia.jpg",
    )
    db.session.add(chia_flax_sd)
    db.session.commit()

    bga_sd = Recipe(
        name="Barley Grain and Ale Sourdough",
        recipe_type=sourdough,
        image_url="BGA.jpg",
    )
    db.session.add(bga_sd)
    db.session.commit()

    ciabatta = Recipe(
        name="Ciabatta",
        recipe_type=preferment,
        image_url="ciabatta.jpg",
    )
    db.session.add(ciabatta)
    db.session.commit()

    morning_rolls = Recipe(
        name="Sourdough Scotch Morning Rolls",
        recipe_type=sourdough,
        image_url="morningrolls.jpg",
    )
    db.session.add(morning_rolls)
    db.session.commit()

    tourte = Recipe(
        name="Tourte au Seigle",
        recipe_type=sourdough,
        image_url="tourte.jpg",
    )
    db.session.add(tourte)
    db.session.commit()

    beetroot_sd = Recipe(
        name="Beetroot, Pumpkin Seed & Cumin Sourdough",
        recipe_type=sourdough,
        image_url="beetroot.jpg",
    )
    db.session.add(beetroot_sd)
    db.session.commit()

    yq_sd = Recipe(
        name="YQ Sourdough",
        recipe_type=sourdough,
        image_url="YQ.jpg",
    )
    db.session.add(yq_sd)
    db.session.commit()

    nydr = Recipe(
        name="New York Deli Rye Sourdough",
        recipe_type=sourdough,
        image_url="NYDR.jpg",
    )
    db.session.add(nydr)
    db.session.commit()

    miso_sd = Recipe(
        name="Miso & Sesame Sourdough",
        recipe_type=sourdough,
        image_url="miso.jpg",
    )
    db.session.add(miso_sd)
    db.session.commit()

    ww_sd = Recipe(
        name="Wholewheat Sourdough",
        recipe_type=sourdough,
        image_url="wholewheat.jpg",
    )
    db.session.add(ww_sd)
    db.session.commit()

    walnut_sd = Recipe(
        name="Walnut Sourdough",
        recipe_type=sourdough,
        image_url="walnut.jpg",
    )
    db.session.add(walnut_sd)
    db.session.commit()

    suppliers = Supplier.query.all()
    raw_material_types = RawMaterialType.query.all()
    raw_materials = RawMaterial.query.all()
    ingredient_categories = IngredientCategory.query.all()
    recipe_types = RecipeType.query.all()
    recipes = Recipe.query.all()
    ingredients = Ingredient.query.all()
    print(suppliers)
    print(raw_material_types)
    print(raw_materials)
    print(ingredient_categories)
    print(recipe_types)
    print(recipes)
    print(ingredients)
