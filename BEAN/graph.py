from node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    # Método para agregar una persona (nodo) al grafo
    def add_person(self, person_id):
        if person_id not in self.nodes:
            self.nodes[person_id] = Node(person_id)

    # Método para agregar una relación de amistad entre dos personas
    def add_friendship(self, person1_id, person2_id):
        self.add_person(person1_id)
        self.add_person(person2_id)
        person1 = self.nodes[person1_id]
        person2 = self.nodes[person2_id]
        person1.add_friend(person2)
        person2.add_friend(person1)

    # Método para obtener un nodo (persona) por su ID
    def get_person(self, person_id):
        return self.nodes.get(person_id)

    # Método para obtener todos los nodos
    def get_all_people(self):
        return self.nodes.values()
