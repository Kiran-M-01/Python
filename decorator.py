def instagram(func):
    def wrapper(*args, **kwargs):
        print("open instagram")
        print("login")
        func(*args, **kwargs)
        print("exit instagram")
    return wrapper

@instagram
def sangu():
    print("chat with risha")

@instagram
def harsha():
    print("chat with pooja")

@instagram
def darshu():
    print("chat with raghu")

sangu()
