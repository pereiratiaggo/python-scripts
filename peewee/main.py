import peewee
from pprint import pprint

db = peewee.SqliteDatabase('tmp.sqlite')

class Model(peewee.Model):
    class Meta:
        database = db
    
class User(Model):
    name        = peewee.CharField()
    email       = peewee.CharField()
    password    = peewee.CharField()

db.create_tables([User])

User.create(name="John", email="john@example.com", password="password")
User.create(name="Mike", email="mike@example.com", password="password")

john = User.get(name="John")
john.name = "John Smith"
john.update()

mike = User().get(name="Mike")
mike.update(name="Mike Smith")
mike.save()

pprint(vars(john))
pprint(vars(mike))