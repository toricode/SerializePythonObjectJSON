import json

# Serialize Python dict Object to JSON String
user = {"firstName": "Kathy", "lastName": "Wells"}

json_user = json.dumps(user)

print(json_user)

# Serialize Python list Object to JSON String
languages = ['Python', 'Java', 'C#', 'C++']

json_languages = json.dumps(languages)

print(json_languages)

# Serialize Python tuple Object to JSON String
skills = ('Web Development', 'Mobile Development', 'Agile')

json_skills = json.dumps(skills)

print(json_skills)

# Serialize Python string Object to JSON String
message = "Hello from toricode.com"

json_message = json.dumps(message)

print(json_message)

# Serialize Python int Object to JSON String
points = 7

json_points = json.dumps(points)

print(json_points)

# Serialize Python float Object to JSON String
price = 45.78

json_price = json.dumps(price)

print(json_price)

# Serialize Python True Object to JSON String
json_true = json.dumps(True)

print(json_true)

# Serialize Python False Object to JSON String
json_false = json.dumps(False)

print(json_false)

# Serialize Python None Object to JSON String
json_none = json.dumps(None)

print(json_none)