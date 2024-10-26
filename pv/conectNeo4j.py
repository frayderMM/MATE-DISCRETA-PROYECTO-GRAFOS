from neo4j import GraphDatabase
from Nodo import Nodo
from Grafo import Grafo

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def run_query(self, query):
        with self._driver.session() as session:
            result = session.run(query)
            return [record for record in result]

# Función para obtener un Grafo poblado desde Neo4j
def obtener_grafo_desde_neo4j():
    # Crear la conexión a Neo4j
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "123456789"

    conn = Neo4jConnection(uri, user, password)
    # Crear una instancia de Grafo
    grafo = Grafo()
    # Crear una instancia de Grafo
    grafo = Grafo()

    # 1. Obtener los nodos (personas)
    query_personas = "MATCH (p:Persona) RETURN p.id AS id, p.nombre AS nombre"
    personas = conn.run_query(query_personas)
    
    # Agregar cada persona como un nodo en el grafo
    for record in personas:
        grafo.agregar_persona(record['id'], record['nombre'])

    # 2. Obtener las amistades (relaciones)
    query_amistades = "MATCH (p1:Persona)-[:AMIGO_DE]-(p2:Persona) RETURN p1.id AS id1, p2.id AS id2"
    amistades = conn.run_query(query_amistades)
    
    # Agregar cada amistad como una conexión entre dos nodos en el grafo
    for record in amistades:
        grafo.agregar_amistad(record['id1'], record['id2'])

    # Cerrar la conexión a Neo4j
    conn.close()

    # Retornar el grafo poblado
    return grafo



