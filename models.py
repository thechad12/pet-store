from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import sys

Base = declarative_base()

class Pet(Base):
	__tablename__ = 'pet'

	id = Column(Integer, primary_key=True)
	pet_type = Column(String, nullable=False)
	pet_sub_type = Column(String, nullable=False)
	color = Column(String, nullable=False)
	lifespan = Column(Integer, nullable=False)
	age = Column(Integer, nullable=False)
	price = Column(Integer, nullable=False)

	def discount(self):
		if self.age >= (self.lifespan/2):
			self.price = self.price*0.75
			return self.price

	def check_discount(self):
		if self.discount():
			return True
		else:
			return False


class Item(Base):
	__tablename__ = 'item'

	id = Column(Integer, primary_key=True)
	item_type = Column(String, nullable=False)
	price = Column(Integer, nullable=False)

engine = create_engine('sqlite:///petstore.db')
Base.metadata.create_all(engine)