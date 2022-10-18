# Assertions

### asserts(value: Any)

    Check if the value passed is True. it is diffrent to the core `assert`. 
    It returns True or False. No exception is returned.
    
    E.g:
    ```
    >>> asserts(True)
    True

    Below test is expected to Fail.

    >>> asserts([])
    True
    ```


### assert\_eq(value1: Any, value2: Any) -> bool
    
    Gets two positional parameters. Check if the parameters
    are the same type. 
    Then check if the parameters are the same. 

    '''

    >>> assert_eq("Lagos", "new yoke")
    False

    >>> assert_eq([0, 1, 2], list(range(3)))
    True

    '''


### asserts\_prnt(value: Any) -> None

    Prints returned value of the function `asserts`. Returns None.


### assert\_eq\_prnt(value1: Any, value2: Any) -> None

    Prints returned values of the function `assert_eq`. Returns None


### \_print\_result(status: bool, *, values: list[Any] = [None], show=False) -> None
    
    it prints out either True or False. It can also
    `show` the reason, if the result is false. 
    _print_result is a private function in this package.
    it takes; a bool, a list and a bool variable. It returns None.
    
