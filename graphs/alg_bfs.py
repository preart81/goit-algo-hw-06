"""Пошук у ширину (BFS)

Пошук у ширину (BFS) відрізняється від DFS тим, що він відвідує всі вершини
на певному рівні перед тим, як перейти до наступного рівня. BFS є корисним для
знаходження найкоротшого шляху в незважених графах та при розв'язку завдань, які
вимагають відвідування вершин у порядку, віддаленому від вихідної вершини."""

from collections import deque


def bfs_iterative(graph, start_vertex, end_vertex=None) -> list:
    """
    Ітеративний пошук в ширину BFS

    Параметри:
        graph: dict
            граф;
        start_vertex: Any
            початкова вершина
        end_vertex: Any, optional
            кінцева вершина, за замовчуванням None

    Повертає:
        visited: list
            відвідані вершини в порядку відвідування.
    """
    visited = []  # Список відвіданих вершин
    queue = deque([start_vertex])  # Черга для збереження вершин для обходу

    while queue:
        current_vertex = queue.popleft()  # Беремо першу вершину з черги
        visited.append(current_vertex)

        # Якщо задана кінцева вершина і вона вже відвідана, завершуємо обхід
        if end_vertex and current_vertex == end_vertex:
            break

        # Додаємо сусідів поточної вершини, які ще не відвідані, у чергу
        # neighbors = graph.get(current_vertex, [])
        neighbors = graph[current_vertex]
        for neighbor in neighbors:
            # якщо end_vertex це сусід, або серед сусідів цього сусіда
            if end_vertex and (end_vertex == neighbor or end_vertex in graph[neighbor]):
                # ставимо такого сусіда першим в чергу
                queue.appendleft(neighbor)
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    return visited


if __name__ == "__main__":
    # Представлення графа за допомогою списку суміжності
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    # Запуск алгоритму BFS
    print(f"{bfs_iterative(graph, 'A') = }")
    print(f"{bfs_iterative(graph, 'A', 'D') = }")

    import matplotlib.pyplot as plt
    import networkx as nx

    pos = nx.spring_layout(graph)  # shell_layout(graph)
    nx.draw(nx.Graph(graph), with_labels=True)
    plt.show()
