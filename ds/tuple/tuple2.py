users = ("user1","user2","user3")

userlist = list(users)
userlist.append("user4")
users = tuple(userlist)
print(users)