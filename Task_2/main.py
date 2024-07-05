import re
from typing import Callable

# Define a function generator_numbers() that will parse the text, 
# identify all float numbers and return them as a generator.
def generator_numbers(text: str):
    # Create a list of all numbers.
    numbers = re.findall(r"\d+\.\d+", text)
    # Return each number.
    for number in numbers:
        yield float(number)

# Calculation of total profit.
def sum_profit(text: str, generator: Callable):
    # Return the sum of a generated numbers.
    return sum([number for number in generator(text)])

# Example.

text = "Загальний дохід працівника складається з декількох частин: "\
"1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")