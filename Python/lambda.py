l = [1,2,3,1,4,5,3,4,7,8,9,9]
res = []
add = lambda x: res.append(x) if x not in res else None
for i in l:
    add(i)

print(res)

