class InvalidAgeError (Exception):
    pass
try:
    name = str(input("What' your name: "))
    if name.isdigit():
        raise ValueError("The name can't be a number ❌")
except ValueError as e:
    print(f"Error [ValueError]:The name is not a number: {e}")
try:
    age = int(input("What's you age: "))
    if age <= 0 or age >100:
        raise InvalidAgeError("use a real age")
except InvalidAgeError as e:
    print(f"Error [InvalidAgeError]: this is no a age: {e}")
except ValueError as e:
    print(f"Error [ValueError]: this is no a age: {e}")
