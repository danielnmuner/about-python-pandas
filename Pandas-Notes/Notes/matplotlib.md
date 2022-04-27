# Visulizaciones con Matplotlib y Seaborn
### [Someone Notes](https://aldeherr.github.io/Seabor_matplotlib/)

### Matplotlib
  - [x] [La importancia de la visualización de datos](#la-importancia-de-la-visualización-de-datos)
  - [x] [Subplot](#subplot) 
  - [x] [Método orientado a objetos](#método-orientado-a-objetos) 
  - [x] [Subplots](#subplots)
  - [x] [Leyendas, etiquetas, títulos, tamaño](#leyendas-,-etiquetas-,-títulos-,-tamaño)


### La importancia de la visualización de datos

**Cheatsheets** valiosas
![image](https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png)
![image](https://matplotlib.org/cheatsheets/_images/handout-beginner.png)
![image](https://matplotlib.org/cheatsheets/_images/handout-intermediate.png)
![image](https://matplotlib.org/cheatsheets/_images/cheatsheets-2.png)
![image](https://matplotlib.org/cheatsheets/_images/handout-tips.png)

### Pyplot básico [Funciones](https://matplotlib.org/stable/plot_types/basic/plot.html)

```python
#Importamos la libreria de Matplotlib
import numpy as np
import matplotlib.pyplot as plt

#Creamos un array con linspace el cual particiona un rango
#en este caso 0 a 5 en 11 partes iguales
x =  np.linspace(0,5,11)
y = x ** 2 #Funcion cuadratica

#Definine los ejes X, Y con plot(X,Y), ademas de formato con 'bs-'
#Ejemplo: plot(x,y,'color,string,tipo_linea') 
plt.plot(x,y,'bs-')
#Para que se muestre la grafica usamos:
plt.show()
```
![image](https://user-images.githubusercontent.com/60556632/165412747-d3cbe9ae-5584-4d84-b313-c318924dfeff.png)

```python
#Graficar X en un histograma cambiando 'plot' por 'hist'
plt.hist(x)
#plt.pie(x) Grafico de pastel
#plt.scatter(x,y) Grafico de correlacion
#plt.boxplot(x) Grafico de cajas
plt.show()
```
![image](https://user-images.githubusercontent.com/60556632/165412773-5d6479fe-0707-439f-b309-46cbddf0257e.png)


Fomato en Graficas con Matplotlib.pyplot

**Formatos de Strings**

| character | description            |
| --------- | ---------------------- |
| ‘.’       | point marker           |
| ‘,’       | pixel marker           |
| ‘o’       | circle marker          |
| ‘v’       | triangle\_down marker  |
| ‘^’       | triangle\_up marker    |
| ‘<’       | triangle\_left marker  |
| ‘>’       | triangle\_right marker |
| ‘1’       | tri\_down marker       |
| ‘2’       | tri\_up marker         |
| ‘3’       | tri\_left marker       |
| ‘4’       | tri\_right marker      |
| ‘8’       | octagon marker         |
| ‘s’       | square marker          |
| ‘p’       | pentagon marker        |
| ‘P’       | plus (filled) marker   |
| ‘\*’      | star marker            |
| ‘h’       | hexagon1 marker        |
| ‘H’       | hexagon2 marker        |
| ‘+’       | plus marker            |
| ‘x’       | x marker               |
| ‘X’       | x (filled) marker      |
| ‘D’       | diamond marker         |
| ‘d’       | thin\_diamond marker   |
| ‘|’       | vline marker           |
| ‘\_’      | hline marker           |

**Tipos de Lineas**

| character | description         |
| --------- | ------------------- |
| ‘-’       | solid line style    |
| ‘–’       | dashed line style   |
| ‘-.’      | dash-dot line style |
| ‘:’       | dotted line style   |


**Colores**
| character | color   |
| --------- | ------- |
| ‘b’       | blue    |
| ‘g’       | green   |
| ‘r’       | red     |
| ‘c’       | cyan    |
| ‘m’       | magenta |
| ‘y’       | yellow  |
| ‘k’       | black   |
| ‘w’       | white   |

### Subplot
```python 
#Subplot es una herramienta que nos permite colocar varios graficos
#Creamos un array usando numpy

x = np.linspace(0,5,11)
y = x ** 2

#subplot de 1 row X 2 cols luego son dos graficos
#por tanto de indica en el 3er arg si es el 1 o el 2

plt.subplot(1,2,1) #1er Grafico dos en uno

plt.plot(x,y,'g--') #Relacion X,Y
plt.plot(y,x,'g--') #Relacion Y,X

plt.subplot(1,2,2) #2er Grafico
plt.hist(y) # Histograma de Y
plt.show()
```
![image](https://user-images.githubusercontent.com/60556632/165413712-eeed0c98-e751-4307-9af6-f708990ad75e.png)

### Método orientado a objetos

```python
#Object Oriented
# - Requiere mas codigo pero vale la pena
# - Mayor personalizacion
# - Mas amigable a mulipple graficos
# - Mas codigo

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

#Creamos el objeto fig. El metodo figure() es el liezo
#donde van las graficas
fig = plt.figure()

#Definimos las dimenciones y posicion del Lienzo de cada grafico
#add_axes([pos_x,pos_y,len_x,len_y])

axes = fig.add_axes([0.1,0.1,0.8,0.9])
axes2 = fig.add_axes([0.2,0.55,0.4,0.3])

#Graficamos axes como objetos independientes
axes.plot(x,y,'b')
axes2.plot(y,x,'m')

#Mostrar objeto fig o lienzos
fig.show()
```
![image](https://user-images.githubusercontent.com/60556632/165430699-726c10ef-d88b-4a94-8f71-2361f69f8c24.png)

**Partes de Fig**
![image](https://user-images.githubusercontent.com/60556632/165423223-c5e00e5a-40c7-4a99-b286-6bcb1666e690.png)

### Subplots

```python
#Object Oriented
# - Requiere mas codigo pero vale la pena
# - Mayor personalizacion
# - Mas amigable a mulipple graficos
# - Mas codigo

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

#Definimos objetos fig y axes, en otras palabras
#crear el lienzo para luego graficar 1 row X 2 cols
fig, axes = plt.subplots(nrows=1,ncols=2) #Diferente de Subplot

#Primer grafico en la posicion [0]
axes[0].plot(x,y,'b')
#Primer grafico en la posicion [1]
axes[1].plot(y,x,'g')
plt.show()
```
![image](https://user-images.githubusercontent.com/60556632/165432534-4d5087e2-0b85-4c32-bd1f-fcce39f336bc.png)

```python
#Como la salida es un array entonces podemos definir
#previamente el nombre de los axes en vez de usar posiciones 
fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2) #Diferente de Subplot

#Exactamente igual al grafico anterior, a esto nos referimos 
#con orientado a objetos independientes
ax1.plot(x,y,'b')
ax2.plot(y,x,'g')
plt.show()
```
![image](https://user-images.githubusercontent.com/60556632/165432534-4d5087e2-0b85-4c32-bd1f-fcce39f336bc.png)


```python
#Si creamos un lienzo de tipo matricial
#axes se debe indicar la posicion a menos que 
#(ax1,ax2,ax3,ax4)
fig, axes = plt.subplots(nrows=2,ncols=2)

#Indicamos la posicion de acada axes.
axes[0,0].plot(x,np.cos(x),'y')
axes[0,1].plot(x,np.sin(x),'r')
axes[1,0].plot(x,np.tan(x),'m')
axes[1,1].plot(x,np.cos(x),'b')

#Controla el padding entre bordes de los figs
fig.tight_layout()
```
![image](https://user-images.githubusercontent.com/60556632/165432624-fd644ed8-d707-4c18-9ba5-e06e4fb0e24b.png)

### Leyendas, etiquetas, títulos, tamaño

```python
#A continuacion le daremos mas contexto a los graficos
#Creamos objetos fig y axes

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

#Cambiamos el tamaño todo el Lienzo conÑ 
#figsize=(len_x,len_y)
fig, axes = plt.subplots(1,2,figsize=(5,5))

#Titulo axes[0]
axes[0].set_title('Relacion_X Y')
#Ejes
axes[0].set_xlabel('Axis X')
axes[0].set_ylabel('Axis Y')
#Etiquetamos dentro de 'plot' y con lenged
axes[0].plot(x,y,'b',label='$sin(x)$')
axes[0].legend()

#Titulo axes[1]
axes[1].set_title('Relacion_Y X')
#Ejes
axes[1].set_xlabel('Axis Y')
axes[1].set_ylabel('Axis X')
#Etiquetamos dentro de 'plot' y con lenged
#dentro del signo $$ podemos colocar notacion matematica
axes[1].plot(y,x,'m',label='$sin(y)$')
axes[1].legend()

#Controla el padding entre bordes de los axes
fig.tight_layout()
```
![image](https://user-images.githubusercontent.com/60556632/165434284-1c7236d7-6552-4e34-9005-c44750f16a3f.png)

