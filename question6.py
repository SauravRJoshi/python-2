my_list = ['Saurav','Sanjay','Sushant','Chetan','Abhishek','Siddhartha','John']
search_name = 'not found'
for name in my_list:
    if name == 'John':
        search_name = name
        break
print(search_name)