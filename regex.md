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
1. `[\w\._][5,30]\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}`




