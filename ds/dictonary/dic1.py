
#data = {} #empty dictonary
data = {'name':'sachin','age':22,'course':'python','name':"Samyak"}
print(data)
print(type(data))
data['name'] = 'samyak'

data['year'] = 2020
data.update({'bgroup':'o+','id':101,'course':'python+'})

#x = data.pop('id')
x = data.popitem()

print("removing...",x)

key = data.keys()
print("key ->",key)
value = data.values()
print("value ->",value)

data.clear()
for i,j in data.items():
    print(i," - ",j)
