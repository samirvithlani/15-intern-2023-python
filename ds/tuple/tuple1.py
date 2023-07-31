#tuple

#data = () #empty tuple
data = ("raj","ajay","jay","parth","priya","amit")
print(data)
print(type(data))

#print(data[1])
#data[0] = "RAJ"
x = data.count("raj")
print(x)
ind = data.index("raj")
print(ind)

for i in data:
    print(i)