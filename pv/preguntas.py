from Grafo import Grafo
from collections import deque
from conectNeo4j import obtener_grafo_desde_neo4j


def conect():
    
    # Obtener el grafo poblado desde Neo4j
    mi_grafo = obtener_grafo_desde_neo4j()

    # Mostrar el grafo cargado
    mi_grafo.show()




### pregunta 001
def dfs(nodo, visitados):
    visitados.add(nodo)
    for amigo in nodo.amigos:
        if amigo not in visitados:
            dfs(amigo, visitados)
            


def bfs(nodo, visitados):
    cola = deque([nodo])
    visitados.add(nodo)
    while cola:
        actual = cola.popleft()
        for amigo in actual.amigos:
            if amigo not in visitados:
                visitados.add(amigo)
                cola.append(amigo)

def find_friend_groups_dfs(grafo):
    visitados = set()
    grupos = 0

    # Itera sobre las claves (nodos) del diccionario de nodos
    for nodo in grafo.listaNodos.values():
        if nodo not in visitados:
            dfs(nodo, visitados)
            grupos += 1
    return grupos


def find_friend_groups_bfs(grafo):
    visitados = set()
    grupos = 0

    # Itera sobre las claves (nodos) del diccionario de nodos
    for nodo in grafo.listaNodos.values():
        if nodo not in visitados:
            bfs(nodo, visitados)
            grupos += 1
    return grupos

### pregunta 002
def recommend_friends(grafo):
    recomendaciones = {}

    # Itera sobre cada nodo (persona) en el grafo
    for nodo in grafo.listaNodos.values():
        recomendados = set()  # Usamos un conjunto para evitar duplicados
        amigos_directos = set(nodo.amigos)  # Los amigos directos de esta persona

        # Recorremos cada amigo directo
        for amigo in amigos_directos:
            # Recorremos los amigos del amigo (amigos en común)
            for amigo_comun in amigo.amigos:
                # Si el amigo en común no es la persona actual y no es un amigo directo
                if amigo_comun != nodo and amigo_comun not in amigos_directos:
                    recomendados.add(amigo_comun)
        
        # Almacenamos los recomendados para la persona actual
        recomendaciones[nodo.id] = list(recomendados)

    return recomendaciones


### pregunta 003
def most_popular_friend(grafo):
    popular = None
    max_amigos = 0

    for nodo in grafo.listaNodos.values(): #recorriendo por cada diccionrio a través de sus valores
        num_amigos = len(nodo.get_friends())
        if num_amigos > max_amigos:
            max_amigos = num_amigos
            popular = nodo

    if popular:
        return popular.nombre, max_amigos
    else:
        return None, 0  # Si no hay nodos en el grafo

### pregunta 004 

def shortest_path(grafo, person1_id, person2_id):
    # Verificar si ambos nodos existen en el grafo
    if person1_id not in grafo.listaNodos or person2_id not in grafo.listaNodos:
        return None

    visitados = set()
    cola = deque([(grafo.listaNodos[person1_id], [grafo.listaNodos[person1_id]])])  # Nodo actual y camino recorrido

    while cola:
        actual, camino = cola.popleft()  # Nodo actual y el camino correspondiente

        # Retornar camino si llegamos al nodo objetivo
        if actual.id == person2_id:
            lista = []
            recorrido = "RECORRIDO : "
            for nodo in camino:
                lista.append(nodo.nombre)
                if nodo.nombre == camino[-1].nombre:
                    recorrido += f"{nodo.nombre}"
                else:
                    recorrido += f"{nodo.nombre} -> "
            print(recorrido)
            return lista

        visitados.add(actual)

        # Explorar amigos no visitados
        for amigo in actual.amigos:
            if amigo not in visitados:
                cola.append((amigo, camino + [amigo]))  # Agregar el amigo y el camino actualizado

    # Si no hay camino, retornar None
    return None
