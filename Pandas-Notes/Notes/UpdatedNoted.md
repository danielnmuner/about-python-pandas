## Transformacion de Datos con Numpy y Pandas
### NumPy
  - [x] [Numpy Array](#numpy-array)

### Numpy Array
Las operaciones en Numpy son hasta 50 veces mas rapidas que en Python,  a continuacion se presenta la creacion de arrays de diferetes dimenciones.

```python
lista = [1,2,3,4,5,10]
array_lista = np.array(lista)
matriz = [[1,2,3],[2,3,4],[23,43,1]]
array_matriz = np.array(matriz)

#Output
Array List <class 'numpy.ndarray'>
Array Matrix <class 'numpy.ndarray'>
```
Si hacemos slicing de matrices simpre colocamos `(nrow:mrow,ncol:ncol)` para 
```python
matriz = [[1,2,3],[2,3,4],[23,43,1]]
array_matriz[-2:,0]
#Outuput
array([2,23])
```
