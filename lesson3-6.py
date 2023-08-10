def get_age():
    age = int(input("enter your age :"))
    if age < 0:
        raise ValueError("oh no, age can not be negative")

def d():
    c()
def c():
    b()
def b():
    a()
def a():
    get_age()


try:
    d()
except ValueError as e:
    print(e.args[0])