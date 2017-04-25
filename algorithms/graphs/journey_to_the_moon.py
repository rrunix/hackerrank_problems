#source https://www.hackerrank.com/challenges/journey-to-the-moon
from collections import  defaultdict

def dfs(graph):
    graph = dict(graph)

    component_counts = []
    while graph:
        component_elements = set()
        elements_to_review = [next(iter(graph))]

        while elements_to_review:
            node = elements_to_review.pop()
            component_elements.add(node)

            if node in graph:
                elements_to_review.extend(graph[node])
                del graph[node]

        component_counts.append(len(component_elements))
    return component_counts

N, P = map(int, input().split(" "))
pairs = defaultdict(list)

for _ in range(P):
    person1, person2 = map(int, input().split(" "))
    pairs[person1].append(person2)
    pairs[person2].append(person1)

astronauts_per_country = dfs(pairs)

for _ in range(N - sum(astronauts_per_country)):
    astronauts_per_country.append(1)

people_so_far = 0
num_pairs = 0

for num_per_country in astronauts_per_country:
    num_pairs += people_so_far * num_per_country
    people_so_far += num_per_country

print (num_pairs)
