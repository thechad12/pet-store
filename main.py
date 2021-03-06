from models import Pet, Item, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import sys
from sqlalchemy import exists

engine = create_engine('sqlite:///petstore.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def pet_columns():
	print("ID\tType\tSub Type\tColor\tSpan\tAge\tPrice\tDiscount?")

def pet_vals(pet):
	print(str(pet.id) + "\t" + pet.pet_type + "\t" + pet.pet_sub_type + "\t"
			+ pet.color + "\t" + str(pet.lifespan) + "\t" + str(pet.age) + "\t" +
			str(pet.price) + "\t" + str(pet.check_discount()))

def item_columns():
	print("ID\tType\tPrice")

def item_vals(item):
	print(str(item.id) + "\t" + item.item_type + "\t" + str(item.price))

def check_vals(user_input, input_type):
	if type(user_input) != input_type:
		raise ValueError("We're sorry, we could not read that. Please enter %s" % input_type)

def empty_query(thing):
	if thing.count() == 0:
		print("We're sorry, we do not have any of those. Please try another search.")

def show_pets():
	pets = session.query(Pet).all()
	pet_columns()
	for pet in pets:
		pet_vals(pet)
	return

def show_items():
	items = session.query(Item).all()
	item_columns()
	for item in items:
		item_vals(item)
	return

def filter_by_pet_type(pet_type):
	check_vals(pet_type, str)
	pets = session.query(Pet).filter_by(pet_type=pet_type)
	empty_query(pets)
	pet_columns()
	for pet in pets:
		pet_vals(pet)
	return

def filter_by_pet_subtype(subtype):
	check_vals(subtype, str)
	breeds = session.query(Pet).filter_by(pet_sub_type=subtype)
	empty_query(breeds)
	pet_columns()
	for pet in breeds:
		pet_vals(pet)
	return

def filter_by_color(color):
	check_vals(color, str)
	colors = session.query(Pet).filter_by(color=color)
	empty_query(colors)
	pet_columns()
	for pet in colors:
		pet_vals(pet)
	return

def filter_by_lifespan(lifespan):
	check_vals(lifespan, int)
	lifespans = session.query(Pet).filter_by(lifespan=lifespan)
	empty_query(lifespans)
	pet_columns()
	for pet in lifespans:
		pet_vals(pet)
	return

def filter_by_age(age):
	check_vals(age, int)
	ages = session.query(Pet).filter_by(age=age)
	empty_query(ages)
	pet_columns()
	for pet in ages:
		pet_vals(pet)
	return

def filter_by_price(price):
	check_vals(price, int)
	prices = session.query(Pet).filter_by(price=price)
	empty_query(prices)
	pet_columns()
	for pet in prices:
		pet_vals(pet)
	return

def filter_items_by_type(item_type):
	check_vals(item_type, str)
	items = session.query(Item).filter_by(item_type=item_type)
	empty_query(items)
	item_columns()
	for item in items:
		item_vals(item)
	return

def filter_items_by_price(price):
	check_vals(price, int)
	items = session.query(Item).filter_by(price=price)
	empty_query(items)
	item_columns()
	for item in items:
		item_vals(item)
	return




