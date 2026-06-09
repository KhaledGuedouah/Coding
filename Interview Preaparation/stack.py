# Interview preparation practice module.
# Contains stack-based interview utilities.

from __future__ import annotations


def valid_parentheses(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            return False

    return not stack


class QueueWithStacks:
    def __init__(self) -> None:
        self._in: list[int] = []
        self._out: list[int] = []

    def _move(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        self._move()
        return self._out.pop()

    def peek(self) -> int:
        self._move()
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out


class MinStack:
    def __init__(self) -> None:
        self._stack: list[int] = []
        self._mins: list[int] = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        if not self._mins:
            self._mins.append(x)
        else:
            self._mins.append(min(x, self._mins[-1]))

    def pop(self) -> int:
        self._mins.pop()
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._mins[-1]


if __name__ == "__main__":
    assert valid_parentheses("()[]{}")
    assert not valid_parentheses("(]")
