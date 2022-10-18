#!/usr/bin/env python3

import assertions


def main() -> None:
    print(assertions.asserts([]))
    print(assertions.assert_eq([1, 3], [1, 3]))
    print(assertions.assert_eq((), list(range(5))))
    assertions.assert_eq_prnt("tim", "Tim")
    assertions._print_result(False, values=[23, list(range(5))], show=True)


if __name__ == '__main__':
    main()
