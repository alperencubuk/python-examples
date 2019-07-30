# Decorator With Parameter

def control(*args_d, **kwargs_d):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if kwargs_d.get('init', None):
                print('1 - OK INIT', func.__name__)
            result = func(*args, **kwargs)
            if kwargs_d.get('end', None):
                print('1 - OK END', func.__name__)
            return result
        return wrapper
    return decorator


@control(init=True, end=True)
def function1(name):
    print(name)


function1('AlperenCubuk')

# --------------------------------------
print('\n')
# --------------------------------------

# Decorator Without Parameter

def decorator(func):
    def wrapper(*args, **kwargs):
        print('2 - OK INIT', func.__name__)
        result = func(*args, **kwargs)
        print('2 - OK END', func.__name__)
        return result
    return wrapper


@decorator
def function2(name):
    print(name)


function2('AlperenCubuk')
