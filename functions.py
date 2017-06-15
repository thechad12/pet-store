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