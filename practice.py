#   DECIMAL TO BIANRY AND BINARY TO DECIMAL ----------
# def dec_to_bin():
#     n = int(input("Enter :"))
#     binary = ''
#     while n != 0:
#         rem = n%2
#         binary = str(rem) + binary
#         n //= 2
#     print(binary)
# dec_to_bin()

# def bin_to_dec():
#     n = int(input("Enter :"))
#     decimal = 0
#     p = 0
#     while n != 0:
#         l = n%10
#         decimal = decimal + l * 2 ** p
#         n //= 10
#         p += 1
#     print(decimal)
# bin_to_dec()

# FIBONACCI SERIES ---------
# def fib():
#     n = int(input("neter a number : "))
#     fibb = []
#     a,b = 0,1
#     for i in range(n):
#         fibb.append(a)
#         a,b = b,a+b
#     return fibb
# print(fib())

# STRONG NUMBER AND FACTORIAL ---------
# factorial

# def fact(n):
#     res = 1
#     for i in range(1,n+1):
#         res *= i
#     return res
# # print(fact(int(input("enter : "))))

# def strong():
#     n = int(input("enter : "))
#     temp = n
#     res = 0
#     while n > 0:
#         l = n % 10
#         res += fact(l)
#         n //= 10

#     if temp == res:
#         print("strong number")
#     else:
#         print("not strong number")

# strong()

# ARMSTRONG NUMBER
def pow(n):
    count = 0
    while n > 0:
        count += 1
        n//=10
    return count
# print(pow(123456789))

def arm_strong():
    n = int(input("enter : "))
    digits = pow(n)
    temp = n
    res = 0
    while n != 0:
        l = n % 10
        res += l ** digits
        n //= 10

    if temp == res:
        print("arm strong number")
    else:
        print("not arm strong number")

arm_strong()


    

        


