import random
def hello(user):
    x=random.randint(1,5)
    if x==1:
        print("hello", user,". Its a wonderfull day")
    elif x==2:
        print("Hey! whats up",user,".")
    elif x==3:
        print("Hey",user,"!")
    elif x==4:
        print("Hello",user,"its a beautiful world.")
    else:
        print("Hi!")
