# Day 1 

## Functions
Basic function structure:

```python
def function_name(parameter1):
    # Body
    # Because we need something to return
    result = parameter1 + 1
    return result
```

Parameters Vs Arguements:
- Parameters are names defined in the function definition
- Arguments are actual values passed when calling the function

```python
def greet(name):
    return f"Hello, {name}!"

greeting = greet("Dipp")
```

Yeah... That's basically the... well... basics of functions. Although, I'm kinda stuck between actually going a little more further, or being beginner like for people
to understand in case anyone wants to follow along and get better as well with. But then I remembered that I'm not making this for anyone. It's my own personal thing. So if someone stumbles upon this
and it helps, I'm happy. If you want it to be slower? No. Suck it up ;).

It will still be basic though...

#### So a little bit further
...just a little

Now we'll go in to multiple parameters while showing how you can have something optional, where a second parameter is optional.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Dipp")) # Now this will use the default "greeting" value that was set. You can change it though
print(greet("Dipp", "Hi")) # Will now change from "Hello", to "Hi" 
```
Okay, cool, but what if you want it to not take in a specific amount of variables?

```python
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply_all(1, 2, 3, 4, 5))
```

Passing a variable length dictonary to functions

```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Dipp", age=24, role="Developer")
```

#### Inner Nested Functions

> Ooooooooo....Defining functions within functions

```python
def outer(x):
    def inner(y):
        return x + y
    return inner(5)

print(outer(10)) # Should print 15
```

___

## Decorators

### What is a decorator 

- A decorator is a higher order function and enhances its behaviour without modifying its internal code 
- Defined using the `@` syntax

```python
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
```

#### So.... How does a decorator actually work?

- The decorator wraps the original function, replacing it with a "Wrapper Function"
- The wrapper function runs extra code clearly before or after the original function

Here's a step-by-step:

```python
#Step 1: Define a decorator
def uppercase_decorator(func):
    print("Before")
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        print(modified_result)
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

```

Could just be simplified to:

```python
@upperclass_decorator
def greet():
    return "hey"

print(greet())
```

Now if you want to log it as it goes:

```python
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
```

And a decorator that takes in an argument

```python
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
```

## Think that's it for today actually. Some basic decorators and functions...
