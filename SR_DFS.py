from queue import Queue
'''Importa la libreria Queue'''
class Grafo:
    '''Clase grafo-Representa a un grafo aplicando búsqueda en profundidad
    Atributos:
    numero_de_nodos:número de nodos
    dirigido:si es dirigido o no dirigido
    Excepciones:
    Evalua --Si (__name__ == "__main__")
    '''
    def __init__(self, numero_de_nodos, dirigido = True):
        '''Método constructor inicializador de la clase Grafo
        Parámetros:
        m_numero_de_nodos--- el número de nodos
        m_nodos--- rango de nodos
        m_dirigido--- dirigido o no dirigido (por defecto en verdadero). Dato de tipo boleano
        m_lista_adyacencia--- Lista de adyacencia (Uso de un diccionario para implementar una lista de adyacencia)
        '''
        self.m_numero_de_nodos = numero_de_nodos
        self.m_nodos = range(self.m_numero_de_nodos)
        self.m_dirigido = dirigido
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}