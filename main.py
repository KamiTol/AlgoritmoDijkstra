import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph} # Creación de Diccionario con nodos y distancias.
    predecessors = {node: None for node in graph} # Creación de Diccionario con nodos y predecesores.
    distances[start] = 0 # Distancia del nodo inicial es 0.
    queue = [(0, start)] # Cola de prioridad con la distancia y el nodo inicial.

    while queue:
        current_distance, current_node = heapq.heappop(queue) # Extraemos el nodo con la menor distancia.

        # Si la distancia actual es menor a la distancia extraída, continua.
        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node].items(): # Recorremos los vecinos del nodo actual.
            distance = current_distance + weight # Calculamos la distancia acumulada.

            if distance < distances[neighbor]: # Si la distancia acumulada es menor a la distancia almacenada.
                distances[neighbor] = distance # Actualizamos la distancia.
                predecessors[neighbor] = current_node # Actualizamos el predecesor.
                heapq.heappush(queue, (distance, neighbor)) # Agregamos a la cola de prioridad.

    return distances, predecessors

def get_path(predecessors, start, end): # Función para obtener el camino
    path = [] # Lista para almacenar el camino.
    current_node = end # Nodo actual es el nodo final.

    while current_node is not None:
        path.append(current_node) # Agregamos el nodo actual a la lista.
        current_node = predecessors[current_node] # Actualizamos el nodo actual.

    path.reverse()  # Invertimos la lista.

    return path

if __name__ == "__main__":

    graph = {
        'A': {'B': 10, 'C': 8, 'D': 15},  # A -> B: 10, A -> C: 8, A -> D: 15
        'B': {'A': 10, 'E': 15},  # B -> A: 10, B -> E: 15
        'C': {'A': 8, 'J': 14, 'G': 15},  # C -> A: 8, C -> J: 14, C -> G: 15
        'D': {'A': 15, 'G': 6, 'I': 15},  # D -> A: 15, D -> G: 6, D -> I: 15
        'E': {'B': 15, 'J': 8, 'H': 30},  # E -> B: 15, E -> J: 8, E -> H: 30
        'F': {'G': 8, 'L': 15, 'J': 9},  # F -> G: 8, F -> L: 15, F -> J: 9
        'G': {'D': 6, 'I': 7, 'C': 15, 'F': 8},  # G -> D: 6, G -> I: 7, G -> C: 15, G -> F: 8
        'H': {'E': 30, 'J': 18, 'L': 15},  # H -> E: 30, H -> J: 18, H -> L: 15
        'I': {'D': 15, 'G': 7, 'K': 10},  # I -> D: 15, I -> G: 7, I -> K: 10
        'J': {'C': 14, 'F': 9, 'H': 18, 'E': 8},  # J -> C: 14, J -> F: 9, J -> H: 18, J -> E: 8
        'K': {'I': 10, 'L': 10},  # K -> I: 10, K -> L: 10
        'L': {'F': 15, 'H': 15, 'K': 10}  # L -> F: 15, L -> H: 15, L -> K: 10
    }

    while True:
        start_node = input("Enter the start node: ")
        end_node = input("Enter the end node: ")

        distances, predecessors = dijkstra(graph, start_node) # Llamamos a la función dijkstra, pasando el grafo y el nodo inicial.
        path = get_path(predecessors, start_node, end_node) # Llamamos a la función get_path, pasando los predecesores, el nodo inicial y el nodo final.
        total_weight = distances[end_node] # Obtenemos el peso total.

        print(f"Path: {path}") # Imprimimos el camino.
        print(f"Total weight: {total_weight}") # Imprimimos el peso total.

        continue_program = input("Continuar? (y/n): ") # Preguntamos si desea continuar.
        if continue_program.lower() != "y":
            break
