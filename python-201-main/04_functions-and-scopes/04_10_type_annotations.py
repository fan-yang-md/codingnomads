# Add type annotations to the three functions shown below.

def multiply(num1: int or float, num2: int or float) -> int or float:
    return num1 * num2

def greet(greeting: str, name: str) -> str:
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args: str) -> str: 
    [print(f"* {item}") for item in args]
    return args

#shopping_list('tomatoes', 'bananas')
