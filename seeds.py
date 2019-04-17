from app import app, db
from models.meal import Meal
from models.rating import Rating
from models.user import UserSchema
user_schema = UserSchema()

with app.app_context():
    db.drop_all() # drop all our tables
    db.create_all() #remake our tables

    jess, errors = user_schema.load({
        'username': 'mejess',
        'email': 'mejess@email.com',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)

    db.session.add(jess)


    james, errors = user_schema.load({
        'username': 'jim',
        'email': 'jim@email.com',
        'password': 'password',
        'password_confirmation': 'password'
    })

    if errors:
        raise Exception(errors)

    db.session.add(james)

with app.app_context():
    db.drop_all()
    db.create_all()

    fish_chips = Meal(
    meal_name='fish and chips',
    meal_image='https://eatbychloe.com/wp-content/uploads/2018/02/Fish-n-Chips-3_preview-1-1.jpg',
    taste_rating=4.5,
    more_info='very tasty and fully vegan everything!',
    restaurant_name='ByChloe',
    restaurant_location='Tower Bridge',
    experience_rating=3,
    creator=jess
    )

    fish_chips = Meal(
    meal_name='fish and chips',
    meal_image='https://secretldn.com/wp-content/uploads/2018/10/vegan-fish-chips-hackney.jpg',
    taste_rating=4,
    more_info='all vegan fish and chips!',
    restaurant_name='Sutton and Sons',
    restaurant_location='Hackney',
    experience_rating=3,
    restaurant_link='https://www.suttonandsons.co.uk/wp-content/uploads/2018/10/Sutton-and-sons-vegan-october-2018.pdf',
    creator=jess
    )

    pie = Meal(
    meal_name='Pie',
    meal_image='http://www.mildreds.co.uk/content/uploads/2016/02/City_Pantry8276.jpg',
    taste_rating=4.5,
    more_info='Mushroom and Ale',
    restaurant_name='Mildreds',
    restaurant_location='Soho',
    experience_rating=5,
    restaurant_link='http://www.mildreds.co.uk/soho/soho-mains/',
    creator=james
    )

    pie = Meal(
    meal_name='Pie',
    meal_image='https://www.globalblue.com/destinations/uk/london/article763133.ece/alternates/LANDSCAPE2_640/young_vegans_pie_mash.jpg',
    taste_rating=4.5,
    more_info='Steak(vegan) and Ale',
    restaurant_name='Sutton and Sons',
    restaurant_location='Hackney',
    experience_rating=4,
    restaurant_link='https://www.suttonandsons.co.uk/wp-content/uploads/2018/10/Sutton-and-sons-vegan-october-2018.pdf',
    creator=james
    )

    fry_up = Meal(
    meal_name='Fry-up',
    meal_image='https://www.touristengland.com/wp-content/uploads/2018/02/The-Retreat-Kitchen.-Image-by-RomyUK.jpg',
    meal_price=10.95,
    taste_rating=3,
    more_info='One of the very few vegan restaurants in Richmond. Its a small vegan cafe.',
    restaurant_name='The Retreat Kitchen',
    restaurant_location='Richmond',
    experience_rating=3,
    restaurant_link='http://www.mildreds.co.uk/kings-cross/kings-cross-brunch/',
    creator=james
    )

    fry_up = Meal(
    meal_name='Fry-up',
    meal_image='https://www.thetimes.co.uk/imageserver/image/methode%2Fsundaytimes%2Fprod%2Fweb%2Fbin%2F8bd6aac4-012f-11e8-9830-aa0ac4f2bc04.jpg?crop=2250%2C1266%2C0%2C117&resize=2400',
    taste_rating=4,
    more_info='',
    restaurant_name='Mildreds',
    restaurant_location='Kings Cross',
    experience_rating=4.5,
    restaurant_link='http://www.mildreds.co.uk/kings-cross/kings-cross-brunch/',
    creator=jess
    )

    fry_up = Meal(
    meal_name='Fry-up',
    meal_image='https://images.immediate.co.uk/volatile/sites/2/2018/11/DSC_4337-706fe05.jpg?quality=45&resize=1880,808',
    meal_price=11.50,
    taste_rating=4.5,
    more_info='One of the best.',
    restaurant_name='byChloe',
    restaurant_location='Regents Street',
    experience_rating=4,
    restaurant_link='https://eatbychloe.com/wp-content/uploads/2018/01/ADA_byCHLOE_UK_TakeOut_March19.pdf',
    creator=jess
    )

    fry_up = Meal(
    meal_name='Fry-up',
    meal_image='http://crummbs.co.uk/wp-content/uploads/2018/11/IMG_2569.jpg',
    taste_rating=3,
    more_info='Londons first all vegan pub.',
    restaurant_name='Spread Eagle',
    restaurant_location='Homerton',
    experience_rating=4,
    restaurant_link='https://static1.squarespace.com/static/59fcb45290bade7d4faab378/t/5cb1cdc3e79c70e52f1b9aaf/1555156422277/SE_BRUNCH_APR19_no+bleed.pdf',
    creator=jess
    )

    fry_up = Meal(
    meal_name='Fry-up',
    meal_image='https://static.standard.co.uk/s3fs-public/thumbnails/image/2018/11/01/09/tyf2.jpg?width=1368&height=912&fit=bounds&format=pjpg&auto=webp&quality=70',
    meal_price=13.5,
    taste_rating=4.5,
    more_info='nice!',
    restaurant_name='Tell your friends',
    restaurant_location='Parsons Green',
    experience_rating=4.5,
    restaurant_link='https://www.tellyourfriendsldn.com/wp-content/uploads/sites/80/2019/04/TYF-SUN-MENU.pdf',
    creator=jess
    )

    mac_cheese = Meal(
    meal_name='mac n cheese',
    meal_image='http://coveteur.com/wp-content/uploads/2017/02/By_Chloe-17-homepage-1280x720.jpg',
    meal_price=4.80,
    taste_rating=4.5,
    more_info='One of the best.',
    restaurant_name='byChloe',
    restaurant_location='Regents Street',
    experience_rating=4,
    restaurant_link='https://eatbychloe.com/wp-content/uploads/2018/01/ADA_byCHLOE_UK_TakeOut_March19.pdf',
    creator=jess
    )

    pancakes = Meal(
    meal_name='Pancakes',
    meal_image='https://www.luxsphere.co/wp-content/uploads/Farmacy-Gluten-free-pancakes-notting-hill-.jpg',
    meal_price=11.50,
    taste_rating=4.5,
    more_info='yummy!',
    restaurant_name='Farmacy',
    restaurant_location='Notting Hill',
    experience_rating=4.5,
    restaurant_link='https://farmacylondon.com/menu-2019-march.pdf',
    creator=jess
    )

    pancakes = Meal(
    meal_name='Pancakes',
    meal_image='https://s3-media1.fl.yelpcdn.com/bphoto/NyDTPS1ixS1c-A3d3MqRyQ/o.jpg',
    meal_price=7,
    taste_rating=4,
    more_info='Airy, modern self-service cafe offering creative meat-free buffet dishes from breakfast to dinner.',
    restaurant_name='Ethos',
    restaurant_location='Fitzrovia',
    experience_rating=4.5,
    restaurant_link='http://www.ethosfoods.com/wp-content/uploads/2018/12/Winter-Breakfast-Menu-.pdf',
    creator=jess
    )

    pancakes = Meal(
    meal_name='Pancakes',
    meal_image='https://assets.londonist.com/uploads/2019/02/i875/kk_food_drink-grainlook-153.jpg',
    meal_price=9,
    taste_rating=4,
    more_info='All vegan. Really cool vibes!',
    restaurant_name='Kalifornia Kitchen',
    restaurant_location='Fitzrovia',
    experience_rating=4.5,
    restaurant_link='https://www.kaliforniakitchen.co.uk/our-food',
    creator=jess
    )

    pancakes = Meal(
    meal_name='Pancakes',
    meal_image='https://assets.londonist.com/uploads/2019/02/i875/39575571_340721176470881_8818232895719079936_n.jpg',
    meal_price=9,
    taste_rating=4,
    more_info='All vegan. Really cool vibes!',
    restaurant_name='WAVE',
    restaurant_location='Hackney',
    experience_rating=3,
    restaurant_link='https://www.kaliforniakitchen.co.uk/our-food',
    creator=jess
    )

    nachos = Meal(
    meal_name='Nachos',
    meal_image='https://londontheinside.com/wp-content/uploads/2016/05/Farmacy-Nachos-e1463050169362.jpg',
    meal_price=14.50,
    taste_rating=4.5,
    more_info='yummy!',
    restaurant_name='Farmacy',
    restaurant_location='Notting Hill',
    experience_rating=4.5,
    restaurant_link='https://farmacylondon.com/menu-2019-march.pdf',
    creator=jess
    )

    roast_dinner = Meal(
    meal_name='Roast dinner',
    meal_image='https://i1.wp.com/www.sophielaetitia.blog/wp-content/uploads/2019/01/PB110030.jpg?w=2880&ssl=1',
    meal_price=15,
    taste_rating=4.5,
    more_info='Delicious Sunday Roast!',
    restaurant_name='Tell your friends',
    restaurant_location='Parsons Green',
    experience_rating=4.5,
    restaurant_link='https://www.tellyourfriendsldn.com/wp-content/uploads/sites/80/2019/04/TYF-SUN-MENU.pdf',
    creator=jess
    )

    roast_dinner = Meal(
    meal_name='Roast dinner',
    meal_image='https://pbs.twimg.com/media/DbZ2qNWXcAAo0pn.jpg:large',
    meal_price=16,
    taste_rating=4.5,
    more_info='Roast butternut squash, za’atar, wild mushrooms, cranberry with vegan gravy',
    restaurant_name='The Phene',
    restaurant_location='Parsons Green',
    experience_rating=5,
    restaurant_link='https://www.thephene.com/wp-content/uploads/sites/54/2019/03/Sunday-lunch-March.pdf',
    creator=jess
    )

    chicken_bites = Meal(
    meal_name='Chicken bites',
    meal_image='https://i2.wp.com/www.sophielaetitia.blog/wp-content/uploads/2019/01/PB110031.jpg?w=2880&ssl=1',
    meal_price=7,
    taste_rating=4,
    more_info='Delicious mock chicken!',
    restaurant_name='Tell your friends',
    restaurant_location='Parsons Green',
    experience_rating=4.5,
    restaurant_link='https://www.tellyourfriendsldn.com/wp-content/uploads/sites/80/2019/04/TYF-SUN-MENU.pdf',
    creator=jess
    )

    burger = Meal(
    meal_name='Burger',
    meal_image='https://images.happycow.net/venues/1024/12/01/hcmp120169_458971.jpeg',
    meal_price=14.50,
    taste_rating=4,
    more_info='Moving mountains burger with cashew cheese!',
    restaurant_name='Tell your friends',
    restaurant_location='Parsons Green',
    experience_rating=4,
    restaurant_link='https://www.tellyourfriendsldn.com/wp-content/uploads/sites/80/2019/04/TYF-SUN-MENU.pdf',
    creator=jess
    )

    burger = Meal(
    meal_name='Burger',
    meal_image='https://pbs.twimg.com/media/DuIWlJZWwAARqIf.jpg:large',
    taste_rating=4,
    more_info='Moving mountains burger!',
    restaurant_name='The Alchemist',
    restaurant_location='Covent Garden',
    experience_rating=4.5,
    restaurant_link='https://thealchemist.uk.com/menus/food-all-day-menu/',
    creator=jess
    )

    chicken_ceasar_salad = Meal(
    meal_name='Chicken ceasar salad',
    meal_image='https://sofreshnsogreen.com/wp-content/uploads/2015/06/DSC_0446-1170x778.jpg',
    meal_price=10.50,
    taste_rating=4,
    more_info='Blackened tempeh, romaine lettuce, kale & caesar sauce',
    restaurant_name='Kalifornia Kitchen',
    restaurant_location='Fitzrovia',
    experience_rating=4.5,
    restaurant_link='https://www.kaliforniakitchen.co.uk/our-food',
    creator=jess
    )

    pizza = Meal(
    meal_name='Pizza',
    meal_image='https://www.pi-pizza.co.uk/img/header-image.jpg',
    meal_price=12.50,
    taste_rating=5,
    more_info='Order vegan. Mushroom Medley - Shiitake, oyster, field, chestnut mushrooms, garlic, thyme, shaved vegan parmesan',
    restaurant_name='Pi Pizza',
    restaurant_location='Battersea',
    experience_rating=5,
    restaurant_link='https://battersea.pi-pizza.co.uk/battersea-rise-menu',
    creator=jess
    )

    pizza = Meal(
    meal_name='Pizza',
    meal_image='https://eco-age.com/sites/default/files/styles/image_gallery/public/images/gallery/18-11/screen_shot_2018-11-21_at_11.02.20_1.png?itok=rl3VUSXN',
    taste_rating=5,
    more_info='The Vegan Temptations (ricotta, kale and blueberries) with extra mushrooms on a hemp base. ',
    restaurant_name='PickyWops',
    restaurant_location='Peckham',
    experience_rating=3,
    creator=jess
    )



    rating1 = Rating(rating=4.2, meal=fish_chips)
    rating2 = Rating(rating=3.5, meal=fish_chips)
    rating3 = Rating(rating=2, meal=fish_chips)

    rating4 = Rating(rating=5, meal=mac_cheese)
    rating5 = Rating(rating=2.5, meal=mac_cheese)

    rating6 = Rating(rating=5, meal=pizza)
    rating7 = Rating(rating=2.5, meal=pizza)

    rating8 = Rating(rating=5, meal=chicken_ceasar_salad)

    rating9 = Rating(rating=2.5, meal=burger)
    rating10 = Rating(rating=5, meal=burger)
    rating11= Rating(rating=2.5, meal=burger)

    rating12 = Rating(rating=5, meal=roast_dinner)
    rating13 = Rating(rating=3, meal=roast_dinner)
    rating14 = Rating(rating=5, meal=roast_dinner)
    rating15 = Rating(rating=2, meal=roast_dinner)


    db.session.add(mac_cheese)
    db.session.add(fish_chips)
    db.session.add(fry_up)
    db.session.add(nachos)
    db.session.add(pancakes)
    db.session.add(pie)
    db.session.add(pizza)
    db.session.add(burger)
    db.session.add(roast_dinner)
    db.session.add(chicken_bites)
    db.session.add(rating1)
    db.session.add(rating2)
    db.session.add(rating3)
    db.session.add(rating4)
    db.session.add(rating5)
    db.session.add(rating6)
    db.session.add(rating7)
    db.session.add(rating8)
    db.session.add(rating9)
    db.session.add(rating10)
    db.session.add(rating11)
    db.session.add(rating12)
    db.session.add(rating13)
    db.session.add(rating14)
    db.session.add(rating15)


    db.session.commit()
