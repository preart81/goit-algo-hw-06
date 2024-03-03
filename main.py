import networkx as nx
import matplotlib.pyplot as plt

from graphs import dfs_iterative, bfs_iterative, dijkstra

# Граф метро Києва
G = nx.Graph()

# ----------------- Станції метро -----------------
line_red = [
    "Академмістечко",
    "Житомирська",
    "Святошин",
    "Нивки",
    "Берестейська",
    "Шулявська",
    "Політехнічний інститут",
    "Вокзальна",
    "Університет",
    "Театральна",
    "Хрещатик",
    "Арсенальна",
    "Дніпро",
    "Гідропарк",
    "Лівобережна",
    "Дарниця",
    "Чернігівська",
    "Лісова",
]
line_blue = [
    "Героїв Дніпра",
    "Мінська",
    "Оболонь",
    "Почайна",
    "Тараса Шевченка",
    "Контрактова площа",
    "Поштова площа",
    "Майдан Незалежності",
    "Площа Українських Героїв",
    "Олімпійська",
    "Палац Україна",
    "Либідська",
    "Деміївська",
    "Голосіївська",
    "Васильківська",
    "Виставковий центр",
    "Іподром",
    "Теремки",
]
line_green = [
    "Сирець",
    "Дорогожичі",
    "Лук'янівська",
    "Золоті ворота",
    "Палац спорту",
    "Кловська",
    "Печерська",
    "Звіринецька",
    "Видубичі",
    "Славутич",
    "Осокорки",
    "Позняки",
    "Харківська",
    "Вирлиця",
    "Бориспільська",
    "Червоний хутір",
]
# --------------- Транзитні станції ----------------
transit_stations = [
    ("Золоті ворота", "Театральна"),
    ("Хрещатик", "Майдан Незалежності"),
    ("Палац спорту", "Площа Українських Героїв"),
]

# --------------- Заповнення графа ----------------
# Червона лінія
G.add_nodes_from(line_red, line="Червона", color="red")
G.add_edges_from(zip(line_red[:-1], line_red[1:]), weight=1, color="red")

# Синя лінія
G.add_nodes_from(line_blue, line="Синя", color="blue")
G.add_edges_from(zip(line_blue[:-1], line_blue[1:]), weight=1, color="blue")

# Зелена лінія
G.add_nodes_from(line_green, line="Зелена", color="green")
G.add_edges_from(zip(line_green[:-1], line_green[1:]), weight=1, color="green")

# Транзитні станції
G.add_edges_from(transit_stations, weight=3, line="Транзит", color="black")

G_node_colors = [G.nodes[node]["color"] for node in G.nodes]
G_edge_colors = [G.edges[edge]["color"] for edge in G.edges]


# -------------- Візуалізація графа --------------------
options = {
    "node_size": 500,  # size of node
    "width": 3,  # line width of edges
}

# pos = nx.shell_layout(G, [line_red, line_blue, line_green])
# pos = nx.spring_layout(G)
pos = nx.kamada_kawai_layout(G)


nx.draw(
    G,
    pos=pos,
    with_labels=True,
    node_color=G_node_colors,
    edge_color=G_edge_colors,
    **options,
)

# Основні характеристики графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"Кількість станцій: {num_nodes}")
print(
    f"Кількість з'єднань станцій: {num_edges}, з них:\n"
    f" - піших переходів: {len(transit_stations)}\n"
    f" - сполучень метро: {num_edges - len(transit_stations)}"
)

# Перевірка на зв'язність
is_connected = nx.is_connected(G)
if is_connected:
    print("Схема метро є зв'язним графом")
else:
    print("Схема метро не є зв'язним графом")

# Ступінь центральності (Degree Centrality)
print()
print("Станції з найбільшою центральністю (Degree Centrality):")
degree_centrality = nx.degree_centrality(G)

top_centrality_stations = sorted(
    degree_centrality.items(), key=lambda item: item[1], reverse=True
)[:6]
for station, centrality in top_centrality_stations:
    print(f"Станція {station:.<28}{centrality:.8f}")

# Близькість вузла (Closeness Centrality)
print()
print("Станції з найвищою близкістю вузла (Closeness Centrality):")
closeness_centrality = nx.closeness_centrality(G)
top_closeness_stations = sorted(
    closeness_centrality.items(), key=lambda item: item[1], reverse=True
)[:8]
for station, closeness in top_closeness_stations:
    print(f"Станція {station:.<28}{closeness:.8f}")


# Ступінь (Degree)
degrees = dict(G.degree())
print()
print("Станції з навищим ступенем:")
for node, degree in degrees.items():
    if degree > 2:
        print(f"Станція {node:.<28}{degree}")
print()
print("Кінцеві станції:")
for node, degree in degrees.items():
    if degree == 1:
        print(f"Станція {node:.<28}{degree}")


# Критерії пошуку
start_station = "Театральна"
end_station = "Арсенальна"
# ---------------- Пошук у глибину (DFS) ------------------
print()
print(f"Пошук у глибину (DFS) для початкової станції {start_station}:")

dfs = dfs_iterative(G, start_station, end_station)
print(f"Відвідано станцій: {len(dfs)}, Відвідані станції DFS: \n{dfs}")

# ---------------- Пошук в ширину (BFS) ------------------
print()
print(f"Пошук в ширину (BFS) для початкової станції {start_station}:")

bfs = bfs_iterative(G, start_station, end_station)
print(f"Відвідано станцій: {len(bfs)}, Відвідані станції BFS: \n{bfs}")

# ---------------- Пошук оптимального маршруту (алгоритм Декйстри) ------------------
print()
print(
    f"Пошук оптимального маршруту (алгоритм Декйстри) між станціями {start_station} і {end_station}:"
)

# Підготовка графа для функції dijkstra
prepared_G = {
    node: {neighbor: data.get("weight", 1) for neighbor, data in neighbors.items()}
    for node, neighbors in G.adj.items()
}

d = dijkstra(prepared_G, start_station, end_station)
print(
    f"Оптимальний маршрут між станціями {start_station} і {end_station}:"
    f"\nВідстань: {d['distance']}\nСтанції: {d['path']}"
)


# plt.show()
