
import numpy as np
from numpy import inf

# Distance matrix between cities
d = np.array([
    [0, 10, 12, 11, 14],
    [10, 0, 13, 15, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
])

# Parameters
n_ants = 5
n_cities = 5
iterations = 100
evaporation_rate = 0.5
alpha = 1        # pheromone importance
beta = 2         # visibility importance

# Initialization
visibility = 1 / (d + np.eye(n_cities))  # avoid division by zero
visibility[visibility == inf] = 0
pheromone = 0.1 * np.ones((n_cities, n_cities))

best_route = None
best_cost = np.inf

for it in range(iterations):
    routes = np.zeros((n_ants, n_cities + 1), dtype=int)
    routes[:, 0] = 0  # start city is 0 for all ants
    all_costs = []

    for ant in range(n_ants):
        unvisited = list(range(1, n_cities))
        for j in range(1, n_cities):
            current_city = routes[ant, j - 1]
            prob_num = np.power(pheromone[current_city, unvisited], alpha) * np.power(visibility[current_city, unvisited], beta)
            prob = prob_num / np.sum(prob_num)
            next_city = np.random.choice(unvisited, p=prob)
            routes[ant, j] = next_city
            unvisited.remove(next_city)
        routes[ant, -1] = 0  # return to start

        # Calculate total distance for route
        cost = 0
        for j in range(n_cities):
            cost += d[routes[ant, j], routes[ant, j + 1]]
        all_costs.append(cost)

        if cost < best_cost:
            best_cost = cost
            best_route = routes[ant].copy()

    # Update pheromone (evaporation + deposit)
    pheromone *= (1 - evaporation_rate)
    for ant in range(n_ants):
        for j in range(n_cities):
            from_city = routes[ant, j]
            to_city = routes[ant, j + 1]
            pheromone[from_city, to_city] += 1 / all_costs[ant]

print("Best Route (0-indexed):", best_route)
print("Cost of Best Route:", best_cost)
