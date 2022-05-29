# Breadth First Search - BFS

'''
    Bryan Alfredo Solórzano Montero
'''

from queue import Queue# Importación de libreria para usar la estructura FIFO (permite almacenar nodos)

'''
    Grafo:
        Una clase para implementar una búsqueda BFS, la cual representara gráficas.
        Con la ayuda de matrices de adyacencia.  
'''

class Grafo: # Clase para aplciar los grafos
    ''' 
    Constructor
    Veamos los atributos necesarios para el objeto Grafo

    Parametros 
    ----------
        g_numeros_nodos: number
            Precisa el tamaño de los nodos
        g_dirigido: boolean
            El que dara dirección - # Es necesario saber si sera diriguido o no
    
    Atributos
    ---------
        g_nodos:  number
            Para que el nado este en un rango permitido
        self.g_adjuntar_lista: Dictionaries
            De cierta forma se hara una representación grafica, por lo que necesitara implmentar matrices de adyacencia
            Par aesta actividad queda perfecto implementar una variable diccionario
            Se encuentra seteando (set()) a cada nodo, es posible gracias al ciclo for y esa caracteristica de código
    '''

    def __init__(self, numero_nodos, dirigido=True):
        # Atributos
        self.g_numeros_nodos = numero_nodos 
        self.g_nodos = range(self.g_numeros_nodos) 
        self.g_dirigido = dirigido 

        self.g_adjuntar_lista = {nodo: set() for nodo in self.g_nodos} 

    '''
    A pesar de que ningun metodo retorna algo en concreto, si modifica y trabajo con los atributos de la clase
    Ojo: cada linea de ocmentado est amuy ligado a cada linea de codigo. Es deicr existe un efoque directo.
    Importante: self -> Solo hace referencia a la propia clase

    Metodos
    -------
        agregar_borde(self, nodo1, nodo2, peso=1): 
            Objetivo
            --------
                Añadir una arista al gráfico
            
            Parametros
            ----------
                La forma de representar un grafico es por medio de una lista de aristas
                Una arista = [nodo1, nodo2, peso]

                nodo1: number
                    Este vendria hacer un vertice de partida

                nodo2: number
                    Este vendria hacer un vertice de llegada
                    
                peso : number
                    Se podria el grado de dificaltad al pasar por aquí, si esta bajo sera mas facil pasarlo
                    Ojo: Es un dato opciocal y por lo tanto es que se le pone un valor por defecto
            
            Descripción
            -----------
                Busca el nodo y le grego otro nodo hijo, con un nivel
                Si la dirección es falsa, entrara para adjuntar un nuevo nodo a la lista
                A diferencia de arriba los nodos cambian de posición nada más
        
        imprimir_adjuntar_lista(self): Hace referencia a la propia clase
            Objetivo
            --------
            Permitir observar el grafo, haicendo recorrido a esa lista de nodos

            Descripción
            -----------
            Por iteración se obtendra el nombre de cada clave
            Usando el nombre hacemos entrada al diccionario para obtener su valor y poder imprimirlo

        busqueda_amplitud(self, inicio_nodo): La busqueda por achura tienen que tener un nod de inicio
            Onjetivo
            -----------
            Para ir juntando los nodos ya vivistados y evitar bucles

            Parametros
            ----------
            self: number 
                Para decir de que nodo comenzaremos a buscar

            inicio_nodo: number
                El nodo al cual queremos buscar

            Avariables
            ----------
            visitado:  cola
                Nos permitira crerar un conjunto de elementos unicos

            queue: lista
                El modo mas estandar para trabajar con nodos de una manera segura

            Descripción
            -----------
            inicio_nodo sera añadido a la cola y en la lista de visitados
                Asignación de ese parametro a los arreglos conjuntos de nuestras varaibles visitado y queue
            
            Mietras no este vacia la lista, siga haciendo la busqueda --> nos ira dando el nodo actual
                Un ciclo for para ir mostrando el nodo actual, mientras la lista no este vacia
                Aquí se procesa el tema del encolamiento y visita por los nodos
    '''

    # Agregar un nodo
    def agregar_borde(self, nodo1, nodo2, peso=1):
        self.g_adjuntar_lista[nodo1].add((nodo2, peso)) 
        if not self.g_dirigido: 
            self.g_adjuntar_lista[nodo2].add((nodo1, peso)) 
    
    # Imprimir lista de nodos
    def imprimir_adjuntar_lista(self): 
        for clave in self.g_adjuntar_lista.keys(): # 
            print(f'nodo{clave}: {self.g_adjuntar_lista[clave]}') 

    # Busqueda por anchura
    def busqueda_amplitud(self, inicio_nodo): 
        visitado = set()
        queue = Queue() 

        # inicio_nodo sera añadido a la cola y en la lista de visitados
        queue.put(inicio_nodo) # A la cola
        visitado.add(inicio_nodo) # A la lista

        # Mietras no este vacia la lista, siga haciendo la busqueda --> nos ira dando el nodo actual
        while not queue.empty():
            actual_nodo = queue.get() # Poner en cola el nodo actual
            print(actual_nodo, end = " ") # Imprimir el nodo de cola
            for (siguiente_nodo, peso) in self.g_adjuntar_lista[actual_nodo]: # Obtener los vertices de eso nodo
                if siguiente_nodo not in visitado: # Para saber si ha sido visitado (ese not, es como hacer la negación para llegar a manejar datos booleanos)
                    queue.put(siguiente_nodo) # Inmediatamente es encolado
                    visitado.add(siguiente_nodo) # Si entra es que no ha sido visitado y ahora ya esta identificado

'''
    Conidcional __name__ == "__main___"

    Descripción
    -----------
        Bloque de codigo considerado como el programa principal, aquí hace llamdo de modulo sde codigo para ejecutarlos

    Objetivos
    ---------
        Intanciar un objeto: Grafo
            A esa instancia de la clase Grafo se le debera agregar sus respectivos bordes
        
        Agregación de los nodos para representar al Grafo
            La cantidad de bordes dependera del numero de nodos que estipulamos en su instancia

        Imprimir los nodos para ver el grafo en forma de matrices
            Como se dijo que se tratara de graficar tipo matrices, pues se implementa la función que nos imprimir la lista de todos esos nodos

        Realización de una busqueda
            Lo que se hara con el llamado de esta función sera buscar un nodo1 a partir de un nodo#
            Debido a que es una función de busqueda necesitara devolver el resultado de la busqueda

'''

if __name__ == "__main__": 
    
    g = Grafo(6, dirigido=False) # Instanicar un objeto

    g.agregar_borde(0, 1)
    g.agregar_borde(0, 2)
    g.agregar_borde(1, 2)
    g.agregar_borde(1, 4)
    g.agregar_borde(2, 3)
    g.agregar_borde(2, 4)

    g.imprimir_adjuntar_lista() 

    print ("Lo siguiente es el primer recorrido de ancho (empezando por el vértice 0)")

    g.busqueda_amplitud(0, 0) 
    print()

''' Finalización del Algoritmo'''