print("Default Parameters")

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Dipp"))
print(greet("Dipp", "Hi"))

print("_" * 30)

print("Variable-length Arguments")

def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(1, 2, 3, 4, 5))

print("_" *  30)
print("Keyword arguements")


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Dipp", age=24, role="Developer")

print("_" *  30)
print("Inner (Nested) Functions")

def outer(x):
    def inner(y):
        return x + y
    return inner(5)

print(outer(10))

print("_" * 30)
print("_" *  30)

print("Decorators")

print("_" *  30)


print("basic:")

def decorator_thing(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@decorator_thing
def greet():
    print("Hey Dipp")

greet()


print("_" * 30)
print("Explained")

#Step 1: Define a decorator
def uppercase_decorator(func):
    print("Before")
    def wrapper():
        original_result = func()
        return original_result.upper()
    print("After")
    return wrapper

# Step 2: Define a simple function
def say_hello():
    return "Hey"

# Step 3: Apply decorator clearly
decorated_function = uppercase_decorator(say_hello)

#Step 4: Call the wrapped function
print(decorated_function())


print("_" * 30)
print("Logger")
print("_" * 30)
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def multiply(x, y):
    return x * y

multiply(2, 4)

print("_" * 30)
print("Arg in decorator")
print("___")


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for time in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello {name}")


greet("Dipp")