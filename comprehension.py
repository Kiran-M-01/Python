# LIST COMPREHENSION
#l = [i for i in range(11)]

#l = [i for i in range(11)]

#print(l)
# l=[12,1,-3,4,-5]
# out=[0 if i<0 else i for i in l]
# print(out)

# l = [[1,2],[3,4],[5,6]]
# l = [j for i in l for j in i ]
# print(l)

# SET COMPREHENSION
# s1 = eval(input("enter a set"))
# s2 = eval(input("enter a set"))
# s = {i for i in s1 if i in s2}
# print(s)

# DICTIONSRY COMPREHENSION
# l = [1,2,3,4,5,6,7,8]
# print({i:l[i] for i in range(len(l))})

l1 = [10,20,30,40,50]
l2 = [1,2,3,4,5]
print({l1[i]: l2[i] for i in range(len(l1))})


