# main.py
from Grafo import Grafo
from preguntas import *
from conectNeo4j import obtener_grafo_desde_neo4j

def llenarGrafo():
    grafo = Grafo()
    # Grupo 1
    grafo.agregar_persona(1, 'Alice')
    grafo.agregar_persona(2, 'Bob')
    grafo.agregar_persona(3, 'Charlie')
    grafo.agregar_persona(4, 'David')
    grafo.agregar_persona(5, 'Eva')
    grafo.agregar_persona(6, 'Frank')

    # Conexiones del Grupo 1
    grafo.agregar_amistad(1, 2)  # Alice - Bob
    grafo.agregar_amistad(1, 3)  # Alice - Charlie
    grafo.agregar_amistad(2, 3)  # Bob - Charlie
    grafo.agregar_amistad(2, 4)  # Bob - David
    grafo.agregar_amistad(3, 4)  # Charlie - David
    grafo.agregar_amistad(3, 5)  # Charlie - Eva
    grafo.agregar_amistad(4, 5)  # David - Eva
    grafo.agregar_amistad(5, 6)  # Eva - Frank
    grafo.agregar_amistad(1, 5)  # Alice - Eva
    grafo.agregar_amistad(4, 6)  # David - Frank

    # Grupo 2
    grafo.agregar_persona(7, 'Grace')
    grafo.agregar_persona(8, 'Hannah')
    grafo.agregar_persona(9, 'Ian')
    grafo.agregar_persona(10, 'Jack')
    grafo.agregar_persona(11, 'Kate')
    grafo.agregar_persona(12, 'Liam')

    
    grafo.agregar_amistad(8, 9)  # Hannah - Ian
    grafo.agregar_amistad(8, 10) # Hannah - Jack
    grafo.agregar_amistad(9, 10) # Ian - Jack
    grafo.agregar_amistad(9, 11) # Ian - Kate
    grafo.agregar_amistad(10, 11) # Jack - Kate
    grafo.agregar_amistad(10, 12) # Jack - Liam
    grafo.agregar_amistad(11, 12) # Kate - Liam
    grafo.agregar_amistad(7, 11)  # Grace - Kate

    # Grupo 3
    grafo.agregar_persona(13, 'Mia')
    grafo.agregar_persona(14, 'Noah')
    grafo.agregar_persona(15, 'Olivia')
    grafo.agregar_persona(16, 'Parker')
    grafo.agregar_persona(17, 'Quinn')
    grafo.agregar_persona(18, 'Ryan')

    # Conexiones del Grupo 3
    grafo.agregar_amistad(11, 13) # Kate - Mia
    grafo.agregar_amistad(11, 13) # Kate - Mia
    grafo.agregar_amistad(13, 14) # Mia - Noah
    grafo.agregar_amistad(13, 15) # Mia - Olivia
    grafo.agregar_amistad(14, 15) # Noah - Olivia
    grafo.agregar_amistad(14, 16) # Noah - Parker
    grafo.agregar_amistad(15, 16) # Olivia - Parker
    grafo.agregar_amistad(15, 17) # Olivia - Quinn
    grafo.agregar_amistad(16, 17) # Parker - Quinn
    grafo.agregar_amistad(16, 18) # Parker - Ryan
    grafo.agregar_amistad(17, 18) # Quinn - Ryan
    grafo.agregar_amistad(13, 17) # Mia - Quinn





    # Conexiones del Grupo 2
    grafo.agregar_amistad(12, 12)  # Grace - Hannah
    grafo.agregar_amistad(7, 9)  # Grace - Ian


    return grafo

def main():
    grafo = llenarGrafo()
    


    grafo.show()

    #pregunta 001
    print("Número de grupos por BFS : ", find_friend_groups_bfs(grafo))
    print("Número de grupos por DFS : ", find_friend_groups_dfs(grafo))

    #pregunta 004
    print(shortest_path(grafo, grafo.listaNodos[1].id,grafo.listaNodos[5].id))

    #obtener_grafo_desde_neo4j().graficar_grafo()
    grafo.graficar_grafo()
    

if __name__ == "__main__":
    main()
