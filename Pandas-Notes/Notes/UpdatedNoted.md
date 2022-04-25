## Transformacion de Datos con Numpy y Pandas - Carlos Alarcon
### NumPy

  - [x] [Numpy Array](#numpy-array)
  - [x] [Tipos de datos](#tipos-de-datos)
  - [x] [Dimensiones](#dimensiones)
  - [x] [Creando arrays](#creando-arrays)
  - [x] [Shape y Reshape](#shape-y-reshape)
  - [x] [Funciones principales de NumPy](#funciones-principales-de-numPy) 
  - [x] [Copy](#copy)
  - [x] [Condiciones](#condiciones)
  - [x] [Operaciones](#operaciones)  
### Pandas
  - [x] [Series y DataFrames en Pandas](#series-y-dataframes-en-pandas)
  - [x] [Leer archivos CSV y JSON con Pandas](#leer-archivos-csv-y-json-con-pandas)  
  - [x] [Filtrado con loc y iloc](#filtrado-con-loc-y-iloc)
  - [x] [Agregar o eliminar datos con Pandas](#agregar-o-eliminar-datos-con-pandas)

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
 
 ### Shape y Reshape
 
 Es muy importante saber manipular las formas de los datos. 

```python
#Shape
arr = np.random.randint(1,10,(3,2))
arr.shape

#Output (rows,cols) shape indica incluso las dimensiones de un tensor.
(3, 2) 

# Reshape permite manipular la forma de los datos arr.reshape(rows,cols) a veces las API requieren formas especificas y por esto es muy util.
arr.reshape(1,6) = np.reshape(arr,(1,6))
array([[7, 2, 4, 3, 3, 4]])

#Reshape + tipo de estructura segun lenguage, donde 'C'se refiere al lenguage. 
np.reshape(arr,(1,6), 'C')

# 'A' -> Segun mi sistema
# 'F' -> Segun Fortran
```

### Funciones principales de NumPy

Nos permiten realizar realizar estadisticos sobre arreglos e incluso concatenarlos.

```python
import numpy as np

arr = np.random.randint(1,20,10) #Crear vector de 10 numeros con rango de 1 a 20
matriz = arr.reshape(2,5) #Reshape a matriz de 2 X 5
matriz = np.array([[15,  5,  8, 10,  8],[12,  8,  7, 10,  4]])
#Output:
#array([[15,  5,  8, 10,  8],
#       [12,  8,  7, 10,  4]])

# .max() o .min() permite hacer las mismas operaciones sobre arrays
matriz.max() #Numero mas grande del array matricial
matriz.max(1)# Numero por eje de rows -> array([15, 12])
matriz.max(0)# Numero por eje de cols -> array([15, 8, 8, 10,  8])
matriz.argmax()# Posicion num mas grande -> 0 donde 0 es 15
matriz.argmax(1)# Posicion num mas grande eje rows -> array([0, 0])
matriz.argmax(0)# Posicion num mas grande eje cols -> array([0, 1, 0, 0, 0])

# .ptp() calcula la diferencia entre el .max() y .min()
matriz.ptp() #Donde max = 15 min = 4 luego ptp() -> 11
matriz.ptp(1) #Donde eje rows max = 15 min = 5
              #Donde eje rows max = 12 min = 4
              #Output array([10,  8])

matriz.ptp(0) #Donde eje cols de restan y se obtienen valores absolutos
              #Output array([ 3,  3,  1,  0, 4])


np.percentile(matriz,50)#Es la mediana o percentil 50
                        #Output: 8.0

matriz.sort() #Ordenal los datos de menor a mayor

np.median(matriz)#Output 8.0 es igual al percentil 50
np.median(matriz, axis=0) #Median en Eje cols -> array([ 4.5,  7.5,  8. , 10. , 13.5])
np.median(matriz, axis=1) #Median en Eje rows -> array([8., 8.])

np.std(matriz)# Desviacion estandar de los datos -> 3.067
np.var(matriz)# Varianza -> 9.409
np.mean(matriz)# Media -> 8.7

#Concatenar dos arrays como los que se muestran a continuacion:
array_a = np.array([[1,2],[3,4]])
array_b = np.array([5,6])

np.concatenate((array_a, array_b))# ValueError: all the input arrays 
                                  # must have same number of dimensions

#Concatenar al eje de Cols
np.concatenate((array_a, array_b), axis = 0)# ValueError: all the input arrays 
                                  # must have same number of dimensions    

#Para solucionarlo modificamos las dimenciones de array_b
array_b = np.expand_dims(array_b, axis=0)
np.concatenate((array_a, array_b), axis = 0) 

#Output: array([[1, 2],
       # [3, 4],
       # [5, 6]])

#Ahora para hacer la concatenacion en el axis = 1 o rows podemos
#transponer array_b.T o hacer un array_b.reshape(2,1) de no ser asi
# aparecera ValueError: all the input array dimensions for the concatenation 
#axis must match exactly
np.concatenate((array_a, array_b.T), axis = 1) 
```

### Copy

Lo correcto antes de empezar a manipular un objeto array o dataframe es crear una **copia** asi podremos hacer exploracion de datos con seguridad que no estamos deformando los datos originales.

```python
#Creamos un array de 1dim
array_a = np.arange(0,10)

#array_a se asigna a slice_array lo cual es un ERROR! 
#por que aun es el mismo espacio en memoria en vez de ser uno nuevo.
slice_array = array_a[0:6]
slice_array
```  
Output : `array([0, 1, 2, 3, 4, 5])`

```python
#Modificamos una parte del slice creyendo que solo estamos
#modificando slice_array lo cual no es verdad.
slice_array[:]=0
slice_array
```  
Output : `array([0, 0, 0, 0, 0, 0])`

```python
#Si validamos array_a veremos que tambien fue modificado 😥
array_a
```  
Output : `array([0, 0, 0, 0, 0, 0, 6, 7, 8, 9])` Shiit!  

La forma correcta es crear una **copia** como se muestra a continuacion:
```python
array_a = np.arange(0,10)
array_copy=array_a.copy()
array_copy[:] = 10
array_copy
```  
Output : `array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])`  
Y si verificamos nuestro array inicial veremos que no ubieron modificaciones 😊

```python
array_a
```  
Output : `array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])` 

### Condiciones

A traves de los condicionales podemos filtrar cualquier estructura de Datos a continuacion crearemos una y realizaremos diferentes condicionales:


```python
import numpy as np
#Creamos un array 'arr' de tipo int8
arr = np.linspace(1,10,10,dtype='int8')
arr
```  
Output : `array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10], dtype=int8)`  

```python
#Entrega una lista booleana si condicionamos el array
arr > 5
```  
Output : `array([False, False, False, False, False,  True,  True,  True,True,True])`  

```python
#Si colocamos el condicional dentro de [condicional] obtendremos los datos
indices_cond = arr > 5
arr[indices_cond]
```  
Output : `array([ 6,  7,  8,  9, 10], dtype=int8)`  


```python
#Incluso podemos colocar varios condicionales para un solo array
arr[(arr>5) & (arr<9)]
```  
Output : `array([6, 7, 8], dtype=int8)`  

Se pueden transformar los datos no solo a traves de slices sino tambien usando condicionales:
```python
arr[arr > 5] = 100
arr
```  
Output : `array([  1,   2,   3,   4,   5, 100, 100, 100, 100, 100], dtype=int8)`  

Luego de modificados podemos hacer nuevas consultas 🤠, esto se trata de creatividad.
```python
arr[arr == 100]
```  
Output : `array([100, 100, 100, 100, 100], dtype=int8)`  

### Operaciones

A diferencia de las listas en python, los arrays en Numpy nos permiten hacer todo tipo de operaciones matematicas. Por ejemplo si tratamos de hacer una operacion matematica con una lista es probale que no logremos el resultado esperado como se muestra a continuacion:  

```python
import numpy as np

#Creamos una lista con python
lista = [1,2]
#Python no entiende la operacion que quiero aplicar
lista * 2
```  
Output : `[1, 2, 1, 2]` 

Si realizamos operaciones con numpy el resultado sera diferente.
```python
#Creamos un array con numpy y realizamos una copia🚀.
arr = np.arange(0,10)
arr_cp = arr.copy()
arr_cp * 2 # Puede ser cualquier tipo de Operacion Aritmetica
#y si hay un MathError no detiene el programa.
```  
Output : `array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])` 

Realizar operaciones de **algebra lineal**✖️➕➖🟰
```python
#Sumamos el array original con la copia del mismo
arr + arr_cp 
```  
Output : `array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])` 

```python
#Usar matrices o tensores y operarlos
matriz = arr.reshape(2,5)
matriz_cp = matriz.copy()
#Sumamos original con la copia de la matriz
matriz + matriz_cp
```  
Output : `array([[ 0,  2,  4,  6,  8],
       [10, 12, 14, 16, 18]])` 

Si queremos calcular el producto punto solo debemos asegurarnos que los arrays tiene dimenciones iguales y que uno esta transpuesto:  
 
```python
#Transpuesta de matriz_cp
matriz_cp.T
```  
Output : `#Transpuesta de matriz_cp matriz_cp.T` 

Ahora si! hay varias formas de hacerlo:
```python
#Producto punto lo cual es muy util en la 
#ciencia de datos por ejemplo en proyecciones
np.matmul(matriz,matriz_cp.T)
#'matriz @ matriz_cp.T' es lo mismo que 'np.matmul(matriz,matriz_cp.T)'
```  
Output : `array([[ 30,  80],
       [ 80, 255]])` 

A continuacion: **Como calcular la proyeccion de un vector sobre otro, [Video](https://www.youtube.com/watch?v=cq6jLrNqZL8)**, tener en cuenta que producto matricial no es lo mismo que producto escalar o entre dos vectores.  

![producto-escalar](https://user-images.githubusercontent.com/60556632/165134640-152ab8e1-1391-4d47-838d-a713f480af11.png)

### Series y DataFrames en Pandas

**Pandas Series**  

Es como un array unidimensional de Numpy donde podemos: Buscar por indice y hacer Slicing, Operaciones aritmeticas sobre distintos tipos de datos

**Pandas DataFrame**  

Es como las estructuras matriciales de Numpy donde podemos hacer busqueda por indices, columnas o filas. 
 
**Pandas Series**  
```python
import pandas as pd

#Crear Series de los Jugadores del PSG
#Si no definimos el indice este iniciara desde 0
psg_players = pd.Series(['Navas','Mbappe','Neymar','Messi'], 
                        index=[1,7,10,30]
                        )
psg_players
```  
Output : `1      Navas
7     Mbappe
10    Neymar
30     Messi
dtype: object` 
 
```python
#Es posible crear el Series a traves de un diccionario
dict = {1:'Navas',7:'Mbappe',10:'Naymar',30:'Messi'}
#Ahora pasamos el dict a Series de pandas y obtenemos lo mismo
pd.Series(dict)
```  
Output : `1      Navas
7     Mbappe
10    Naymar
30     Messi
dtype: object` 

 
```python
#Realizar un slicing el cual se fija en la cantidad
# de elementos mas no en el indice.
psg_players[0:3]
```  
Output : `1      Navas
7     Mbappe
10    Neymar
dtype: object` 

**Pandas DataFrame**
 
```python
#Un DataFrame se puede definir como una super dict o JSON file
# el DataFrame al menos tiene 3 dimenciones como se muestra:

super_dict = {'Jugador':['Navas','Mbappe','Neymar','Messi'],
 'Altura':[183.0,170.0,170.0,165.0],
 'Goles':[2,200,200,200]}
df_players = pd.DataFrame(super_dict, index=[1,7,10,30])
df_players
```  
Output :

|index |Jugador |	Altura|Goles |
| --- | --- | --- | --- |
| 1	| Navas |	183.0 |	2 |
| 7	| Mbappe |	170.0 |	200 |
| 10	| Neymar |	170.0	| 200 |
| 30	| Messi	| 165.0	| 200 |

Igualmente podemos hacer consultas de columnas, indices y datos
```python
#Obtener columnas del DataFrame
df_players.columns
```  
Output : `Index(['Jugador', 'Altura', 'Goles'], dtype='object')` 

### Leer archivos CSV y JSON con Pandas  
 
```python
import pandas as pd

#Montamos un sistema local de archivos a colab 
# en este caso el de google drive
from google.colab import drive
drive.mount('/content/drive')

#Permite cargar modulos de Python es un magic command
%reload_ext autoreload
#Reload all modules except those excluded by %aimport 
%autoreload 2
```  
Output : `Drive already mounted at /content/drive` 

 Asi cargamos archivos **csv** y **JSON**
```python
#Cagar archivos csv
#A veces debemos usar el argumento 'sep' dependiendo
# el seperador del archivo csv.

#El arg 'header' permite definir que fila se debe tomar como header por defecto es igual a 0
#El arg 'names' se refiere a los nombres de las columnas.

df_countries = pd.read_csv('/content/drive/MyDrive/conda_data_science/data/raw/Metadata_Country.csv')
```  
Es poco comun leer archivos JSON, normalmente es csv o sql donde sql se convierte primero a csv.
```python
#Se puede realizar comunmente en datos estructurados como JSON
#Podemos convertirlo a Series con el arg typ='Series'

pd.read_json('/content/drive/MyDrive/conda_data_science/data/raw/students.json')
```  
Output:
```
	edad	cm	pais	genero	Q1	Q2
0	10	115	co	M	5.0	7
1	9	110	mx	F	10.0	9
2	13	130	co	F	8.0	9
3	14	155	mx	M	NaN	8
4	12	125	mx	M	7.0	8
5	11	120	ch	M	8.0	8
6	12	125	ch	F	3.0	9
```

### Filtrado con loc y iloc

```python
#Filtrado por indices
df_data[0:4]
```  
Output : 
```
edad	cm	pais	genero	Q1	Q2
0	10	115	co	M	5.0	7
1	9	110	mx	F	10.0	9
2	13	130	co	F	8.0	9
3	14	155	mx	M	NaN	8
```
#Filtrado por Columnas
df_data[['edad','cm','pais']]

#Primero filtramos por indice y luego por Columna con loc
#df_data.loc[0:4,'edad']

#Primero filtramos por indice y luego por Columna con iloc
df_data.iloc[0:4,:2]

Output:
```
	edad	cm
0	10	115
1	9	  110
2	13	130
3	14	155
```

### Agregar o eliminar datos con Pandas
```python
#Eliminamos columna 'edad' usamos arg inplace=True para que se guarde.
df_data.drop('edad', axis=1, inplace=True)
df_data
```  
Output : 
```
	cm	pais	genero	Q1	Q2
0	115	co	M	5.0	7
1	110	mx	F	10.0	9
2	130	co	F	8.0	9
3	155	mx	M	NaN	8
4	125	mx	M	7.0	8
5	120	ch	M	8.0	8
6	125	ch	F	3.0	9
```

```python
#Borrado de Filas
df_data.drop([0,1,2],axis=0, inplace=True)
df_data
```  
Output : 
```
cm	pais	genero	Q1	Q2
3	155	mx	M	NaN	8
4	125	mx	M	7.0	8
5	120	ch	M	8.0	8
6	125	ch	F	3.0	9
```

```python
#Borrado de Rango de Filas
df_data.drop(range(4,6),axis=0, inplace=True)
df_data
```  
Output : 
```
cm	pais	genero	Q1	Q2
3	155	mx	M	NaN	8
6	125	ch	F	3.0	9
```

```python
#Agregar Columnas
import numpy as np
df_data['New_column'] = np.nan
df_data
```  
Output : 
```
cm	pais	genero	Q1	Q2	New_column
3	155	mx	M	NaN	8	NaN
6	125	ch	F	3.0	9	NaN
```

```python
#Agregar filas
df_data.append(df_data, ignore_index = True)
```  
Output : 
```
cm	pais	genero	Q1	Q2	New_column
0	155	mx	M	NaN	8	NaN
1	125	ch	F	3.0	9	NaN
2	155	mx	M	NaN	8	NaN
3	125	ch	F	3.0	9	NaN
```




```python

```  
Output : 
```

```

