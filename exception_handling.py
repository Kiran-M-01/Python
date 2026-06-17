try:
    a = int(input("enter an number : "))
    b = int(input("enter an number : "))
    print(a + b)
except ValueError :
    print("enter only integer")
else:
    print("no errors found")
finally:
    print("exception completed")