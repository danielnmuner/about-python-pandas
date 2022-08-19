## Expresiones Regulares [TestRegex](https://rubular.com/)

### ¿Qué son las expresiones regulares?
Consite en la creacion o diseño de patrones personalizados que permitiran filtrar un conjunto de datos.

### Aplicaciones de las expresiones regulares
[Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)

- Uso en la lectura de archivos `.log` de los servidores como `nginex`.
- En Backend se usa para validar los datos dentro de un formulario.

### Introducción al lenguaje de expresiones regulares

- **Archivo TXT** Serie de cadenas de caracteres. *Una sucesión de líneas.*
- **Cadena de caracteres** Un carácter seguido de otro carácter, seguido de otro carácter.
- **Caracter** Representación gráfica en bits de algún código, en su mayoria casos ASCII. Es la unidad mínima que se puede abstraer de una cadena de caracteres.
- La unidad minima en **REGEX** es `.` el punto. Es decir si colocamos `.` en una busqueda el resultado seran todos lo caracteres del archivo uno a uno incluso espacios.
- Si buscamos `.....` **REGEXP** traera una busqueda mas especifica para conjuntos de 5 caracteres agrupados.

### Las clases predefinidas y construidas de REGEXP
- `\d` Selecciona dígitos. Equivalente: `[0-9]` $\to$ Todos los Numeros. `[7-9]` $\to$ Numeros del 7 al 9
- `\w` Resalta caracteres. Equivalente: `[a-zA-Z0-9]` Busca lo que puede ser equivalente a una palabra sin caracteres especiales. 
- `[a-tA-Z0-2_\.]` Solo lower case de la `a-t`, upper case `A-Z`, numeros de `0-2`, caracteres especial `_` y `.`. 
- `\s` Muestra los espacios en blanco. Equivalente: `[ ]` o Espacios en blanco.
- `[ \.]` Busca el símbolo de punto

### Delimitadores +, *, ?

- `*` Es una abrevicion `todo`, `\d*` Resaltara todos los caracteres numericos. `.*` Todos los caracteres sin distriminacion.
- `+` Indica que el proximo caracter **debe** aparecer es decir mas de uno.
- `*` Indica que **puede** aparecer 0-muchas.
- `?` Indica que **puede** aparecer 0-1. Es decir tomara solo 1 en caso de que aplique.

**Ejemplo Basico** `\d*[a-z]?s` Se podria decir que se lee de por secciones de derecha a izquierda.
1. `\d*` Puede haber 0 o Muchos`*` digitos Numericos `\d`.
2. `[a-z]?` Puede haber 0 o 1 `?` carateres de `a-z` lower case. 
3. `s` Al no haber `*,+,?` indica que la cadena debe terminar con `s`    

### Los contadores {1,4}

1. `\d\d` Este patron extrae no solo **dos** digitos numericos sino pares de digitos numericos en una cadena de caracteres como `1234` es decir cadenas pares. `\d\d\d` traeria cadenas nuericas consecutivas multiplos de 3
2. `\d{2,4}` Este patron extrae cadenas de digitos numericos cuyo largo sea de **2** a **4** digitos.
3. `[a-zA-Z]{10}` Extrae cadenas de caracteres no numericos, no especiales de 10 cararacteres de largo. 
4. `\d{4,}` Podemos definir un limite inferior y dejar abierto el limite superior.

**Ejemplo Contadores** `\d{2,2}[\-\.]?` Este patron tiene algo adicional y es la creacion de una **clase personalizada** como `[0-9]` o `[a-z]` la clase es `[\-\.]` es decir `-` o `.`.
1. `\d{2,2}` cadenas de caracteres numericas de minimo 2 digitos y maximo 2 digitos.
2. `[\-\.]?` Inidica que puede o no haber `-` o `.` justo despues de las cadena numerica.
3. Este patron podria identificar $\to$ `12345678`, `12-34-56-78`, `12.34.56.78`
4. `\d{2,2}[\-\.]?\d{2,2}[\-\.]?\d{2,2}[\-\.]?\d{2,2}[\-\.]?` En el punto 3 se realizan match a nivel de caracteres pero para hacerlo a nivel de linea podemos replicarlo segun la necesidad.
5. Ademas pudes añadir un espacio en blanco `[\-\. ]?` y reemplazar en `?` por un contador `[\-\. ]{0,1}`


### El caso de (?) como delimitador de lo General a lo Especifico
1. `.*,` Trae `.*` todo lo que anteceda una coma `,` a nivel general. Ejemplo `csv1,csv2,csv3,`
2. `.+?,` Trea todo lo que antecede a una coma `,` a un nivel mas especifico `cvs1,` `csv2,` `csv3,` 

### Not (^), su uso y sus peligros
1. `\w` corresponde a todo lo que se ajusta a `[a-zA-Z0-9]` sin embargo `\W` corresponde a todo lo que no se justa a `\w`.
2. `[^0-5a-c]` indica que solo toma `[6-9d-z]`
3. Cuando estudiamos contadores creamos la expresion `\d{2,2}[\-\.]?` la cual puede ser reemplazada por `\d{2,2}\D?` donde `\D` es simplemente un **No Numerico** lo cual permitiria cual quier tipo de caracter.  Es decir es menos riguroso pero igualemte util.

### Principio (^) y final de linea ($)
1. Usualmente en una sola linea de cadenas de caracteres varias cadenas o incluso caracateres se ajustan al patron establecido. Para evitar multiples matches a nivel de linea y ser mas estrictos indicamos el inicio y le fin de la Expresion regular para evitar su multiplicacion en la linea. Ejemplo `^\d\d$` solo toma dos digitos numericos por linea si una cadena tiene mas de 2 o incluso es par entonces no sera tomada en cuenta.
2. `^[^\d]$` Que es un solo carater no numerico.
3. `^\w+,\w+,\w+$` Mas de un caracter alfanumerico seguido de una coma hasta 3 veces. **Si ocurre una cuarta vez se ignorara por completo toda la linea.**


**Nota** `Escapamos cuando necesitamos usar caracteres reservados`
### Teléfonos
1. Aplica para un caso de uso especifico visto en la [clase](https://platzi.com/clases/1301-expresiones-regulares/11859-telefonos/). Expresion `^\+\d+[#pe]?\d*$` Donde `\+` es por que necesitamos `+` y este es un caracter reservado. Por otro lado `[#pe]?` es una clase delimitada por `?`.
2. `\+?\d{2,3}[^\da-z]?\d{2,3}[#pe]?\d*$` Toda la expresion regualar se hace de manera experimental para lo cual podriamos utilizar una editor de codigo. **Nota**: `[^\da-z]?` Es una clase que acepta todo menos datos alfanumericos lower case. 


### RegExp en URLs(Dirrecione/Dominios)
1. Expresion `https?:\/\/[\w\-\.]+\.\w{2,5}\/?\S*`. La expresion `https?` es equivalente a `http[s]?` aun que parece que `https?` toma toda la cadena de carateres en realidad solo esta tomando la inmediata anterior. La clase `[\w\-\.]` escapa `-` y `.` debido a que son reservados. Finalmente `\S` al final no aceptara espacion esn blanco. 

## RegExp en Emails
1. `[\w\._]{5,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}`

### Localizaciones
1. Las coordenadas usualmente son Lat/Lon, donde los valores oscilan entre 0 y 180 mas 6 cifras significativas como maximo.
2. `^\?\d{1,3}\.\d{1,6},\s?\-?\d{1,3}\.\d{1,6},.*$` $\to$ `-134.345678, 123.567845, WW EE`
3. Las coordenadas tambien se pueden entregar en formato de Grados, Minutos y Segundos.
4. `^\-?\d{1,3}\s\d{1,,2}' \d{1,2}\.\d{2,2}"[WE],\s?\-?\d{1,3}\s\d{1,2}' \d{1,2}\. \d{2,2}"[SN]$` $\to$ ``-34 54' 32.00"N, -31 23' 34.00"S`

### Búsqueda y Reemplazo **Agrupar** `()` o Variables en RegExp
1. `^\d+::([\w\s:,\(\)'\.\-&!\/]+)\s\((\d\d\d)\)::.*$` $\to$ `240::Hoop Dreams (1990)::Documentary` Agrupar consiste en seccionar una cadena de caracteres. En general con las RegExp creamos patrones que pueden filtrar cadenas de caracteres sin embargo los grupos exiten para separar patrones por grupos. 
2. `([\w\s:,\(\)'\.\-&!\/]+)` $\to$ `$1`, `(\d\d\d)` $\to$ `$2` Reprecentan dos patrones aplicados a una sola cadena de carateres aun siendo estrictos con el inicio y el fin de la expresion `^$`. Es importante tener encuenta que aun que hay otros parentesis `\(\)` estos en realidad se `Escapan` y se utilizan como parte de los patrones. 
3. En la practica **Buscar** llevaría los **2** patrones agrupados `^\d+::([\w\s:,\(\)'\.\-&!\/]+)\s\((\d\d\d)\)::.*$` y en **Reemplazar** por ejemplo `INSERT INTO TABLE (YEAR,TITLE) VALUES($2,$1)` entonces el Editor/Lenguaje de Programación solo tomará lo que esta en el Grupo y los colocará dentro de la estructura definida en **Reemplazar**.
4. Ejemplo aplicado a JSON $\to$ `{title:"$1", year:$2}`

### Uso de REGEX para descomponer Queries GET en una ULR
El tracking de las URL's es importante en Analytics y nos referimos al Metodo GET puesto que la informacion viaja concatenada a una URL. `https://www.google.com/search?q=regex+platzi&oq=regex+platzi&aqs=chrome..69i57j69i60.6885j0j9&sourceid=chrome&ie=UTF-8` El informacion se coloca a partir de `[\?&]` y luego se concatena entre `&` Asi la expresion regular para Buscar y Reemplazar sería **Find**: `[\?&](\w+)=([^&\n]+)` y **Replace**: `\n - $1=$2`.

1. `$1` $\to$ `(\w+)=` respentando la condicion `[\?&]`. Asi `?q=regex+platzi&oq=regex+platzi` sería `q=` , `oq`
2. `$2` $\to$ `([^&\n]+)` luego justo despues de `=` debe haber cualquier texto pero no podemos tomar `&` o `\n` puesto que ambos son delimitadores del patron, asi que debemos usar `^` para negar esos dos caracteres. Entonces para `?q=regex+platzi&oq=regex+platzi` sería `regex+platzi` , `regex+platzi` 

### `grep` y `find` desde consola
1. `cat file_name.csv | wc -l` $\to$ Indica la cantidad de lineas en el archivo.
2. `cat file_name | grep ^2012` $\to$ Todas la filas que inician con 2012.
3. `cat file_name | grep ,3[0-9],` $\to$ Lineas que continen el `31` entre `,`
4. `cat file_name | grep SE$` $\to$ Termina en `SE`
5. `cat file_name | grep Brazil | grep ^1952` $\to$ Se procesa una despues del otro. Intput | Output/Input | Output




