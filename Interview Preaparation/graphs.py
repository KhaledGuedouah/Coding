# Interview preparation practice module.
# Contains graph interview algorithms and traversal patterns.

from __future__ import annotations

import heapq
from collections import defaultdict, deque


class GraphNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.neighbors: list[GraphNode] = []


def build_graph_directed(edges: list[list[int]]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph


def build_graph_undirected(edges: list[list[int]]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def dfs_recursive(start: int, graph: dict[int, list[int]]) -> list[int]:
    order: list[int] = []
    visited: set[int] = set()

    def dfs(node: int) -> None:
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for nei in graph.get(node, []):
            dfs(nei)

    dfs(start)
    return order


def dfs_iterative(start: int, graph: dict[int, list[int]]) -> list[int]:
    stack = [start]
    visited: set[int] = set()
    order: list[int] = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nei in reversed(graph.get(node, [])):
            if nei not in visited:
                stack.append(nei)
    return order


def bfs(start: int, graph: dict[int, list[int]]) -> list[int]:
    q: deque[int] = deque([start])
    visited = {start}
    order: list[int] = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return order


def number_of_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def flood_fill(r: int, c: int) -> None:
        stack = [(r, c)]
        grid[r][c] = "0"
        while stack:
            cr, cc = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    stack.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                flood_fill(r, c)
    return count


def clone_graph(start_node: GraphNode | None) -> GraphNode | None:
    if not start_node:
        return None
    old_to_new: dict[GraphNode, GraphNode] = {start_node: GraphNode(start_node.val)}
    q: deque[GraphNode] = deque([start_node])

    while q:
        node = q.popleft()
        for nei in node.neighbors:
            if nei not in old_to_new:
                old_to_new[nei] = GraphNode(nei.val)
                q.append(nei)
            old_to_new[node].neighbors.append(old_to_new[nei])

    return old_to_new[start_node]


def can_finish_courses_dfs(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    state = [0] * num_courses

    def dfs(course: int) -> bool:
        if state[course] == 1:
            return False
        if state[course] == 2:
            return True
        state[course] = 1
        for nei in graph[course]:
            if not dfs(nei):
                return False
        state[course] = 2
        return True

    return all(dfs(i) for i in range(num_courses))


def can_finish_courses_kahn(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    q: deque[int] = deque([i for i in range(num_courses) if indegree[i] == 0])
    visited = 0

    while q:
        node = q.popleft()
        visited += 1
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return visited == num_courses


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    parent: dict[int, int] = {}

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> bool:
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        parent[root_y] = root_x
        return True

    for u, v in edges:
        if u not in parent:
            parent[u] = u
        if v not in parent:
            parent[v] = v
        if not union(u, v):
            return [u, v]
    return []


def is_valid_tree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited: set[int] = set()
    stack = [(0, -1)]
    while stack:
        node, parent = stack.pop()
        if node in visited:
            return False
        visited.add(node)
        for nei in graph[node]:
            if nei != parent:
                stack.append((nei, node))
    return len(visited) == n


def dijkstra(adj: list[list[tuple[int, int]]], src: int) -> list[float]:
    # adj[u] contains tuples (v, weight).
    dist = [float("inf")] * len(adj)
    dist[src] = 0.0
    pq: list[tuple[float, int]] = [(0.0, src)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue
        for v, w in adj[u]:
            candidate = curr_dist + w
            if candidate < dist[v]:
                dist[v] = candidate
                heapq.heappush(pq, (candidate, v))

    return dist


if __name__ == "__main__":
    base_graph = build_graph_undirected([[0, 1], [0, 2], [1, 3]])
    assert dfs_recursive(0, base_graph) == [0, 1, 3, 2]
    assert bfs(0, base_graph) == [0, 1, 2, 3]
    assert can_finish_courses_dfs(2, [[1, 0]])
    assert can_finish_courses_kahn(2, [[1, 0]])
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
