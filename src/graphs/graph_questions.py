import collections


def dfs_traverse_iter(n, graph):
    """
    DFS iterative approach
    """

    stack = []
    visited = {i:0 for i in range(n)}
    for i in range(n):
        if visited[i] != 0:
            continue

        stack.append(i)

        while stack:
            v = stack.pop()
            visited[v] = 1
            for u in graph[v]:
                if not visited[u]:
                    stack.append(u)
    return


def dfs_recur(n, graph):
    visited = {i:0 for i in range(n)}

    def dfs(u):
        visited[u] = 1
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

    for i in range(n):
        if not visited[i]:
            dfs(i)


def bfs_iter(n, graph):
    """
    BFS iterative approach
    """

    queue = collections.deque()
    visited = {i:0 for i in range(n)}
    for i in range(n):
        if visited[i] != 0:
            continue

        queue.append(i)

        while queue:
            u = queue.popleft()
            visited[u] = 1
            for v in graph[u]:
                if not visited[v]:
                    queue.append(v)
    return


def topological_sort_dfs(n, course_list):
    """
    DAG: course schedule
    :param n:
    :param graph:
    :return: List[int]
    """

    graph = collections.defaultdict(list)
    for c1, c2 in course_list:
        graph[c1].append(c2)

    topo_sort = []
    visited = {i:0 for i in range(n)}

    def dfs(course):
        nonlocal topo_sort
        visited[course] = 1
        for nc in graph[course]:
            if not visited[nc]:
                dfs(nc)
        topo_sort.append(course)

    for c in range(n):
        if not visited[c]:
            dfs(c)

    return topo_sort


def topological_sort_bfs(n, course_list):
    indegree = {i:0 for i in range(n)}
    graph = collections.defaultdict(set)

    for c1, c2 in course_list:
        graph[c1].append(c2)
        indegree[c2] += 1

    queue = collections.deque([u for u, d in indegree.items() if d == 0])
    topological_sort = []
    while queue:
        u = queue.popleft()
        topological_sort.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return topological_sort

def biparatite_graph_check_bfs(adj_list):
    """
    :param adj_list:
    :return:
    """
    color_map = {}
    queue = collections.deque(0)
    color_map[0] = 0
    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if v in color_map:
                if color_map[v] == color_map[u]:
                    return False
            else:
                color_map[v] = 1 ^ color_map[u]
                queue.append(v)
    return True

def biparatite_graph_check_dfs(adj_list):
    """
    :param adj_list:
    :return:
    """
    color_map = {}
    stack = [0]
    color_map[0] = 0

    while stack:
        u = stack.pop()
        for v in adj_list[u]:
            if v in color_map:
                if color_map[v] == color_map[u]:
                    return False
            else:
                color_map[v] = 1 ^ color_map[u]
                stack.append(v)
    return True















