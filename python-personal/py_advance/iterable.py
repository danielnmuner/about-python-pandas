# # Creando un iterador

# my_list = [1,2,3,4,5]
# my_iter = iter(my_list)

# # Iterando un iterador

# print(next(my_iter))

# # Cuando no quedan datos, la excepción StopIteration es elevada

# # Creando un iterador

# my_list = [1,2,3,4,5]
# my_iter = iter(my_list)

# # Iterando un iterador

# while True: #ciclo infinito
#   try:
#     element = next(my_iter)
#     print(element)
#   except StopIteration:
#     break

# class EvenNumbers:
#   """Clase que implementa un iterador de todos los números pares,
#   o los números pares hasta un máximo
#   """

#   #* Constructor de la clase
#   def __init__(self, max = None): #self hace referencia al objeto futuro que voy a crear con esta clase
#     self.max = max


#   # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
#   def __iter__(self):
#     self.num = 0 #Primer número par
#     #* Convertir un iterable en un iterador
#     return self

#   # Método para tener la función "next" de Python
#   def __next__(self):
#     if not self.max or self.num <= self.max:
#       result = self.num
#       self.num += 2
#       return result
#     else:
#       raise StopIteration

# # Ventajas de usar iteradores:

# # Nos ahorra recursos.
# # Ocupan poca memoria.

#----------------------------------------------------------
#Import Time permite introducir un delay durante la ejecucion del codigo
import time

#Nombre de la Clase
class FiboIter():

#Metodo Dunder Iterador convierte un iterable en un iterador
#Inicializad n1 y n2
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

#Metodo Dunder next, permite avanzar al siguiente elemento del iterador
#Counter == 0 posicion cero self.counter += 1
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1

#Counter == 1 posicion uno self.counter += 1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
#Si ya esta en la posicion dos ya puede ejecutar los otros numeros
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
#Swaping consite en asignar varibles de forma cruzada en una sola linea
            self.n1, self.n2 = self.n2, self.aux
#Conter sigue avanzando y el return es return self.aux
            self.counter += 1
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()
    # fibonacci es practicamente igual a return self.aux
    for element in fibonacci:
        print(element)
    #time.sleep genera un delay en segundos
        time.sleep(1)