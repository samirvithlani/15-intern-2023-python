users = {1:["ram","lakshman"],2:["sita","gita"]}

print(users)

for i,j in users.items():
    print(i," - ",j)
    for k in j:
        print(k)
    