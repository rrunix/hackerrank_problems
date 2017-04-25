#source https://www.hackerrank.com/challenges/torque-and-development
from collections import defaultdict

Q = int(input())

for _ in range(Q):
    n, m, clib, croad = map(int, input().split(" "))

    cost = 0
    if clib < croad:
        for i in range(m):
            input()

        cost = n * clib
    else:
        graph = defaultdict(list)
        for i in range(m):
            u, v = map(int, input().split(" "))
            graph[u].append(v)
            graph[v].append(u)

        components = []
        while graph:
            component_elements = set()
            elements_to_review = [next(iter(graph))]

            while elements_to_review:
                node = elements_to_review.pop()
                component_elements.add(node)

                if node in graph:
                    elements_to_review.extend(graph[node])
                    del graph[node]

            components.append(component_elements)

        visited_cities = 0
        for component in components:
            n_cities = len(component)
            cost += min(n_cities * clib, (n_cities - 1) * croad + clib)
            visited_cities += n_cities

        #Don't forget the cities that are not connected to any other.
        cost += (n - visited_cities) * clib

    print (cost)
