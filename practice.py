#   DECIMAL TO BIANRY AND BINARY TO DECIMAL
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

# FIBONACCI SERIES
def fib():
    n = int(input("neter a number : "))
    fibb = []
    a,b = 0,1
    for i in range(n):
        fibb.append(a)
        a,b = b,a+b
    return fibb
print(fib())

