from Producto import Producto
from Nodo import Nodo
from Grafo import Grafo
from itertools import combinations
from collections import deque

### pregunta 006

### pregunta 008
def frequent_itemsets(transactions, k):
    """Encuentra todos los conjuntos de artículos que aparecen en al menos k transacciones."""
    itemset_counts = {}
    
    # Contar la frecuencia de cada subconjunto en las transacciones
    for transaction in transactions:
        for subset_size in range(1, len(transaction) + 1):
            for subset in combinations(transaction, subset_size):
                subset = frozenset(subset)
                itemset_counts[subset] = itemset_counts.get(subset, 0) + 1

    # Filtrar los conjuntos frecuentes que cumplen con la frecuencia mínima k
    frequent_sets = [itemset for itemset, count in itemset_counts.items() if count >= k]
    
    return frequent_sets

### pregunta 007
def build_cooccurrence_graph(transactions, k):
    # Crear instancia del grafo
    grafo = Grafo()
    
    # Diccionario para contar co-ocurrencias de pares de artículos
    cooccurrence_counts = {}

    # Contar las veces que cada par de artículos aparece en las transacciones
    for transaction in transactions:
        for item1, item2 in combinations(transaction, 2):
            pair = frozenset((item1, item2))
            cooccurrence_counts[pair] = cooccurrence_counts.get(pair, 0) + 1

    # Crear nodos para cada artículo único
    productos = {}
    for transaction in transactions:
        for item in transaction:
            if item not in productos:
                productos[item] = Producto(len(productos)+1, item, 0)  # Crear Producto con id único
                grafo.agregar_nodo(productos[item])

    # Agregar aristas para los pares de artículos que cumplen con la frecuencia mínima
    for pair, count in cooccurrence_counts.items():
        if count >= k:
            item1, item2 = tuple(pair)
            grafo.agregar_arista(productos[item1], productos[item2])

    # Graficar el grafo
    return grafo


### pregunta 008

def bfs(nodo, visitados):
    cola = deque([nodo])
    visitados.add(nodo)
    grupo = [nodo.producto.name]  # Agrega el nombre del nodo inicial
    while cola:
        actual = cola.popleft()
        for amigo in actual.get_friends():  # Asegúrate de usar el método adecuado para obtener los amigos
            if amigo not in visitados:
                visitados.add(amigo)
                cola.append(amigo)
                grupo.append(amigo.producto.name)  # Almacena el nombre del amigo en el recorrido
    return grupo






def find_communities(grafo):
    visitados = set()
    grupos = 0
    conjunto = []
    # Itera sobre las claves (nodos) del diccionario de nodos
    for nodo in grafo.listaNodos.values():
        if nodo not in visitados:
            conjunto.append(bfs(nodo, visitados))
            grupos += 1
    return conjunto

