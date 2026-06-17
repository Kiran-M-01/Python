try:
    a = int(input("enter an number : "))
    b = int(input("enter an number : "))
    print(a / c)
except ValueError :
    print("enter only integer")
except ZeroDivisionError :
    print("can not be dedvided by Zero")
except NameError :
    print("variable not declared")
else:
    print("no errors found")
finally:
    print("exception completed")