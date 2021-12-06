# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

# Напишіть функцію з назвою oops, яка при виклику явно викликає виняток IndexError.
# Потім напишіть іншу функцію, яка викликає oops всередині оператора try/except, щоб уловити помилку.
# Що станеться, якщо змінити помилку на виклик KeyError замість IndexError?

def oops():
    raise IndexError


def another():
    try:
        numbers = list(range(0, 10))
        print(numbers[10])
        pass
    except oops():
        pass


another()