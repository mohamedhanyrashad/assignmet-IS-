import heapq

def uniform_cost_search(graph, start, goal):

    frontier = [(0, start)]

    cost_so_far = {start: 0}

    came_from = {start: None}

    while frontier:

        current_cost, current_node = heapq.heappop(frontier)


        if current_node == goal:

            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path, current_cost  


        for neighbor, cost in graph[current_node]:
            new_cost = current_cost + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start = 'A'
goal = 'D'
path, cost = uniform_cost_search(graph, start, goal)

print("Path:", path)
print("Cost:", cost)
