# Lambda Decorator

dec = lambda f: lambda *args, **kwargs: (print('Dec'), f(*args, **kwargs))

@dec
def hello():
	print('Hello')

hello()

# Alperen Cubuk