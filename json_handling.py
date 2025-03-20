import json
from datetime import datetime

# JSON string
json_data = '{"name": "Anmol", "age": 23, "city": "Noida"}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_data)

print(python_dict)
print(type(python_dict))  # Output will be a Python dict

# Assuming you have a JSON file named 'data.json'
try:
    with open('data.json', 'r') as file:
        data = json.load(file)
    print(data)
except FileNotFoundError:
    print("The file 'data.json' was not found.")
except json.JSONDecodeError:
    print("The file 'data.json' contains invalid JSON.")
except Exception as e:
    print(f"An error occurred: {e}")
python_dict = {"name": "Ansh", "age": 23, "city": "Delhi"}

# Convert Python dictionary to JSON string
json_string = json.dumps(python_dict)
print(json_string)

# Python dictionary
python_dict = {"name": "Anu", "age": 23, "city": "Gurgaon"}

# Writing Python dictionary to 'output.json' file
with open('output.json', 'w') as file:
    json.dump(python_dict, file)
print("Data written to file.")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Custom serialization function
def person_serializer(obj):
    if isinstance(obj, Person):
        return {'name': obj.name, 'age': obj.age}
    raise TypeError("Type not serializable")
person = Person("Ankish", 28)

# Serialize the person object
json_string = json.dumps(person, default=person_serializer)
print(json_string)

def datetime_decoder(obj):
    if 'date' in obj:
        obj['date'] = datetime.strptime(obj['date'], "%Y-%m-%d")
    return obj
json_data = '{"name": "Event", "date": "2025-03-20"}'

# Deserialize and decode datetime
data = json.loads(json_data, object_hook=datetime_decoder)
print(data)
print(type(data['date']))