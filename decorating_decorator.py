def decorator_with_args(decorator_to_enhance):
    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args 
def decorated_decorator(func, *args, **kwargs): 
    def wrapper(function_arg1, function_arg2):
        print('Decorated with', args, kwargs)
        return func(function_arg1, function_arg2)
    return wrapper
    

@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print('Hello', function_arg1, function_arg2)


decorated_function('Universe and', 'everything')
