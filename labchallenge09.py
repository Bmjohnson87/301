# help from classmate T.Taylor and bard to understand

a = 5
b = 10

# Equals
if a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is not equal to {b}")

# Not equals
if a != b:
    print(f"{a} is not equal to {b}")
else:
    print(f"{a} is equal to {b}")  # This won't be printed as the previous condition is true

# Less than
if a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is not less than {b}")

# Less than or equal to
if a <= b:
    print(f"{a} is less than or equal to {b}")
else:
    print(f"{a} is not less than or equal to {b}")

# Greater than
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is not greater than {b}")

# Greater than or equal to
if a >= b:
    print(f"{a} is greater than or equal to {b}")
else:
    print(f"{a} is not greater than or equal to {b}")

# Example with elif

if a % 2 == 0:
    print(f"{a} is even")
elif a % 3 == 0:
    print(f"{a} is divisible by 3")
else:
    print(f"{a} is neither even nor divisible by 3")

# Example with both elif and else

if a > b:
    print(f"{a} is the largest number")
elif a < b:
    print(f"{b} is the largest number")
else:
    print(f"{a} and {b} are equal")
