from fastfood.models import *

# client1 = Client(user=User.objects.create(email='nikname21@gmail.com', password='defender42'), name='Nursultan Berdiev', card_number='4147565798789009')
# client1.save()
#
# worker1 = Worker(user=User.objects.create(email='altywa1998@gmail.com', password='nono34'), name='Altynai Alieva', position='Checkout operator')
# worker1.save()
#
# shawarma = Food.objects.create(name='Shawarma', start_price=200, type_of_cuisine='Fastfood', calories=500)
# burger = Food.objects.create(name='Burger', start_price=180, type_of_cuisine='Fastfood', calories=350)
# pasta = Food.objects.create(name='Pasta', start_price=450, type_of_cuisine='Italian', calories=400)
# boul = Food.objects.create(name='Boul', start_price=600, type_of_cuisine='Europe', calories=500)
# sushi = Food.objects.create(name='Sushi', start_price=400, type_of_cuisine='Japan', calories=450)
#
# cheese = Ingredient.objects.create(name='cheese', extra_price=80, calories=150)
# chicken = Ingredient.objects.create(name='chicken', extra_price=100, calories=250)
# meat = Ingredient.objects.create(name='meat', extra_price=120, calories=300)
# fish = Ingredient.objects.create(name='fish', extra_price=120, calories=270)
# rice = Ingredient.objects.create(name='rice', extra_price=70, calories=100)
# salad = Ingredient.objects.create(name='salad', extra_price=50, calories=50)
# chicken_eggs = Ingredient.objects.create(name='chicken eggs', extra_price=50, calories=120)
# cottage_cheese = Ingredient.objects.create(name='cottage cheese', extra_price=100, calories=170)
# fries = Ingredient.objects.create(name='fries', extra_price=50, calories=70)
#
# order1 = shawarma.booking.set([cheese, salad, fries], through_defaults={'client': client1, 'worker': worker1})
# order2 = burger.booking.set([chicken, salad], through_defaults={'client': client1, 'worker': worker1})
# order3 = pasta.booking.set([chicken_eggs, cheese, cottage_cheese], through_defaults={'client': client1, 'worker': worker1})
# order4 = boul.booking.set([rice, cheese, fries, salad, cottage_cheese], through_defaults={'client': client1, 'worker': worker1})
# order5 = sushi.booking.set([rice, fish, chicken_eggs, rice, cheese, fries, salad, cottage_cheese, rice, cheese, fries, salad, cottage_cheese], through_defaults={'client': client1, 'worker': worker1})
# order6 = burger.booking.set([chicken, salad, fries], through_defaults={'client': client1, 'worker': worker1})
# order7 = sushi.booking.set([rice, cheese, salad, fries, cottage_cheese], through_defaults={'client': client1, 'worker': worker1})
# order8 = boul.booking.set([chicken_eggs, salad, rice], through_defaults={'client': client1, 'worker': worker1})
# order9 = pasta.booking.set([chicken, chicken_eggs], through_defaults={'client': client1, 'worker': worker1})
# order10 = shawarma.booking.set([meat, salad, cheese], through_defaults={'client': client1, 'worker': worker1})
#
# for fp in OrderProxy.objects.all():
#     fp.save()


# snack = Order.objects.filter(food_status='snack')
# snack
# lunch = Order.objects.filter(food_status='lunch')
# lunch
# obzhiralova = Order.objects.filter(food_status='obzhiralova')
# obzhiralova
# vegetarian = Order.objects.filter(vegetarian=True)
# vegetarian
# gt1000 = Order.objects.filter(final_price<1000)
# gt1000
# lt = Order.objects.filter(final_price>1000)
# lt

























# order = Order.objects.filter(eat=shawarma,ingredient=meat)
# order

# Food.objects.filter(booking__name__startswith='chee')
# Ingredient.objects.filter(meal__name='Shawarma')

# shawarma.booking.all()
# burger.booking.all()

# res = (shawarma.start_price+cheese.extra_price+salad.extra_price+fries.extra_price)
# res
#
# res1 = (burger.start_price+salad.extra_price+chicken.extra_price)
# res1
#
# amount = (shawarma.start_price+burger.start_price+cheese.extra_price+salad.extra_price+fries.extra_price+chicken.extra_price+salad.extra_price)
# amount









