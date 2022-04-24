## Transformacion de Datos con Numpy y Pandas
### NumPy

  - [x] [Numpy Array](#numpy-array)
  - [x] [Tipos de datos](#tipos-de-datos)
  - [x] [Dimensiones](#dimensiones)
  - [x] [Creando arrays](creando-arrays)

### Numpy Array
[Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html#what-is-an-array)  

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
### Tipos de datos  
[Lista Tipos de Datos](https://numpy.org/doc/stable/user/basics.types.html)  

Los arrays de NumPy solo pueden contener un tipo de dato, ya que esto es lo que le confiere las ventajas de la optimización de memoria. Manipulacion de `tipos de datos` en Numpy:
```python
# Array con dtype para definir el tipo de dato
arr = np.array([0,1,2,4,5], dtype = "float64")
# Astype es una alternativa cuando el array ya ha sido creado.

arr = arr.astype(np.float64) #Output: array([0., 1., 2., 4., 5.])
arr = arr.astype(np.bool_) #Output: array([False,  True,  True,  True,  True])
arr = arr.astype(np.string_) #Output: array([b'0.0', b'1.0', b'2.0', b'4.0', b'5.0'], dtype='|S32')
```

### Dimensiones
**Tipos de Dimenciones**
![image](https://user-images.githubusercontent.com/60556632/164954432-a1f245d9-f189-4164-be1b-9233fbe5410a.png)

| Tensor 3 Dimenciones en Series de Tiempo |
| --- |
| ![image](https://user-images.githubusercontent.com/60556632/164954538-6b5ba6f2-a6c1-4ceb-81c4-462da7ee2132.png)
| **Tensor 4 Dimenciones Imagenes** |
| ![image](https://user-images.githubusercontent.com/60556632/164954563-d3e90480-e262-4157-94e5-e512f7759b11.png) | 
| **Alto:** Alto de la Imagen,  **Ancho:** Ancho de la Imagen, **Ejemplos:** Cada una de las Imagenes, **Canales:** Composición de Color de Cada Imagen (Grises,RGB, etc) |  

 A traves del comando `.ndim` podremos saber en Numpy con que dimensiones estamos trabajando. El argumento `ndmin` dentro de array establece la cantidad de dimensiones minimas que debe tener nuestro array: `np.array([1,2,3], ndmin=3)` al momento de crearlo `#Output: [[[1,2,3]]]` asi no las tenga.  
 
 Una alternativa mas completa a `ndmin` es la funcion `np.expand_dims(np.array([1,2,3]), axis=0 )` en la cual ademas de expandir la dimension podemos indicar el Eje a expandir. Para eliminar, comprimir o reducir dimensiones donde no hay datos usamos `np.squeeze([[[1,2,3]]])` Output: `[1,2,3]`.  
 
 
 ### Creando arrays
 - **Rangos**
Podemos crear arrays en python con `range(start,stop,steps)` como se muestra a continuacion:
```python
range(0,10) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Igualmente lo podemos hacer con Numpy np.arange(start,stop,steps: 

np.arange(0,10) # Output: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

- Crear arrays de **Zeros** `np.zeros((rows,cols))` o `np.zeros(n)` y de **Ones** `np.ones((rows,cols))`

- Rangos definidos con **Linspace**
`np.linspace(start,stop,n)`
Donde **start** y **stop** determina el rango digamos de 1 a 100 y **n** se refiere a la cantidad, por ejemplo 10 numeros del 1 al 100.

- Generar una **Matriz identidad**

```python
np.eye(n)
#Para n = 3

#Output matriz identidad:
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

- Generar **Numeros Alatorios**:
```python
#1. General un num aleatorio de 0 a 1
np.random.rand()
#2. General un array de n aletorios
#np.random.rand(n) para n = 4
np.random.rand(3)
array([0.75949945, 0.73539686, 0.27406198])
#3. General un matriz de n x m aletorios
np.random.rand(rows,cols)
#4. Generar un aleatorio para un rango definido.
np.random.randint(n,m) 
#5. Matriz aleatorio con valores enteros definidos n-m.
np.random.randint(n,m,(rows,cols))
```
 
 
 
 

