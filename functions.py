import main
from models import Base, Pet, Item
import test
from main import session
import resources

print("\nPets\n------------------------------------\n")

main.show_pets()

print("\nItems\n-----------------------------------\n")

main.show_items()

print("\nFiltering by Pet type\n----------------------------------\n")

main.filter_by_pet_type(pet_type=resources.petType)

print("\nFiltering by Pet sub tpe\n--------------------------------\n")

main.filter_by_pet_subtype(subtype=resources.petSubType)

print("\nFiltering by color\n----------------------------------\n")

main.filter_by_color(color=resources.color)

print("\nFiltering by life span\n-------------------------------\n")

main.filter_by_lifespan(lifespan=resources.lifespan)

print("\nFiltering pets by age\n----------------------------\n")

main.filter_by_age(age=resources.age)

print("\nFiltering pets by price\n--------------------------\n")

main.filter_by_price(price=resources.price)

print("\nFiltering items by type\n-----------------------------\n")

main.filter_items_by_type(item_type=resources.itemType)

print("\nFiltering items by price\n--------------------------------\n")

main.filter_items_by_price(price=resources.itemPrice)
