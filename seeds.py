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
    starter = RawMaterialType(name="Starter")

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

    ingredient8 = Ingredient(
        recipe=focaccia,
        raw_material=ciabatta_flour,
        ingredient_category=levain,
        quantity=400,
    )
    ingredient9 = Ingredient(
        recipe=focaccia,
        raw_material=water,
        ingredient_category=levain,
        quantity=400,
    )
    ingredient10 = Ingredient(
        recipe=focaccia,
        raw_material=yeast_rm,
        ingredient_category=levain,
        quantity=1,
    )
    ingredient11 = Ingredient(
        recipe=focaccia,
        raw_material=ciabatta_flour,
        ingredient_category=dough,
        quantity=600,
    )
    ingredient12 = Ingredient(
        recipe=focaccia,
        raw_material=olive_oil,
        ingredient_category=dough,
        quantity=60,
    )
    ingredient13 = Ingredient(
        recipe=focaccia,
        raw_material=water,
        ingredient_category=dough,
        quantity=320,
    )
    ingredient14 = Ingredient(
        recipe=focaccia,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=20,
    )
    ingredient15 = Ingredient(
        recipe=focaccia,
        raw_material=yeast_rm,
        ingredient_category=dough,
        quantity=8,
    )
    db.session.add(ingredient8)
    db.session.add(ingredient9)
    db.session.add(ingredient10)
    db.session.add(ingredient11)
    db.session.add(ingredient12)
    db.session.add(ingredient13)
    db.session.add(ingredient14)
    db.session.add(ingredient15)
    db.session.commit()

    chia_flax_sd = Recipe(
        name="Chia & Flaxseed Sourdough",
        recipe_type=sourdough,
        image_url="chia.jpg",
    )
    db.session.add(chia_flax_sd)
    db.session.commit()

    ingredient16 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=strong_bread_flour,
        ingredient_category=levain,
        quantity=150,
    )
    ingredient17 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=water,
        ingredient_category=levain,
        quantity=120,
    )
    ingredient18 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=wheat_starter,
        ingredient_category=levain,
        quantity=30,
    )
    ingredient19 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=wholewheat_flour,
        ingredient_category=dough,
        quantity=250,
    )
    ingredient20 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=strong_bread_flour,
        ingredient_category=dough,
        quantity=500,
    )
    ingredient21 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=t85_flour,
        ingredient_category=dough,
        quantity=100,
    )
    ingredient22 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=water,
        ingredient_category=dough,
        quantity=730,
    )
    ingredient23 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=18,
    )
    ingredient24 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=chia_seeds,
        ingredient_category=dough,
        quantity=70,
    )
    ingredient25 = Ingredient(
        recipe=chia_flax_sd,
        raw_material=flax_seeds,
        ingredient_category=dough,
        quantity=70,
    )

    db.session.add(ingredient16)
    db.session.add(ingredient17)
    db.session.add(ingredient18)
    db.session.add(ingredient19)
    db.session.add(ingredient20)
    db.session.add(ingredient21)
    db.session.add(ingredient22)
    db.session.add(ingredient23)
    db.session.add(ingredient24)
    db.session.add(ingredient25)
    db.session.commit()

    bga_sd = Recipe(
        name="Barley Grain and Ale Sourdough",
        recipe_type=sourdough,
        image_url="BGA.jpg",
    )
    db.session.add(bga_sd)
    db.session.commit()

    ingredient26 = Ingredient(
        recipe=bga_sd,
        raw_material=strong_bread_flour,
        ingredient_category=levain,
        quantity=600,
    )
    ingredient27 = Ingredient(
        recipe=bga_sd,
        raw_material=water,
        ingredient_category=levain,
        quantity=480,
    )
    ingredient28 = Ingredient(
        recipe=bga_sd,
        raw_material=wheat_starter,
        ingredient_category=levain,
        quantity=120,
    )
    ingredient29 = Ingredient(
        recipe=bga_sd,
        raw_material=wholewheat_flour,
        ingredient_category=dough,
        quantity=400,
    )
    ingredient30 = Ingredient(
        recipe=bga_sd,
        raw_material=strong_bread_flour,
        ingredient_category=dough,
        quantity=4000,
    )
    ingredient31 = Ingredient(
        recipe=bga_sd,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=100,
    )
    ingredient32 = Ingredient(
        recipe=bga_sd,
        raw_material=water,
        ingredient_category=dough,
        quantity=2400,
    )
    ingredient33 = Ingredient(
        recipe=bga_sd,
        raw_material=ale,
        ingredient_category=dough,
        quantity=1000,
    )
    ingredient34 = Ingredient(
        recipe=bga_sd,
        raw_material=sunflower_seeds,
        ingredient_category=dough,
        quantity=300,
    )
    ingredient35 = Ingredient(
        recipe=bga_sd,
        raw_material=flax_seeds,
        ingredient_category=dough,
        quantity=300,
    )
    ingredient36 = Ingredient(
        recipe=bga_sd,
        raw_material=pearl_barley,
        ingredient_category=dough,
        quantity=350,
    )

    db.session.add(ingredient26)
    db.session.add(ingredient27)
    db.session.add(ingredient28)
    db.session.add(ingredient29)
    db.session.add(ingredient30)
    db.session.add(ingredient31)
    db.session.add(ingredient32)
    db.session.add(ingredient33)
    db.session.add(ingredient34)
    db.session.add(ingredient35)
    db.session.add(ingredient36)
    db.session.commit()

    ciabatta = Recipe(
        name="Ciabatta",
        recipe_type=preferment,
        image_url="ciabatta.jpg",
    )
    db.session.add(ciabatta)
    db.session.commit()

    ingredient37 = Ingredient(
        recipe=ciabatta,
        raw_material=ciabatta_flour,
        ingredient_category=levain,
        quantity=3600,
    )
    ingredient38 = Ingredient(
        recipe=ciabatta,
        raw_material=water,
        ingredient_category=levain,
        quantity=2160,
    )
    ingredient39 = Ingredient(
        recipe=ciabatta,
        raw_material=yeast_rm,
        ingredient_category=levain,
        quantity=5,
    )
    ingredient40 = Ingredient(
        recipe=ciabatta,
        raw_material=ciabatta_flour,
        ingredient_category=dough,
        quantity=4200,
    )
    ingredient41 = Ingredient(
        recipe=ciabatta,
        raw_material=olive_oil,
        ingredient_category=dough,
        quantity=78,
    )
    ingredient42 = Ingredient(
        recipe=ciabatta,
        raw_material=water,
        ingredient_category=dough,
        quantity=4080,
    )
    ingredient43 = Ingredient(
        recipe=ciabatta,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=156,
    )
    ingredient44 = Ingredient(
        recipe=ciabatta,
        raw_material=yeast_rm,
        ingredient_category=dough,
        quantity=30,
    )

    db.session.add(ingredient37)
    db.session.add(ingredient38)
    db.session.add(ingredient39)
    db.session.add(ingredient40)
    db.session.add(ingredient41)
    db.session.add(ingredient42)
    db.session.add(ingredient43)
    db.session.add(ingredient44)
    db.session.commit()

    morning_rolls = Recipe(
        name="Sourdough Scotch Morning Rolls",
        recipe_type=sourdough,
        image_url="morningrolls.jpg",
    )
    db.session.add(morning_rolls)
    db.session.commit()

    ingredient45 = Ingredient(
        recipe=morning_rolls,
        raw_material=strong_bread_flour,
        ingredient_category=levain,
        quantity=3500,
    )
    ingredient46 = Ingredient(
        recipe=morning_rolls,
        raw_material=water,
        ingredient_category=levain,
        quantity=2100,
    )
    ingredient47 = Ingredient(
        recipe=morning_rolls,
        raw_material=wheat_starter,
        ingredient_category=levain,
        quantity=350,
    )
    ingredient48 = Ingredient(
        recipe=morning_rolls,
        raw_material=wholewheat_flour,
        ingredient_category=dough,
        quantity=3500,
    )
    ingredient49 = Ingredient(
        recipe=morning_rolls,
        raw_material=strong_bread_flour,
        ingredient_category=dough,
        quantity=24500,
    )
    ingredient50 = Ingredient(
        recipe=morning_rolls,
        raw_material=extra_strong_flour,
        ingredient_category=dough,
        quantity=4000,
    )
    ingredient51 = Ingredient(
        recipe=morning_rolls,
        raw_material=water,
        ingredient_category=dough,
        quantity=19200,
    )
    ingredient52 = Ingredient(
        recipe=morning_rolls,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=500,
    )
    ingredient53 = Ingredient(
        recipe=morning_rolls,
        raw_material=yeast_rm,
        ingredient_category=dough,
        quantity=1300,
    )
    ingredient54 = Ingredient(
        recipe=morning_rolls,
        raw_material=olive_oil,
        ingredient_category=dough,
        quantity=700,
    )
    ingredient55 = Ingredient(
        recipe=morning_rolls,
        raw_material=sugar,
        ingredient_category=dough,
        quantity=460,
    )

    db.session.add(ingredient45)
    db.session.add(ingredient46)
    db.session.add(ingredient47)
    db.session.add(ingredient48)
    db.session.add(ingredient49)
    db.session.add(ingredient50)
    db.session.add(ingredient51)
    db.session.add(ingredient52)
    db.session.add(ingredient53)
    db.session.add(ingredient54)
    db.session.add(ingredient55)
    db.session.commit()

    tourte = Recipe(
        name="Tourte au Seigle",
        recipe_type=sourdough,
        image_url="tourte.jpg",
    )
    db.session.add(tourte)
    db.session.commit()

    ingredient56 = Ingredient(
        recipe=tourte,
        raw_material=dark_rye_flour,
        ingredient_category=levain,
        quantity=2400,
    )
    ingredient57 = Ingredient(
        recipe=tourte,
        raw_material=water,
        ingredient_category=levain,
        quantity=2400,
    )
    ingredient58 = Ingredient(
        recipe=tourte,
        raw_material=rye_starter,
        ingredient_category=levain,
        quantity=600,
    )
    ingredient59 = Ingredient(
        recipe=tourte,
        raw_material=dark_rye_flour,
        ingredient_category=dough,
        quantity=2400,
    )
    ingredient60 = Ingredient(
        recipe=tourte,
        raw_material=wholewheat_flour,
        ingredient_category=dough,
        quantity=1800,
    )
    ingredient61 = Ingredient(
        recipe=tourte,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=120,
    )
    ingredient62 = Ingredient(
        recipe=tourte,
        raw_material=water,
        ingredient_category=dough,
        quantity=3120,
    )
    db.session.add(ingredient56)
    db.session.add(ingredient57)
    db.session.add(ingredient58)
    db.session.add(ingredient59)
    db.session.add(ingredient60)
    db.session.add(ingredient61)
    db.session.add(ingredient62)
    db.session.commit()

    beetroot_sd = Recipe(
        name="Beetroot, Pumpkin Seed & Cumin Sourdough",
        recipe_type=sourdough,
        image_url="beetroot.jpg",
    )
    db.session.add(beetroot_sd)
    db.session.commit()

    ingredient63 = Ingredient(
        recipe=beetroot_sd,
        raw_material=strong_bread_flour,
        ingredient_category=levain,
        quantity=625,
    )
    ingredient64 = Ingredient(
        recipe=beetroot_sd,
        raw_material=water,
        ingredient_category=levain,
        quantity=500,
    )
    ingredient65 = Ingredient(
        recipe=beetroot_sd,
        raw_material=wheat_starter,
        ingredient_category=levain,
        quantity=125,
    )
    ingredient66 = Ingredient(
        recipe=beetroot_sd,
        raw_material=strong_bread_flour,
        ingredient_category=dough,
        quantity=3675,
    )
    ingredient67 = Ingredient(
        recipe=beetroot_sd,
        raw_material=beetroot,
        ingredient_category=dough,
        quantity=800,
    )
    ingredient68 = Ingredient(
        recipe=beetroot_sd,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=80,
    )
    ingredient69 = Ingredient(
        recipe=beetroot_sd,
        raw_material=water,
        ingredient_category=dough,
        quantity=2600,
    )
    ingredient70 = Ingredient(
        recipe=beetroot_sd,
        raw_material=pumpkin_seeds,
        ingredient_category=dough,
        quantity=800,
    )
    ingredient71 = Ingredient(
        recipe=beetroot_sd,
        raw_material=cumin,
        ingredient_category=dough,
        quantity=22,
    )
    db.session.add(ingredient63)
    db.session.add(ingredient64)
    db.session.add(ingredient65)
    db.session.add(ingredient66)
    db.session.add(ingredient67)
    db.session.add(ingredient68)
    db.session.add(ingredient69)
    db.session.add(ingredient70)
    db.session.add(ingredient71)
    db.session.commit()

    yq_sd = Recipe(
        name="YQ Sourdough",
        recipe_type=sourdough,
        image_url="YQ.jpg",
    )
    db.session.add(yq_sd)
    db.session.commit()

    ingredient72 = Ingredient(
        recipe=yq_sd,
        raw_material=yq_flour,
        ingredient_category=levain,
        quantity=2000,
    )
    ingredient73 = Ingredient(
        recipe=yq_sd,
        raw_material=water,
        ingredient_category=levain,
        quantity=1200,
    )
    ingredient74 = Ingredient(
        recipe=yq_sd,
        raw_material=wheat_starter,
        ingredient_category=levain,
        quantity=400,
    )
    ingredient75 = Ingredient(
        recipe=yq_sd,
        raw_material=yq_flour,
        ingredient_category=dough,
        quantity=5000,
    )
    ingredient76 = Ingredient(
        recipe=yq_sd,
        raw_material=extra_strong_flour,
        ingredient_category=dough,
        quantity=3000,
    )
    ingredient77 = Ingredient(
        recipe=yq_sd,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=180,
    )
    ingredient78 = Ingredient(
        recipe=yq_sd,
        raw_material=water,
        ingredient_category=dough,
        quantity=6000,
    )

    db.session.add(ingredient72)
    db.session.add(ingredient73)
    db.session.add(ingredient74)
    db.session.add(ingredient75)
    db.session.add(ingredient76)
    db.session.add(ingredient77)
    db.session.add(ingredient78)
    db.session.commit()

    nydr = Recipe(
        name="New York Deli Rye Sourdough",
        recipe_type=sourdough,
        image_url="NYDR.jpg",
    )
    db.session.add(nydr)
    db.session.commit()

    ingredient79 = Ingredient(
        recipe=nydr,
        raw_material=dark_rye_flour,
        ingredient_category=levain,
        quantity=200,
    )
    ingredient80 = Ingredient(
        recipe=nydr,
        raw_material=water,
        ingredient_category=levain,
        quantity=120,
    )
    ingredient81 = Ingredient(
        recipe=nydr,
        raw_material=rye_starter,
        ingredient_category=levain,
        quantity=50,
    )
    ingredient82 = Ingredient(
        recipe=nydr,
        raw_material=strong_bread_flour,
        ingredient_category=dough,
        quantity=750,
    )
    ingredient83 = Ingredient(
        recipe=nydr,
        raw_material=wholewheat_flour,
        ingredient_category=dough,
        quantity=50,
    )
    ingredient84 = Ingredient(
        recipe=nydr,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=22,
    )
    ingredient85 = Ingredient(
        recipe=nydr,
        raw_material=water,
        ingredient_category=dough,
        quantity=540,
    )
    ingredient86 = Ingredient(
        recipe=nydr,
        raw_material=caraway_seeds,
        ingredient_category=dough,
        quantity=10,
    )

    db.session.add(ingredient79)
    db.session.add(ingredient80)
    db.session.add(ingredient81)
    db.session.add(ingredient82)
    db.session.add(ingredient83)
    db.session.add(ingredient84)
    db.session.add(ingredient85)
    db.session.add(ingredient86)
    db.session.commit()

    miso_sd = Recipe(
        name="Miso & Sesame Sourdough",
        recipe_type=sourdough,
        image_url="miso.jpg",
    )
    db.session.add(miso_sd)
    db.session.commit()

    ingredient87 = Ingredient(
        recipe=miso_sd,
        raw_material=strong_bread_flour,
        ingredient_category=levain,
        quantity=100,
    )
    ingredient88 = Ingredient(
        recipe=miso_sd,
        raw_material=water,
        ingredient_category=levain,
        quantity=80,
    )
    ingredient89 = Ingredient(
        recipe=miso_sd,
        raw_material=wheat_starter,
        ingredient_category=levain,
        quantity=20,
    )
    ingredient90 = Ingredient(
        recipe=miso_sd,
        raw_material=strong_bread_flour,
        ingredient_category=dough,
        quantity=700,
    )
    ingredient91 = Ingredient(
        recipe=miso_sd,
        raw_material=wholewheat_flour,
        ingredient_category=dough,
        quantity=300,
    )
    ingredient92 = Ingredient(
        recipe=miso_sd,
        raw_material=t85_flour,
        ingredient_category=dough,
        quantity=100,
    )
    ingredient93 = Ingredient(
        recipe=miso_sd,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=17,
    )
    ingredient94 = Ingredient(
        recipe=miso_sd,
        raw_material=water,
        ingredient_category=dough,
        quantity=780,
    )
    ingredient95 = Ingredient(
        recipe=miso_sd,
        raw_material=miso,
        ingredient_category=dough,
        quantity=50,
    )
    ingredient96 = Ingredient(
        recipe=miso_sd,
        raw_material=sesame_oil,
        ingredient_category=dough,
        quantity=15,
    )

    db.session.add(ingredient87)
    db.session.add(ingredient88)
    db.session.add(ingredient89)
    db.session.add(ingredient90)
    db.session.add(ingredient91)
    db.session.add(ingredient92)
    db.session.add(ingredient93)
    db.session.add(ingredient94)
    db.session.add(ingredient95)
    db.session.add(ingredient96)
    db.session.commit()

    ww_sd = Recipe(
        name="Wholewheat Sourdough",
        recipe_type=sourdough,
        image_url="wholewheat.jpg",
    )
    db.session.add(ww_sd)
    db.session.commit()

    ingredient97 = Ingredient(
        recipe=ww_sd,
        raw_material=wholewheat_flour,
        ingredient_category=levain,
        quantity=2000,
    )
    ingredient98 = Ingredient(
        recipe=ww_sd,
        raw_material=water,
        ingredient_category=levain,
        quantity=1200,
    )
    ingredient99 = Ingredient(
        recipe=ww_sd,
        raw_material=wheat_starter,
        ingredient_category=levain,
        quantity=400,
    )
    ingredient100 = Ingredient(
        recipe=ww_sd,
        raw_material=extra_strong_flour,
        ingredient_category=dough,
        quantity=2500,
    )
    ingredient101 = Ingredient(
        recipe=ww_sd,
        raw_material=wholewheat_flour,
        ingredient_category=dough,
        quantity=5500,
    )
    ingredient102 = Ingredient(
        recipe=ww_sd,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=180,
    )
    ingredient103 = Ingredient(
        recipe=ww_sd,
        raw_material=water,
        ingredient_category=dough,
        quantity=6800,
    )

    db.session.add(ingredient97)
    db.session.add(ingredient98)
    db.session.add(ingredient99)
    db.session.add(ingredient100)
    db.session.add(ingredient101)
    db.session.add(ingredient102)
    db.session.add(ingredient103)
    db.session.commit()

    walnut_sd = Recipe(
        name="Walnut Sourdough",
        recipe_type=sourdough,
        image_url="walnut.jpg",
    )
    db.session.add(walnut_sd)
    db.session.commit()

    ingredient104 = Ingredient(
        recipe=walnut_sd,
        raw_material=dark_rye_flour,
        ingredient_category=levain,
        quantity=560,
    )
    ingredient105 = Ingredient(
        recipe=walnut_sd,
        raw_material=t85_flour,
        ingredient_category=levain,
        quantity=560,
    )
    ingredient106 = Ingredient(
        recipe=walnut_sd,
        raw_material=water,
        ingredient_category=levain,
        quantity=1050,
    )
    ingredient107 = Ingredient(
        recipe=walnut_sd,
        raw_material=wheat_starter,
        ingredient_category=levain,
        quantity=245,
    )
    ingredient108 = Ingredient(
        recipe=walnut_sd,
        raw_material=strong_bread_flour,
        ingredient_category=dough,
        quantity=5880,
    )
    ingredient109 = Ingredient(
        recipe=walnut_sd,
        raw_material=salt_rm,
        ingredient_category=dough,
        quantity=140,
    )
    ingredient110 = Ingredient(
        recipe=walnut_sd,
        raw_material=water,
        ingredient_category=dough,
        quantity=4200,
    )
    ingredient111 = Ingredient(
        recipe=walnut_sd,
        raw_material=walnuts,
        ingredient_category=dough,
        quantity=1680,
    )

    db.session.add(ingredient104)
    db.session.add(ingredient105)
    db.session.add(ingredient106)
    db.session.add(ingredient107)
    db.session.add(ingredient108)
    db.session.add(ingredient109)
    db.session.add(ingredient110)
    db.session.add(ingredient111)
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
