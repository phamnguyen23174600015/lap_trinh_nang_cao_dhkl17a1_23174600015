import json 

data = { 
"ten": "Nguyen van a", 
"msv": 123456, 
"truong": "uneti" 
} 
 
json_string = json.dumps(data, ensure_ascii=False) 
print(json_string) 
print(type(json_string))