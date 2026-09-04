input = [10,10,0,4,5,-5,-20]
output = [[10,10,-20],[5,-5,0]]

i = [10,10,0,4,5,-5,-20]
out = []
i.sort()           #[-20,-5,0,4,5,10,10]

for a,f in enumerate(i):
    if a > 0 and f == i[a - 1]:
        continue
    l, r = a + 1, len(i) - 1
    while l < r:
        if f + i[l] + i[r] < 0:
            l += 1
        elif f + i[l] + i[r] > 0:
            r -= 1
        else:
            out.append([f,i[l],i[r]])
            l += 1
            while l < r and i[l] == i[l]-1:
                l += 1
print(out)        

    
# print(out)

# l = [10,10,0,4,5,-5,-20]
# largest = second = float('-inf')
# for num in l:
#     if num > largest:
#         largest = num
#         second = largest
#     elif num > second and num != largest:
#         second = num


# print(second)