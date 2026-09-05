# 1 & 2 -  reverse a string , check palondrome
# def reverse(str):
#     rev = ''
#     for s in str:
#         rev = s + rev

#     if rev == str:
#         return True
#     else:
#         return False

# print(reverse('ata'))

# 3 & 4 - reverse an integer , check palindrome for a number
# def reverse(n):
#     num = n
#     rev = ''
#     while n > 0:
#         l = n % 10
#         rev =  rev + str(l) 
#         n = n // 10

#     # return rev
#     if int(rev) == num:
#         return f'palindrome'
#     else:
#         return f'not palindrome'

# print(reverse(12345564321))


# 5), 5) Prime number  , range of prime numbers
# def isPrime(n):
#     if n < 2:
#         return False
    
#     for i in range(2,n):
#         if n % i == 0:
#             # return f'not prime'
#             return False

#     # return f'Prime number'
#     return True

# # print(isPrime(3))

# def PrimeRange(m,n):
#     for num in range(m,n+1):
#         if isPrime(num):
#             print(num)

# PrimeRange(10, 20)


# 7)Find Factorial of a Number
# def fact(n):
#     res = 1
#     for i in range(1,n+1):
#         res = res*i
#     return res

# print(fact(7))

# 8. Generate Fibonacci Series
def fib(n):
    a = 0
    b = 1
    for i in range(n+1):
        print(a)
        a,b = b,a+b

print(fib(7))


    

