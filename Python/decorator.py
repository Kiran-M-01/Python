# def instagram(func):
#     def wrapper(*args, **kwargs):
#         print("open instagram")
#         print("login")
#         func(*args, **kwargs)
#         print("logout from instagram")
#     return wrapper

# @instagram
# def sangu():
#     print("chat with risha")

# @instagram
# def harsha():
#     print("chat with pooja")

# @instagram
# def darshan():
#     print("chat with raghu")

# sangu()
# harsha()
# darshan()




# 2
import time 
def delay_time(func):
    def wrapper(*args,**kwargs):
        time.sleep(10)
        r = func(*args,**kwargs)
        print(r)
    return wrapper

@delay_time
def reverse(s):
    rev = ''
    for i in s :
        rev = i + rev
    return rev

reverse("hello")
