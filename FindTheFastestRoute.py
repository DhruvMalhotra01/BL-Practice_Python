from collections import deque

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]

start = 'A'
end = 'G'

graph = {}
reverse_graph = {}

for u , v in edges:
    graph.setdefault(u,[]).append(v)
    reverse_graph.setdefault(v,[]).append(u)


def biDirectional(start,end):
    if start == end:
        return 0

    queue_start = deque([start])
    queue_end = deque([end])

    visited_start = {start:0}
    visited_end = {end:0}

    while queue_start and queue_end:
        current_start = queue_start.popleft()

        for neighbour_start in graph.get(current_start,[]):
            if neighbour_start in visited_end:
                return visited_start[current_start] + 1 + visited_end[neighbour_start]

            if neighbour_start not in visited_start:
                visited_start[neighbour_start] = (
                    visited_start[current_start] + 1
                )

                queue_start.append(neighbour_start)

        current_end = queue_end.popleft()

        for neighbour_end in reverse_graph.get(current_end,[]):
            if neighbour_end in visited_start:
                return visited_start[neighbour_end] + 1 + visited_end[current_end]

            if neighbour_end not in visited_end:
                visited_end[neighbour_end] = (
                    visited_end[current_end] + 1
                )

                queue_end.append(neighbour_end)


    return -1

def func3():
    steps = biDirectional(start,end)
    print("steps :",steps)
    return steps


if __name__ == "__main__":
    func3()
