# Coding Interview Preparation Repository

This repository contains Python practice files focused on core coding interview topics:
arrays, linked lists, stacks, recursion, sorting, trees, graphs, and object-oriented programming.

## Goals

- Practice common interview problems repeatedly
- Compare brute-force and optimized solutions
- Build speed in writing clean, correct Python code
- Review data structure patterns before interviews

## Repository Structure

- `arrays.py`: canonical array and two-pointers patterns
- `binary_tree preparation.py`: canonical binary tree and BST patterns
- `graphs.py`: canonical graph traversal and graph algorithms
- `linkedlist.py`: canonical singly linked list patterns
- `doubly_linked_lists.py`: doubly linked list fundamentals
- `sorting.py`: bubble sort, merge sort, and quick sort
- `stack.py`: stack/queue interview utilities (valid parentheses, min stack)
- `recursion.py`: recursion fundamentals and recursive binary search
- `coding/coding_innterview.py`: extra interview snippets
- `OOP.py`: object-oriented programming practice
- `component_inetrconnect.py`: component interface/interconnection practice

## How To Run

From the project folder:

```powershell
C:/Users/khaled.guedouah/AppData/Local/Programs/Python/Python313/python.exe arrays.py
```

Replace `arrays.py` with any target file.

## Recommended Practice Flow

1. Start with one topic per day (for example: arrays).
2. Solve each problem without looking at the existing solution.
3. Compare your version with the file solution.
4. Re-implement the optimized approach from memory.
5. Repeat the same set after 2-3 days for retention.

## Quality Checks

To validate syntax for all project scripts:

```powershell
C:/Users/khaled.guedouah/AppData/Local/Programs/Python/Python313/python.exe -m py_compile *.py
```

For recursive subfolders (including `coding`):

```powershell
Get-ChildItem -Recurse -Filter *.py | ForEach-Object {
  C:/Users/khaled.guedouah/AppData/Local/Programs/Python/Python313/python.exe -m py_compile $_.FullName
}
```

