## Transformacion de Datos con Numpy y Pandas
### NumPy
  - [x] [Numpy Array](#numpy-array)

### Numpy Array
El array es el principal objeto de la librería. Representa datos de manera estructurada y se puede acceder a ellos a traves del indexado, a un dato específico o un grupo de muchos datos específicos. Las operaciones en Numpy son hasta 50 veces mas rapidas que en Python,  a continuacion se presenta la creacion de arrays de diferetes dimenciones.


```python
lista = [1,2,3,4,5,10]
array_lista = np.array(lista)
matriz = [[1,2,3],[2,3,4],[23,43,1]]
array_matriz = np.array(matriz)

#Output
Array List <class 'numpy.ndarray'>
Array Matrix <class 'numpy.ndarray'>
```
Si hacemos slicing de matrices simpre colocamos `(nrow:mrow,ncol:ncol)` E.g.:
```python
matriz = [[1,2,3],[2,3,4],[23,43,1]]
array_matriz[-2:,0]

#Outuput
array([2,23])

```
Si el slicing se realiza sobre un a matriz de 3 dimenciones el orden es diferente como se muestra a continuacion.
```python
#Creamos x = 2 rows, y = 4 cols, z = 2
a_3d_array = np.array([[[1,2,3,4],[2,3,4,5]],[[43,21,56,7],[2,1,3,5]]])

#Slicing a_3d_array
#a_3d_array[0] ->[[1,2,3,4],[2,3,4,5]] Profundidad o Eje Z
#a_3d_array[0,1] -> [2,3,4,5] Altura Eje Y
#a_3d_array[0,1,3] -> 5 Ancho Eje X

a_3d_array[0:,0:,2:]
# 1. Tomar ambas matrices de 2X4 Eje Z
# 2. Tomar tanto rows como cols de ambas matrices Eje Z
# 3. Tomar de la col3 a col4 de ambas matrices Eje X

#Output
array([[[ 3,  4],
        [ 4,  5]],

       [[56,  7],
        [ 3,  5]]])
```
