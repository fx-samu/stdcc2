import stdcc2

def foo():
    print("A dummy function")

stdcc2.f_name("foo funcion", foo)

print(foo.__code__.co_name)