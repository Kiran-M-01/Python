try:
    a = int(input("enter an number : "))
    b = int(input("enter an number : "))
    print(a / c)
# except ValueError as e:
#     # print("enter only integer")
#     print(e)
# except ZeroDivisionError as e :
#     # print("can not be dedvided by Zero")
#     print(e)
# except NameError as e:
#     # print("variable not declared")
#     print(e)


except Exception as e:         # TO HANDLE ALL ERRORS
    print(e)
else:
    print("no errors found")
finally:
    print("exception completed")