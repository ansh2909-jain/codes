import json
import rapidjson

# Convert Python dictionary to JSON string
data = {"Name": "Anmol", "Age": 23}
json_str = json.dumps(data)
print(json_str)  

# Convert JSON string to Python dictionary
parsed_data = json.loads(json_str)
print(parsed_data)

# Rapidjson

# Convert Python dictionary to JSON string using rapidjson
data = {"Name": "Anu", "Age": 24}
json_str = rapidjson.dumps(data)
print(json_str)  

# Convert JSON string to Python dictionary using rapidjson
parsed_data = rapidjson.loads(json_str)
print(parsed_data)  
