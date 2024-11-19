import json 

data = { 
"ten": "Nguyen van a", 
"msv": 123456, 
"truong": "uneti" 
} 

json_string = json.dumps(data, indent = 4, sort_keys = True)
print(json_string) 