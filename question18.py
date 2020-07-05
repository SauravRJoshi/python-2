import json

input_dict = {'Name': 'Saurav Raj Joshi', 'age': 24}
print('Converting dictionary to JSON ')



def Py_to_Json(input_dict):
    json_format = json.dumps(input_dict)
    return json_format

print(Py_to_Json(input_dict))

print('Converting JSON to Python format dictionary ')

def Json_to_py(json_format):
    python_format = json.loads(json_format)
    return python_format

print(Json_to_py(Py_to_Json(input_dict)))