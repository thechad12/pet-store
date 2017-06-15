from models import Pet, Item, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import sys

engine = create_engine('sqlite:///petstore.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def check_vals(user_input, input_type):
	if type(user_input) != input_type:
		raise ValueError("We're sorry, we could not read that, please try again")

def show_pets():
	pets = session.query(Pet).all()
	print("ID\tType\tSub Type\tColor\tSpan\tAge\tPrice")
	for pet in pets:
		print(str(pet.id) + "\t" + pet.pet_type + "\t" + pet.pet_sub_type + "\t"
			+ pet.color + "\t" + str(pet.lifespan) + "\t" + str(pet.age) + "\t" +
			str(pet.price))
	return

def show_items():
	items = session.query(Item).all()
	print("ID\tType\tPrice")
	for item in items:
		print(str(item.id) + "\t" + item.item_type + "\t" + str(item.price))
	return

def filter_by_pet_type(pet_type):
	check_vals(pet_type, str)
	pets = session.query(Pet).filter_by(pet_type=pet_type)
	print("ID\tType\tSub Type\tColor\tSpan\tAge\tPrice")
	for pet in pets:
		print(str(pet.id) + "\t" + pet.pet_type + "\t" + pet.pet_sub_type + "\t"
			+ pet.color + "\t" + str(pet.lifespan) + "\t" + str(pet.age) + "\t" +
			str(pet.price))
	return

def filter_by_pet_subtype(subtype):
	check_vals(subtype, str)
	breeds = session.query(Pet).filter_by(pet_sub_type=subtype)
	if len(breeds) == 0:
		print("We're sorry, we do not have any breeds of that type")
	else:
		print(breeds)
	return

def filter_by_color(color):
	check_vals(color, str)
	colors = session.query(Pet).filter_by(color=color)
	if len(colors) == 0:
		print("We're sorry, we are out of those colors")
	else:
		print(colors)
	return

def filter_by_lifespan(lifespan):
	check_vals(lifespan, int)
	lifespans = session.query(Pet).filter_by(lifespan=filter_type)
	if len(lifespans) == 0:
		print("We're sorry, we are out of pets with that lifespan")
	else:
		print(lifespans)
	return

def filter_by_age(age):
	check_vals(age, int)
	ages = session.query(Pet).filter_by(age=age)
	if len(ages) == 0:
		print("We're sorry, we are out of pets with that age")
	else:
		print(ages)
	return

def filter_by_price(price):
	check_vals(price, int)
	prices = session.query(Pet).filter_by(price=price)
	if len(prices) == 0:
		print("You may have to shell out some more dough")
	else:
		print(prices)
	return

def filter_items_by_type(item_type):
	check_vals(item_type, str)
	items = session.query(Item).filter_by(item_type=item_type)
	if len(items) == 0:
		print ("No items of that type")
	else:
		print(items)
	return

def filter_items_by_price(price):
	check_vals(price, str)
	items = session.query(Item).filter_by(price=price)
	if len(items) == 0:
		print("Seriously, get a bigger wallet")
	else:
		print(items)
	return


