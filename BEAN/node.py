class Node:
    def __init__(self, id):
        self.id = id  # Identificador del nodo (persona)
        self.friends = []  # Lista de amigos (otros nodos)

    # Método para agregar un amigo (nodo) a la lista de amigos
    def add_friend(self, friend_node):
        if friend_node not in self.friends:
            self.friends.append(friend_node)

    # Método para obtener los amigos de este nodo
    def get_friends(self):
        return self.friends

    # Representación del nodo para facilitar la impresión
    def __repr__(self):
        return f'Node({self.id})'
