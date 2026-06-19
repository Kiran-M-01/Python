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
# class NotEligibleError(Exception):
#     pass

# n = int(input("enter a number :"))
# if n >= 18:
#     print("Eligible")
# else:
#     raise NotEligibleError("you are not eligible")

# 3
# class NotSpecialCharecter(Exception):
#     pass

# ch = input("enter a char :")
# if (32 <= ord(ch) <= 47) or \
#    (58 <= ord(ch) <= 64) or \
#    (91 <= ord(ch) <= 96) or \
#    (123 <= ord(ch) <= 126):
#     print("Special Character")
# else:
#     raise NotSpecialCharecter("not a special charecter")

# 4
class InsufficientBalanceError(Exception):
    pass


class account():
    def __init__(self,bal):
        self.bal = bal
    def withdraw(self):
        amt = int(input("enter amount to withdraw : "))
        if self.bal > amt :
            self.bal -= amt
            print("withdraw success full",self.bal)
        else:
            raise InsufficientBalanceError("enter less amount")

ob = account(1000)
ob.withdraw()