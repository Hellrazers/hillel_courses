import json


with open('first_json.json', 'r') as f:
    first_json = json.load(f)
    print(first_json)



first_json['kids_name'] = ['Ivan', 'Oleksii', "Anna"]

first_json_2 = json.dumps(first_json, indent=4)
print(first_json_2)
print(json.loads(first_json_2))



print(first_json)

with open('second_json.json', 'w') as f:
    json.dump(first_json, f, indent=4)


