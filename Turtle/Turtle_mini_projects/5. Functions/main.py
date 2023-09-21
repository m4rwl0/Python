def say_hello(name):
    # def
    # function name
    # argument/paramiter
    print("Hello " + name)


say_hello("Martyna")
say_hello("Michael")
say_hello("User")


def say_how_are_you(name_test):
    print("How are you " + name_test)


say_how_are_you("Steve")
say_how_are_you("Bob")
say_how_are_you("Vicky")

# Along with inputs into a function, we can also have outputs.
# The return will end the fuction and return value


def add_numbers(a, b):
    sum = a + b
    return sum


num = add_numbers(129, 20202020)
print(num)
