try:
    a = int(input("enter an number : "))
    b = int(input("enter an number : "))
    print(a / b)
except ValueError :
    print("enter only integer")
except ZeroDivisionError :
    print("can not be dedvided by Zero")
else:
    print("no errors found")
finally:
    print("exception completed")