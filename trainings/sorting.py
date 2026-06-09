# Interview preparation practice module.
# Contains classic sorting algorithms with interview-friendly complexity tradeoffs.

from __future__ import annotations


def bubble_sort(nums: list[int]) -> list[int]:
    arr = nums[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    merged: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(nums: list[int]) -> list[int]:
    arr = nums[:]

    def partition(low: int, high: int) -> int:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def sort(low: int, high: int) -> None:
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    data = [5, 1, 4, 2, 8]
    assert bubble_sort(data) == [1, 2, 4, 5, 8]
    assert merge_sort(data) == [1, 2, 4, 5, 8]
    assert quick_sort(data) == [1, 2, 4, 5, 8]
