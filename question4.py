collegues = []
id_before = id(collegues)
collegues.append('Saurav')
collegues.append('Sanjay')
collegues.append('Shreeja')
id_after_append = id(collegues)

if id_before == id_after_append:
    print('Id is',id_before)
else:
    print('After changing, Id is',id_after_append)

collegues.sort()
print()
print(f'First item -> {collegues[0]}')
print(f'second item -> {collegues[1]}')