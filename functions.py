import main
from models import Base, Pet, Item
import test
from main import session

print("\nPets\n------------------------------------\n")

main.show_pets()

print("\nItems\n-----------------------------------\n")

main.show_items()

print("\nFiltering by Pet type\n----------------------------------\n")

main.filter_by_pet_type(pet_type="Dog")

print("\nFiltering by Pet sub tpe\n--------------------------------\n")

main.filter_by_pet_subtype(subtype="Black Lab")

print("\nFiltering by color\n----------------------------------\n")

main.filter_by_color(color="Yellow")

print("\nFiltering by life span\n-------------------------------\n")

main.filter_by_lifespan(lifespan=10)

print("\nFiltering pets by age\n----------------------------\n")

main.filter_by_age(2)

print("\nFiltering pets by price\n--------------------------\n")

main.filter_by_price(500)

print("\nFiltering items by type\n-----------------------------\n")

main.filter_items_by_type(item_type="Aquarium")

print("\nFiltering items by price\n--------------------------------\n")

main.filter_items_by_price(price=100)