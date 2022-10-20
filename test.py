#!/usr/bin/env python3

from assertions import asserts, asserts_prnt, assert_eq, assert_eq_prnt, _print_result

def main() -> None:
    print(asserts([]))
    print(assert_eq([1, 3], [1, 3]))
    print(assert_eq((), list(range(5))))
    asserts_prnt(0)
    assert_eq_prnt("tim", "Tim", show=True)
    _print_result(False, values=[23, list(range(5))], show=True)


if __name__ == '__main__':
    main()
