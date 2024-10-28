from Producto import Producto
from Nodo import Nodo
from Grafo import Grafo
from preguntas import *

def main():
    # Crear productos de ejemplo
    producto1 = Producto(1, "Leche", 1.5)
    producto2 = Producto(2, "Pan", 0.5)
    producto3 = Producto(3, "Huevos", 2.0)
    producto4 = Producto(4, "Queso", 3.0)
    producto5 = Producto(5, "Mantequilla", 2.5)

    # Crear grafo
    grafo = Grafo()

    # Ejemplo de uso
    # transactions = [
    #     {"arroz", "huevo", "pan","detergente"},
    #     {"huevo", "pan","mantequilla","aceite"},
    #     {"detergente", "pan","mantequilla","azucar"},
    #     {"leche", "queso","carne"},
    #     {"arroz","huevo"},
    #     {"aceite","mantequilla"},
    #     {"leche","carne","avena"},
    #     {"avena","carne"},
    #     {"leche", "queso","yogurt"}
    # ]
    transactions = [
        {"arroz", "huevo", "pan","detergente"},
        {"arroz", "pan","detergente"},
        {"mantequilla","huevo", "pan"}

    ]


    # pregunta 006
    A = frequent_itemsets(transactions,2)
    
    
    index = 0
    for i in A:
        index += 1
        print(f"Conjunto {index}: "+'{  ',end="")
        for j in i:
            print(j,end="   ")
        print("}")


    # pregunta 007
    build_cooccurrence_graph(transactions,2).graficar_grafo()


    # pregunta 008
    R = find_communities(build_cooccurrence_graph(transactions,2))
    for i in R:
        print("grupo:",end=" ")
        for j in i:
            print(j,end="  ")
        print("")

    
    

if __name__ == "__main__":
    main()
