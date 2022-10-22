#!/usr/bin/env python3

from typing import Any
from decofunc import printer, deprecated


def asserts(value: Any) -> bool:
    '''Check if the value passed is True.
    it is diffrent to the core `assert`. It returns
    True or False. No exception is returned.

    >>> asserts(True)
    True

    Below test is expected to Fail.

    >>> asserts([])
    True

    '''
    if value:
        return True
    else:
        return False


@printer(show=True)
def assert_eq(value1: Any, value2: Any) -> bool:
    '''
    Gets two positional parameters. Check if the parameters
    are the same type.
    Then check if the parameters are the same.

    >>> assert_eq("Lagos", "new yoke")
    False

    >>> assert_eq([0, 1, 2], list(range(3)))
    True

    '''
    if type(value1) is type(value2):
        return value1 == value2
    return False


def asserts_prnt(value: Any) -> None:
    '''Prints returned value of the function `asserts`. Returns None.'''
    print(asserts(value))


@deprecated(message='Deprecated. Use `assert_eq`, it does what you expects.')
def assert_eq_prnt(value1: Any, value2: Any, *, show: bool = False) -> None:
    '''Prints returned values of the function `assert_eq`. Returns None'''
    result = assert_eq(value1, value2)
    _print_result(result, values=[value1, value2], show=show)


def _print_result(status: bool, *, values: list[Any] = [None], show=False) -> None:
    '''
    it prints out either True or False. It can also
    `show` the reason, if the result is false.
    _print_result is a private function in this package.
    it takes; a bool, a list and a bool variable. It returns None.
    '''
    if type(values) is not list or len(values) != 2:
        raise Exception(
            "Parameter `values` must be a list of atleast 2 values")
    if status:
        print(status)
    else:
        expected, got = values
        if show:
            print(f'{status} Reason: => ' f'expected: {expected}, got: {got}')
        else:
            print(status)
