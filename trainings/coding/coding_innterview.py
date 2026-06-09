# Interview preparation practice module.
# Contains extra interview snippets.

from __future__ import annotations


def circular_shift_right(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k %= len(arr)
    if k == 0:
        return arr[:]
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    sample = [5, -3, 10, -8, 0, 1, 2, 7, -18, 25]
    assert circular_shift_right(sample, 3) == [7, -18, 25, 5, -3, 10, -8, 0, 1, 2]
