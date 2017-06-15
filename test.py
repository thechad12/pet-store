import unittest
from models import Pet, Item
import main
from main import session

class TestCases(unittest.TestCase):

	def test_pets(self):
		session.query(Pet).delete()
		pet1 = Pet(pet_type="Dog", pet_sub_type="Black Lab", color="Black", lifespan=13, age=3,
			price=600)
		pet2 = Pet(pet_type="Dog", pet_sub_type="Retriever", color="Yellow",
			lifespan=12, age=7, price=1000)
		pet3 = Pet(pet_type="Dog", pet_sub_type="Welsh Spaniel", color="White",
			lifespan=10, age=2, price=500)
		pet4 = Pet(pet_type="Dog", pet_sub_type="Hound Dog", color="Brown",
			lifespan=10, age=6, price=600)
		pet5 = Pet(pet_type="Dog", pet_sub_type="Bull Dog", color="Yellow",
			lifespan=14, age=5, price=1200)
		pet6 = Pet(pet_type="Cat", pet_sub_type="Black Cat", color="Black",
			lifespan=15, age=1, price=300)
		pet7 = Pet(pet_type="Cat", pet_sub_type="Calico Cat", color="Brown",
			lifespan=14, age=8, price=450)
		pet8 = Pet(pet_type="Cat", pet_sub_type="Brown Cat", color="Brown",
			lifespan=16, age=2, price=400)
		pet9 = Pet(pet_type="Cat", pet_sub_type="Yellow Cat", color="Yellow",
			lifespan=13, age=7, price=500)
		pet10 = Pet(pet_type="Cat", pet_sub_type="White Cat", color="White",
			lifespan=14, age=1, price=550)
		pet11 = Pet(pet_type="Reptile", pet_sub_type="Python Snake", color="Green",
			lifespan=6, age=4, price=75)
		pet12 = Pet(pet_type="Reptile", pet_sub_type="Box Turtle", color="Green",
			lifespan=5, age=3, price=50)
		pet13 = Pet(pet_type="Reptile", pet_sub_type="Dart Frog", color="Yellow",
			lifespan=6, age=1, price=50)
		pet14 = Pet(pet_type="Reptile", pet_sub_type="Green Gecko", color="Green",
			lifespan=6, age=4, price=50)
		pet15 = Pet(pet_type="Reptile", pet_sub_type="Komodo Dragon", color="Brown",
			lifespan=15, age=1, price=1000)
		session.add(pet1)
		session.add(pet2)
		session.add(pet3)
		session.add(pet4)
		session.add(pet5)
		session.add(pet6)
		session.add(pet7)
		session.add(pet8)
		session.add(pet9)
		session.add(pet10)
		session.add(pet11)
		session.add(pet12)
		session.add(pet13)
		session.add(pet14)
		session.add(pet15)
		session.commit()

	def test_items(self):
		session.query(Item).delete()
		item1 = Item(item_type="Dog Crate", price=100)
		item2 = Item(item_type="Aquarium", price=250)
		item3 = Item(item_type="Hamster Wheel", price=10)
		item4 = Item(item_type="Dog Bone", price=15)
		item5 = Item(item_type="Cat Scratcher", price=30)
		session.add(item1)
		session.add(item2)
		session.add(item3)
		session.add(item4)
		session.add(item5)
		session.commit()

if __name__ == '__main__':
	unittest.main()