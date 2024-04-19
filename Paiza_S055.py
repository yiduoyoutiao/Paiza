# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

# get H W
input_line = input()
input_array = input_line.split()
H = int(input_array[0])
W = int(input_array[1])

# get animal location
A_matrix = [["-" for _ in range(W)] for _ in range(H)]
for i in range(H):
    input_line = input()
    input_array = input_line.split()
    for j in range(W):
        A_matrix[i][j] = input_array[j]

# get N
input_line = input()
input_array = input_line.split()
N = int(input_array[0])

# get prey-predator relationship
P_matrix = [["-" for _ in range(2)] for _ in range(N)]
for i in range(N):
    input_line = input()
    input_array = input_line.split()
    for j in range(2):
        P_matrix[i][j] = input_array[j]

# Creat Graph based on prey-predator relationship
graph = {}
for start, end in P_matrix:
    if start not in graph:
        graph[start] = []
    graph[start].append(end)

for start, end in P_matrix:
    if end not in graph:
        graph[end] = []

# Breadth first search
positions = {A_matrix[i][j]: (i, j) for i in range(len(A_matrix)) for j in range(len(A_matrix[0]))}

from collections import defaultdict, deque




from collections import deque

def bfs_update(matrix, graph, start_nodes):
    queue = deque(start_nodes)
    visited = set(start_nodes)

    while queue:
        current = queue.popleft()
        # 在矩阵中找到当前节点所有的位置
        positions = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == current]

        # 对每个找到的位置处理其周围8个邻居
        for x, y in positions:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue  # 跳过自己
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                        neighbor = matrix[nx][ny]
                        # 检查邻居是否是当前节点的直接后继节点
                        if neighbor in graph[current]:
                            matrix[nx][ny] = '-'

        # 将未访问的后继节点加入队列
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return matrix




# 建立起始节点
in_degrees = defaultdict(int)
for node in graph:
    for target in graph[node]:
        in_degrees[target] += 1
start_nodes = [node for node in graph if in_degrees[node] == 0]



updated_matrix = bfs_update(A_matrix, graph, start_nodes)

for row in updated_matrix:
    # 将每行的元素转换为字符串，并用空格分隔
    print(" ".join(row))