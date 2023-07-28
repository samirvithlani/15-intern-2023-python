no = int(input("Enter a number: ")) 
# 123 = 3
# 123 // 10 = 12 no =12 coumt = 1
# 12 // 10 = 1 no = 1  count = 2
# 1 // 10 = 0 no = 0   count = 3

#2345
#2345 // 10 = 234 no = 234 count = 1
#234 // 10 = 23 no = 23 count = 2
#23 // 10 = 2 no = 2 count = 3
#2 // 10 = 0 no = 0 count = 4
count=0
while no>0:
    count+=1
    no = no // 10


print("count of digit = ",count)    

