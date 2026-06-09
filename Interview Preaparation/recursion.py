# Interview preparation practice module.
# Contains recursion fundamentals and recursive search patterns.

from __future__ import annotations


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def binary_search_recursive(nums: list[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    return binary_search_recursive(nums, target, left, mid - 1)


if __name__ == "__main__":
    assert factorial(5) == 120
    assert fibonacci(7) == 13
    assert reverse_string("khaled") == "delahk"
    assert binary_search_recursive([1, 3, 5, 7], 5, 0, 3) == 2
