#!/usr/bin/env python3

def printer(show: bool = False):
    '''Decorator to prints assert_eq. This enables assert_eq to prints,
    without using the print function. It doesn't only prints the result but
    shows the result expected and what is gotten, if the result is `false`.
    '''
    def prints(func):
        def wrapper(*args, **kwargs):
            result = func(*args)
            expected, got = args
            if result == show:
                print(result)
            else:
                print(f'{result} Reason: => ' f'expected: {expected}, got: {got}')
            wrapper.__doc__ = func.__doc__
            wrapper.__name__ = str(func.__name__)
            return result
        return wrapper
    return prints
