my_dict = {'1': 'Anmol', '2': 'Jain', '3': 'anm'}                  #clear() Method
my_dict.clear()
print(my_dict)

d = {'Name': 'Anmol', 'Age': '23', 'Country': 'India'}          #get() Method
print(d.get('Name'))
print(d.get('Gender'))

d = {'Name': 'Anmol', 'Age': '23', 'Country': 'India'}          #items() Method
print(list(d.items())[2][0])
print(list(d.items())[0][1])

d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}            #keys() Method
print(list(d.keys()))

d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}           #update() Method
d2 = {'Name': 'Anmol', 'Age': '23'}

d1.update(d2)
print(d1)

d = {'Name': 'Anmol', 'Age': '23', 'Country': 'India'}            #values() Method
print(list(d.values()))

d = {'Name': 'Anmol', 'Age': '23', 'Country': 'India'}          #pop() Method
d.pop('Age')
print(d)

d = {'Name': 'Anmol', 'Age': '23', 'Country': 'India'}            #popitem() Method
val = d.popitem()
print(val)

val = d.popitem()
print(val)

val = d.popitem()
print(val)