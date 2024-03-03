"""
Алгоритм Дейкстри 

Алгоритм Дейкстри — це алгоритм пошуку найкоротшого шляху у графі з невід'ємними
вагами ребер від однієї вершини до всіх інших."""

import heapq


def dijkstra(graph, start_vertex, end_vertex=None) -> dict:
    """Алгоритм Дейкстри

    Параметри:
        graph: dict - граф;
        start_vertex - початкова вершина;
        end_vertex - кінцева вершина.
    Повертає dict:
        distances:dict|int - відстані від початкової до всіх вершин, або відстань до заданої end_vertex.;
        path:list - оптимальний шлях якщо задана end_vertex або None.

    """
    # Ініціалізація відстаней і списку попередніх вершин
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start_vertex] = 0
    previous_vertices = {vertex: None for vertex in graph}

    # Пріоритетна черга для зберігання вершин і відстаней
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо в списку вже є коротший шлях - ігноруємо цю вершину
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден более короткий путь до соседа, обновляем расстояние и предыдущую вершину
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    # Если указана конечная вершина, строим оптимальный путь
    if end_vertex:
        path = []
        current_vertex = end_vertex
        while previous_vertices[current_vertex] is not None:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.insert(0, start_vertex)
        return {"distance": distances[end_vertex], "path": path}
    else:
        # return {"distance": distances, "path": previous_vertices}
        return {"distance": distances, "path": None}


if __name__ == "__main__":
    # Приклад графа у вигляді словника
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        "D": {"B": 3, "C": 2, "E": 4},
        "E": {"D": 4},
    }

    print(f"{graph = }")

    print(f"{dijkstra(graph, 'A') = }")
    print(f"{dijkstra(graph, 'A', 'D') = }")
    print(f"{dijkstra(graph, 'A', 'E') = }")

    import matplotlib.pyplot as plt
    import networkx as nx

    nx.draw(nx.Graph(graph), with_labels=True)
    plt.show()
