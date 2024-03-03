"""Пошук у глибину (DFS)

Пошук у глибину (DFS) виконується шляхом відвідування вершини, а потім
рекурсивного відвідування всіх сусідніх вершин, які ще не були відвідані.
Алгоритм DFS може бути ефективним для знаходження циклу у графі або перевірки
зв'язності графу. Однак DFS може бути неефективним для пошуку найкоротшого шляху
у графі, особливо у графах з великою кількістю вершин та ребер."""


def dfs_iterative(graph, start_vertex, end_vertex=None) -> list:
    """Пошук в глибину DFS

    Ітеративний пошук в глибину з використанням стеку.

    Параметри:
        graph: dict - граф;
        start_vertex - початкова вершина.
        end_vertex - кінцева вершина.
    Повертає:
        visited - відвідані вершини в порядку відвідування.
    """
    visited = []
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]
    while stack and end_vertex not in visited:
        # Вилучаємо вершину зі стеку
        curr_vertex = stack.pop()
        if curr_vertex not in visited:
            # print(curr_vertex, end="-") # DEBUG
            # Відвідуємо вершину
            # visited.add(curr_vertex)
            visited.append(curr_vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(list(reversed(list(graph[curr_vertex]))))
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

    # Виклик функції DFS
    print(f"{dfs_iterative(graph, 'A') = }")
    print(f"{dfs_iterative(graph, 'A','F') = }")

    import matplotlib.pyplot as plt
    import networkx as nx

    nx.draw(nx.Graph(graph), with_labels=True)
    plt.show()
