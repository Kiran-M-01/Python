# # WITHOUT ARDUMENT WITHOUT RETURN
# # DECIMAL TO BINARY
# def decimalToBinary():
#     n = int(input("Enter :"))
#     binary = ''
#     while n != 0:
#         rem = n%2
#         binary = str(rem) + binary
#         n//=2
#     print(binary)
# decimalToBinary()
# # # 
# # # BINARY TO DECIMAL
# # def binaryToDecimal():
# #     n = int(input("Enter :"))
# #     dec = 0
# #     p = 0
# #     while n != 0:
# #         l = n%10
# #         dec = dec + l * 2 ** p
# #         n//=10
# #         p += 1
# #     print(dec)
# # binaryToDecimal()

# # WITH ARGUMENT WITHOUT RETURN
# # EXTRACT NON DEFAULT VALUES FROM LIST
# # def extNonDef(l):
# #     nondef = []  
# #     for i in l:
# #         if bool(i) == True:
# #             nondef.append(i)
# #     print(nondef)
# # extNonDef([1,0,'',34,[],'abc',()])

# # WITHOUT ARG AND WITH RETURN
# # def add():
# #     a = int(input("enter:  "))
# #     b = int(input("enter:  "))
# #     return a + b
# # print(add())

def fib():
    n = int(input( ))
    a,b = 0,1
    fib = []
    for i in range(n):
        fib.append(a)
        a,b = b,a+b
    return fib
print(fib())

# # FUNCTION WITH ARGUMENT AND WITH RETURN
# # def add(a,b):
# #     return a + b
# # print(add(1,3))

# # PATTERN
# # def kabab(s):
# #     out = {}

# #     for w in s.split(" "):
# #         vowel = 0
# #         cons = ''
# #         for c in range(len(w)):
# #             if w[c] in 'aeiouAEIOU':
# #                 vowel += 1
# #             else:
# #                 cons += w[c]

# #         b = [w[::-1],vowel,cons]
# #         out[w] = b
# #     return out    
# # print(kabab('kabab is love'))

# # FACTORIAL
# def fact(n):
#     res = 1
#     for i in range(1,n+1):
#         res *= i
#     return res

# # print(fact(4))

# # # STRONG NUMBER

# # def is_strong(num):
# #     tempNum = num
# #     sum = 0
# #     while num != 0:
# #         l = num % 10
# #         sum += fact(l)
# #         num //= 10
# #     if tempNum == sum:
# #         print("strong number")
# #     else:
# #         print("Not a strong number")
# # is_strong(145)

# # # STRONG NUMBER BETWEEN 1 TO 50000
# # def fact(n):
# #     res = 1
# #     for i in range(1,n+1):
# #         res *= i
# #     return res

# # # print(fact(4))

# # # STRONG NUMBER

# # def is_strong(num):
# #     tempNum = num
# #     summ = 0
# #     while num != 0:
# #         l = num % 10
# #         summ += fact(l)
# #         num //= 10
# #     if tempNum == summ:
# #         return sum
# #     #     print("strong number",num)
# #     # else:
# #     #     print("Not a strong number",num)
# # # is_strong(145)
# # def strongBtw1To50k(m,n):
# #     for i in range(m,n):
# #         if is_strong(i):
# #             print(i)

# # strongBtw1To50k(1,100)

# # # AMSTRONG NUMBER
# def amstrong(num):
#     a = str(num)
#     length = len(a)
#     sum1 = 0
#     temp = num
#     while num != 0:
#         d = num % 10
#         sum1 += d ** length
#         num //= 10
#     if temp == sum1:
#         return True
#     #     print("amstrong number")
#     # else:
#     #     print('not amstrong number')
# # amstrong(153)

# def ams_50(m,n):
#     for i in range(m,n):
#         if amstrong(i):
#             print(i)
# ams_50(1,50000)



