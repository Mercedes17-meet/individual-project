from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}  #This will enable us to add more columns later
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password_hash = Column(String)
    photo = Column(String)
    email = Column(String)
    date_of_birth= Column(String)
    gender= Column(String)
    my_outfits= relationship("Outfit", back_populates= "creator")
    outfits=relationship("Outfit_association", back_populates= "user")

    def hash_password(self,password):
    	self.password_hash= pwd_context.encrypt(password)
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class Outfit(Base):
    __tablename__ = 'outfit'
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    season = Column(String)
    photo = Column(String)
    gender = Column(String)
    categorty = Column(String)
    description = Column(String)
    creator_id = Column(Integer, ForeignKey('user.id'))
    creator =relationship("User", back_populates="my_outfits")
    owners= relationship("Outfit_association", back_populates="outfit")

class Outfit_association(Base):
	__tablename__='outfit_association'
	__table_args__={'extend_existing': True}
	user_id= Column (Integer, ForeignKey("user.id"), primary_key=True)
	outfit_id=Column(Integer, ForeignKey("outfit.id"), primary_key=True)
	user= relationship("User", back_populates="outfits")
	outfit= relationship("Outfit", back_populates="owners")