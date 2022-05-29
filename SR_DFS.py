from queue import Queue
'''Importa la libreria Queue'''
class Grafo:
    '''Clase grafo-Representa a un grafo aplicando búsqueda en profundidad
    Atributos:
    numero_de_nodos:número de nodos
    dirigido:si es dirigido o no dirigido
    Métodos:
    __init__(self, num_de_nodos, dirigido=True)
        Método constructor que inicializa la clase grafo
    agregar_borde(self, nodo1, nodo2, peso=1)
        Genera los bordes de la lista de adyacencia.
    Imprimir_lista_adyacencia(self)
        Método que imprime el grafo generado en la lista de adyacencia
    dfs(self, inicio, objetivo, camino = [], visitado = set())
        Método de búsqueda que imprime el recorrido por dfs
    Excepciones:
    Evalua --Si (__name__ == "__main__")
    Crea una instancia de la clase Grafo  
    Donde el grafo es no dirigido y tiene cinco nodos
    Agrega los bordes al grafo donde el peso=1
    Imprime la lista de adyacencia en lo forma nodo n: {(nodo, peso)}
    '''
    def __init__(self, numero_de_nodos, dirigido = True):
        '''Método constructor inicializador de la clase Grafo
        Parámetros:
        m_numero_de_nodos--- el número de nodos. Tipo de dato int
        m_nodos--- rango de nodos. Tipo de dato int
        m_dirigido--- dirigido o no dirigido (por defecto en verdadero). Dato de tipo boleano
        m_lista_adyacencia--- Lista de adyacencia (Uso de un diccionario para implementar una lista de adyacencia)
        '''
        self.m_numero_de_nodos = numero_de_nodos
        self.m_nodos = range(self.m_numero_de_nodos)
        self.m_dirigido = dirigido
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
    def agregar_borde(self, nodo1, nodo2, peso=1):
        '''Método para agregar bordes al grafo 
        Parámetros:
        nodo1: Tipo de dato int
        nodo2:Tipo de dato int
        peso(1): Tipo de dato int
        --Agrega nodo2 y el peso a lista de adyacencia en nodo1
        Excepciones
        Evalua: Si (es NO dirigido)
            Agrega nodo1 y el peso a lista de adyacencia en nodo2
        '''
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        if not self.m_dirigido:
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
    def imprimir_lista_adyacente(self):
        '''Método para imprimir el grafo generado en la lista de adyacencia
        Excepciones:
        Recorre por la lista de adyacencia
            Imprime el nodo
        '''
        for llave in self.m_lista_adyacencia.keys():
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])
    def dfs(self, inicio, objetivo, camino = [], visitado = set()):
        '''Método de búsqueda que imprime el recorrido por dfs
        Párametros:
        inicio: int
        objetivo: int
        camino: lista
        visitado: int
        Excepciones:
        Evalua-- Si(inicio==objetivo)
            retorna camino
            Recorre vecino y peso en la lista de adyacencia
                Evalua-- Si(vecino no esta en visitado)
                    Asignamos a resultado que es igual a (vecino, objetivo, camino, visitado)
                    Evalua-- Si (resultado is not None) -> Si el resultadon o hasido encontrado
                        devuelve el resultado
        apila camino
        retorna None
        '''
        camino.append(inicio)
        visitado.add(inicio)
        if inicio == objetivo:
            return camino
        for (vecino, peso) in self.m_lista_adyacencia[inicio]:
            if vecino not in visitado:
                resultado = self.dfs(vecino, objetivo, camino, visitado)
                if resultado is not None:
                    return resultado
        camino.pop()
        return None
if __name__ == "__main__":
    g = Grafo(5, dirigido=False)

    g.agregar_borde(0, 1)
    g.agregar_borde(0, 2)
    g.agregar_borde(1, 3)
    g.agregar_borde(2, 3)
    g.agregar_borde(3, 4)
    
    g.imprimir_lista_adyacente()

    camino_transversal = []
    camino_transversal = g.dfs(0, 3)
    print(f"El camino transversal del nodo 0 a el nodo 3 is: {camino_transversal}")