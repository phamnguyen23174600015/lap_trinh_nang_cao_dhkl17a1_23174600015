import json

obj = '{"name": "Quan", "age": 19, "city": "Ha Noi"}'
dict = json.loads(obj)
sorted_obj = dict(sorted(dict.items()))
json_data = json.dumps(sorted_obj, indent=4)
print(json_data)