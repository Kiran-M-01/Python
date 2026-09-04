# 39
# n = 1
# while n <= 5:
#     print(n,"Python")
#     n += 1

# 40
# n = int(input("enter n value : "))

# i = 1
# while i <=n:
#     print(i)
#     i = i + 1


#41
# n = int(input("enter n value : "))
# i = 1
# while i <= 10:
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# 42
# n = int(input("enter n value : "))
# i = 1
# a = 0
# while i <= n:
#     a = a + i
#     i += 1
# print(a)

# 43
# n = int(input("enter n value : "))
# i = 1
# a = 1
# b = 1
# while i <= n:
#     a = a * i
#     b = b * i
#     i += 1
# print("product is ",a)
# print("factorial is ",b)


# s = input("enter  a string : ")
# i = 0

# while i < len(s):
#     if i % 2 == 0:
#         print(s[i])
#     i += 1

# BINARY SEARCH
s = [1,3,3,4,5,6,7,8]
target = int(input("enter  target : ")) #5
l,r = 0,len(s)-1
while l <= r:
    mid = (l+r) // 2
    if s[mid] < target :
        l = mid + 1
    elif s[mid] > target:
        r = mid - 1
    else:
        print("found at",mid)
        break
else:
    print("not found")

