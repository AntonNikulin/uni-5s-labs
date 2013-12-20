from collections import deque
                #1  2  3  4  5
graph =       [ [0, 0, 0, 1, 1], #1
                [0, 0, 1, 0, 0], #2
                [0, 1, 0, 1, 0], #3
                [1, 0, 1, 0, 1], #4
                [1, 0, 0, 1, 0], #5
                ]

queue = deque()
source = 0
color = ['W' for i in range(5)]
res = []
res.append(source+1)

queue.append(source)
color[source] = 'B'     #visited

while len(queue):
    u = queue.popleft()
    for v in range(5):
        if graph[u][v] == 1 and color[v] == 'W':
            color[v] = 'B'
            queue.append(v)
            res.append(v+1)

print res
