# ==========================
# Python Built-in Data Types
# ==========================

# There are 8 main categories and 15 built-in data types in Python.
# Below is the full list with explanations and examples.

# 1. Numeric Types (3 types)
# ---------------------------

# int: Whole numbers, positive or negative
age = 25
year = -1990

# float: Decimal (floating-point) numbers
pi = 3.14159
temperature = -5.6

# complex: Numbers with real and imaginary parts
z = 2 + 3j
another_complex = complex(4, -2)


# 2. Text Type (1 type)
# ---------------------

# str: A sequence of Unicode characters (text)
language = "Python"
greeting = 'Hello, Habil!'


# 3. Boolean Type (1 type)
# ------------------------

# bool: Logical value, either True or False
is_online = True
has_permission = False


# 4. Sequence Types (3 types)
# ---------------------------

# list: Ordered, changeable, allows duplicates
fruits = ["apple", "banana", "cherry"]

# tuple: Ordered, unchangeable (immutable), allows duplicates
colors = ("red", "green", "blue")

# range: Sequence of numbers, often used for loops
numbers = range(0, 5)  # Represents 0 to 4


# 5. Set Types (2 types)
# ----------------------

# set: Unordered, unindexed, no duplicates
unique_ids = {1, 2, 3, 3}  # → {1, 2, 3}

# frozenset: Immutable version of a set
frozen_ids = frozenset(["a", "b", "c"])


# 6. Mapping Type (1 type)
# ------------------------

# dict: Key-value pairs, very flexible
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}


# 7. Binary Types (3 types)
# -------------------------

# bytes: Immutable sequence of bytes
b = b"hello"

# bytearray: Mutable sequence of bytes
ba = bytearray(5)  # bytearray of 5 zero bytes

# memoryview: A view object of binary data
mv = memoryview(b)


# 8. None Type (1 type)
# ---------------------

# NoneType: Represents a null value or no value
x = None


# ✅ Global Scope: Accessible everywhere (outside functions)
# ✅ Local Scope: Only inside the function where it's defined
# ✅ Enclosing Scope: From outer function, visible to inner functions (closure)
# ✅ Built-in Scope: Python's built-in names like len(), print(), range(), etc.

# ------------------------------------------
# 🔍 What is Variable Scope?
# Scope means the area in the code where a variable is accessible.
# ------------------------------------------

# 🟡 Global Scope: Variable defined outside any function
x = "I'm global"

def outer_function():
    # 🔵 Enclosing Scope: Outer function's variable (seen by inner function)
    y = "I'm in outer function"

    def inner_function():
        # 🔴 Local Scope: Only exists inside this inner function
        z = "I'm local to inner function"

        # Accessing all three variables
        print(x)  # Access global variable
        print(y)  # Access enclosing variable
        print(z)  # Access local variable

    inner_function()

    # print(z)  # ❌ This will cause an error (z is local to inner_function)

outer_function()

# print(y)  # ❌ This will also cause an error (y is local to outer_function)

# ⚪ Built-in Scope: Functions that are always available in Python
print(len("scope"))  # 'len' is a built-in function
