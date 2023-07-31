#list -->
#data = [] #empty list
data = ["raj","ajay","jay","parth","priya","amit"]
print(data)
print(type(data))
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])

size = len(data)
data.append("sachin")
data.extend(["saurav","rahul","virendra","sachin"])
data.insert(1,"Mahi")

data[1] ="Dhoni"

data.remove("saurav")
removedelm = data.pop(2)
print("removing..",removedelm)

ind = data.index("sachin")
print("index of sachin is ",ind)


#data.reverse()
data.sort(reverse=True)
cnt = data.count("sachin")
print("count of sachin is ",cnt)




# for i in range(0,len(data)):
#     print(data[i])

for i in data:
    print(i)