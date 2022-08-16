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
- `+` Indica que el proximo caracter **debe** aparecer.
- `*` Indica que **puede** aparecer 0-muchas.
- `?` Indica que **puede** aparecer 0-1. Es decir tomara solo 1 en caso de que aplique.

**Ejemplo Basico** `\d*[a-z]?s` Se podria decir que se lee de por secciones de derecha a izquierda.
1. `\d*` Puede haber 0 o Muchos`*` digitos Numericos `\d`.
2. `[a-z]?` Puede haber 0 o 1 `?` carateres de `a-z` lower case. 
3. `s` Al no haber `*,+,?` indica que la cadena debe terminar con `s`    

![image](https://user-images.githubusercontent.com/60556632/182173497-8da0f6f2-7ed8-4308-80b0-0f135017a3a2.png)

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
