from graph import Graph
from collections import deque
class SocialNetwork:
    def __init__(self):
        self.graph = Graph()

    # Agregar una relación de amistad (arista)
    def add_friendship(self, person1_id, person2_id):
        self.graph.add_friendship(person1_id, person2_id)

    # Función para encontrar grupos de amigos (componentes conectados)
    def find_friend_groups(self, use_dfs=True):
        visited = {person.id: False for person in self.graph.get_all_people()}
        friend_groups = 0
        
        # Función para realizar DFS
        def dfs(person):
            stack = [person]
            while stack:
                current = stack.pop()
                if not visited[current.id]:
                    visited[current.id] = True
                    for friend in current.get_friends():
                        if not visited[friend.id]:
                            stack.append(friend)

        # Función para realizar BFS
        def bfs(person):
            from collections import deque
            queue = deque([person])
            visited[person.id] = True
            while queue:
                current = queue.popleft()
                for friend in current.get_friends():
                    if not visited[friend.id]:
                        visited[friend.id] = True
                        queue.append(friend)

        # Recorremos todas las personas del grafo
        for person in self.graph.get_all_people():
            if not visited[person.id]:
                # Elegir entre DFS o BFS según el parámetro `use_dfs`
                if use_dfs:
                    dfs(person)
                else:
                    bfs(person)
                friend_groups += 1  # Cada vez que entramos a este bloque, encontramos un nuevo grupo
        
        return friend_groups
    
    # Método para recomendar amigos a cada persona
    def recommend_friends(self):
        recommendations = {}
        
        # Para cada persona en el grafo
        for person in self.graph.get_all_people():
            recommended = set()
            friends = set(person.get_friends())
            
            # Recorremos los amigos directos de la persona
            for friend in friends:
                friends_of_friend = set(friend.get_friends())
                
                # Añadir amigos de amigos que no sean amigos directos ni la misma persona
                for fof in friends_of_friend:
                    if fof != person and fof not in friends:
                        recommended.add(fof.id)
            
            # Convertimos el conjunto a lista y guardamos las recomendaciones
            recommendations[person.id] = list(recommended)
        
        return recommendations
    # Método para encontrar a la persona con más amigos (nodo con el grado más alto)
    def most_popular_friend(self):
        max_friends = -1
        most_popular = None

        # Recorremos todas las personas en el grafo
        for person in self.graph.get_all_people():
            num_friends = len(person.get_friends())  # Número de amigos de esta persona
            if num_friends > max_friends:
                max_friends = num_friends
                most_popular = person
        
        # Devolvemos el nombre de la persona más popular y la cantidad de amigos
        return (most_popular.id, max_friends) if most_popular else (None, 0)

    # Método para encontrar el camino más corto entre dos personas usando BFS
    def shortest_path(self, person1_id, person2_id):
        if person1_id not in self.graph.nodes or person2_id not in self.graph.nodes:
            return None  # Si alguna persona no existe en el grafo
        
        # BFS para encontrar el camino más corto
        queue = deque([[person1_id]])  # Cola que guarda caminos
        visited = set()  # Conjunto de personas visitadas
        
        while queue:
            path = queue.popleft()  # Extraemos el camino más antiguo
            current_person = path[-1]  # Última persona en el camino

            if current_person == person2_id:
                return path  # Si hemos llegado a la persona objetivo, devolvemos el camino

            if current_person not in visited:
                visited.add(current_person)
                
                # Recorremos los amigos de la persona actual
                for friend in self.graph.get_person(current_person).get_friends():
                    if friend.id not in visited:
                        new_path = list(path)  # Creamos un nuevo camino basado en el actual
                        new_path.append(friend.id)
                        queue.append(new_path)  # Añadimos el nuevo camino a la cola
        
        return None  # Si no se encuentra un camino
    # Método para detectar ciclos en el grafo usando DFS
    def has_cycle(self):
        visited = set()

        # Función auxiliar para realizar DFS y detectar ciclos
        def dfs(current, parent):
            visited.add(current)

            # Recorremos los amigos (vecinos) del nodo actual
            for neighbor in self.graph.get_person(current).get_friends():
                # Si el vecino no ha sido visitado, realizamos DFS sobre él
                if neighbor.id not in visited:
                    if dfs(neighbor.id, current):
                        return True
                # Si el vecino ya fue visitado y no es el padre del nodo actual, hay un ciclo
                elif neighbor.id != parent:
                    return True
            
            return False

        # Recorremos todos los nodos del grafo para asegurarnos de que no haya ciclos en componentes no visitados
        for person in self.graph.get_all_people():
            if person.id not in visited:
                if dfs(person.id, None):
                    return True
        
        return False
    


# Ejemplo de uso:
if __name__ == "__main__":
    social_network = SocialNetwork()
    social_network.add_friendship(0, 1)
    social_network.add_friendship(0, 2)
    social_network.add_friendship(1, 3)
    social_network.add_friendship(2, 4)
    social_network.add_friendship(3, 4)
    social_network.add_friendship(4, 5)

    #grupo 2
    social_network.add_friendship(6, 7)
    social_network.add_friendship(7, 8)
    social_network.add_friendship(8, 6)
    social_network.add_friendship(7, 10)

    #grupo 3
    social_network.add_friendship(12, 13)
    social_network.add_friendship(13, 14)
    social_network.add_friendship(14, 15)
    social_network.add_friendship(12, 15)


    

    # Encontrar grupos de amigos usando DFS
    print("Número de grupos de amigos (DFS):", social_network.find_friend_groups(use_dfs=True))

    # Encontrar grupos de amigos usando BFS
    print("Número de grupos de amigos (BFS):", social_network.find_friend_groups(use_dfs=False))


    # Obtener recomendaciones de amigos
    recommendations = social_network.recommend_friends()
    print("Recomendaciones de amigos:", recommendations)


    # Encontrar la persona con más amigos
    most_popular, num_friends = social_network.most_popular_friend()
    print(f"La persona con más amigos es: {most_popular} con {num_friends} amigos.")


    # Encontrar el camino más corto entre dos personas
    path = social_network.shortest_path(0, 5)
    if path:
        print(f"El camino más corto entre 0 y 5 es: {path}")
    else:
        print("No existe un camino entre 0 y 5.")


    # Verificar si hay un ciclo ##TODO
    has_cycle = social_network.has_cycle()
    print(f"¿La red social tiene ciclos?: {'Sí' if has_cycle else 'No'}")

