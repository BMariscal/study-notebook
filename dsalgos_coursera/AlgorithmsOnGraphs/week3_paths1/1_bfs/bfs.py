#Uses python3

import sys
import queue

def distance(adj, s, t):
    distance_arr = [len(adj)] * len(adj)
    distance_arr[s] = 0

    q = queue.Queue()
    q.put(s)

    while q.empty()  == False:
        v = q.get()

        for i in adj[v]:
            if distance_arr[i] == len(adj):
                q.put(i)
                distance_arr[i] = distance_arr[v] + 1

    return -1 if distance_arr[t] == len(adj) else distance_arr[t]



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
