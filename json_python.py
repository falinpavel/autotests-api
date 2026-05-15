import json

json_data = '{"name": "Petr","age": 19,"gender": "Male"}'
parsed_json = json.loads(json_data)

print(type(parsed_json))
print(parsed_json)
print(parsed_json['name'])
print(parsed_json['age'])

data_dict = {
    "name": "Petr",
    "age": 19,
    "gender": "Male",
    "is_student": True
}

print(type(data_dict))
dict_in_str = json.dumps(data_dict, indent=2)
print(type(dict_in_str))
print(dict_in_str)

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(type(data))
    print(data)

with open("json_example_dump.json", "w", encoding="utf-8") as file:
    json.dump(data_dict, file, indent=4, ensure_ascii=False)