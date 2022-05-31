# Learning SAS

## Environment
**Menu**
- **Server Files and Folders**
- Task and Utilities
- Snippets
- **Libraries**
- File shortcuts

**Server Files and Folders**
Normalmente se deben guardar los archivos en `Archivos(Inicio)`.

**Libraries**
Es un repositorio de Datos donde podemos asignar permisos basados en roles. Para acceder a los datos indicamos el nombre de la libreria y el nombre del tada set.
```sas
/*Nombre del dataset*/
data test;
/*Ruta del dataset en libraries*/
    set sashelp.airline;
/*Cada linea finaliza con `;` y los errores de sintaxis no se muestran como tal*/
run;
```
Para ejecutar el codigo tenemos que seleccionarlo y luego ejecutarlo, ademas es importante guardarlo en una carpeta en `Archivos(Inicio)`.
## Gettin Start
La `columnas` las llamamos `Variables`
Las `filas` las llamamos `Observations`
- **Origin Datasets**
![image](https://user-images.githubusercontent.com/60556632/171077136-abce897e-a56e-48f2-9c20-e1808159fa1e.png)

- **Tipos de Variables**
![image](https://user-images.githubusercontent.com/60556632/171077420-a751bd8c-e4b4-4fb0-a935-77c0382aa834.png)
- **Valores nulos de tipo caracter y numericos**
![image](https://user-images.githubusercontent.com/60556632/171077482-b29ef687-45be-4076-a2b7-9c614836db2b.png)
- **Reglas para nombrar variables en SAS**
![image](https://user-images.githubusercontent.com/60556632/171077650-94624eea-e81f-4456-9ccb-800fe7c42de1.png)

- **Tipos de Bloques en SAS**
    - `data step` _Crea o modifica datos_
```sas
/*Creamos variable o DataFrame*/
data airline_create;
    set sashelp.airline;
/*Creamos la columna Month la cual es igual al mes de la columna date*/
    Month = month(date);
run;
/*Procedure step que imprime data que es igual a airline create*/
proc print data=airline_create;
run;
```

**Datalines**
```sas
data demografic_cols;
/*Ademas de $ para indicar que es tipo caracter podemos usar 1-5 rangos para
indicar los espacios que pueden ocupar los datos de las filas es como
un limitante de carateres y numeros, es util cuando tenemos archivos de
texto alineados pero sin limitadores como ; o ,*/
	input Name $ 1-5 Age 6-8 State $ 9-11 Weight 12-15;
	datalines;
Marie 25 WV 132
Danie 188 ST 188
;
run;

proc print data=demografic_cols;
run;
```
- **Datalines Archivos separados por espacios**
```sas
data demografic_cols;
/*Donde infile recibe la ruta del archivo no delimitado por ; sino por espacios*/
	infile 'path/file.txt';
/*+1 salta una colmna e inicia a partir de la siguiente
@18 Indica que iniciara en la columna 18*/
	input Gender $ 1-2 Index +1 Age $ 5-6 Ethnicity $ @18;
run;

proc print data=demografic_cols;
run;
```

- **Datalines en Fechas**
```sas
data date_sample;
/*El 10. indica el total de caracteres incluyendo `-`
si no usamos format obtendremos el valor numerico de la fecha*/
	format Date_Birth MMDDYY10.;
	input Name $ Date_Birth MMDDYY10.;
	Datalines;
Oliver 03-16-1972
Natalie 12-11-1965
;
run;
proc print data=date_sample;
run;
```




