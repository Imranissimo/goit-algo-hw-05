import re
from typing import Callable

def generator_numbers(text: str):

    for match in re.findall(r' (\d+(?:\.\d+)?) ', text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    return sum(func(text))
