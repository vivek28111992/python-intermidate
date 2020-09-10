import json
from json import JSONEncoder

with open('example.json', 'r') as f:
  person = f.read().replace('\n', '')
print(person)

personJSON = json.dumps(person, indent=2)
print(personJSON)

# with open('person.json', 'w') as file:
#   json.dump(person, file, indent=4)

from json import JSONEncoder

class User:

  def __init__(self, name, age):
    self.name = name
    self.age = age

class UserEncoder(JSONEncoder):

  def default(self, o):
    if isinstance(o, User):
      return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    return JSONEncoder.default(self, o)

user = User('Max', 27)

def encode_user(o):
  if isinstance(o, User):
    return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
  else:
    raise TypeError('Object of type User is not JSON serialiable')

def decode_user(dct):
  if User.__name__ in dct:
    return User(name=dct['name'], age=dct['age'])
  return dct


# userJSON = json.dumps(user, default=encode_user)
userJSON = UserEncoder().encode(user)
userDecode = json.loads(userJSON, object_hook=decode_user)
print(userDecode.name)
print(userJSON)
