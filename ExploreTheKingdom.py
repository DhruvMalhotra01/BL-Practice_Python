graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

startNode = 'A'
def Kingdom(graph,startNode):
    visited = []

    def dfs(node):
        visited.append(node)
        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(startNode)
    return visited

def func4():
    order = Kingdom(graph,startNode)
    print(" -> ".join(order))
    return order


if __name__ == "__main__":
    func4()
