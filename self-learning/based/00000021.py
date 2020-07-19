# decorator

def greetings(name):
    print('Hello,', name)


def morning(func):
    def wrapper(arg):
        func(arg)
        print('Good morning,', arg)

    return wrapper


@morning
def greetings(name):
    print('Hello,', name)



greetings('Susie')