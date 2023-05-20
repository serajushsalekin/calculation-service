import math
from functools import reduce
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def cal(option, value):
    """
    :param option: sq, sqrt, fact, fibbo
    :param value: integer only
    :return: result of calculation
    """
    return get_result(option, value)


@router.get("/hello/{name}")
async def say_hello(name: str):
    """
    :param name: str
    :return: greetings message [dict]
    """
    return {"message": f"Hello {name}"}


def get_result(option_name, value):
    value = int(value)
    if option_name == 'sq':
        return int(value) ** 2
    elif option_name == 'sqrt':
        return math.sqrt(value)
    elif option_name == 'fact':
        return math.factorial(value)
    elif option_name == 'fibbo':
        return reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (value - 2), [0, 1])
    else:
        return value
