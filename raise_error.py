# RAISING BUILTIN ERROR
# s = input("enter a string :")
# if s == s[::-1]:
#     print('palindrome')
# else:
#     raise TypeError("not palindrome")

# RAISING USER DEFINED ERROR

# class NotPalindromeError(Exception):
#     pass

# s = input("enter a string :")
# if s == s[::-1]:
#     print('palindrome')
# else:
#     raise NotPalindromeError("not palindrome")

#   PROBLEMS
# 1
# class NegativeNumberError(Exception):
#     pass
# n = int(input("enter a number :"))
# if n > 0:
#     print(n)
# else:
#     raise NegativeNumberError("you entered negative number")

# 2
class NotEligibleError(Exception):
    pass
n = int(input("enter a number :"))
if n >= 18:
    print("Eligible")
else:
    raise NotEligibleError("you are not eligible")
