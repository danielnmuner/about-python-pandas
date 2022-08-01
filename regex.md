## Expresiones Regulares [TestRegex](https://rubular.com/)

### ¿Qué son las expresiones regulares?
Consite en la creacion o diseño de patrones personalizados que permitiran filtrar un conjunto de datos.

### Aplicaciones de las expresiones regulares
[Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)

- Uil en la lectura de archivos `.log` de los servidores como `nginex`.
- En Backend se usa para validar los datos dentro de un formulario.

### Introducción al lenguaje de expresiones regulares

- **Archivo TXT** Serie de cadenas de caracteres. *Una sucesión de líneas.*
- **Cadena de caracteres** Un carácter seguido de otro carácter, seguido de otro carácter.
- **Caracter** Representación gráfica en bits de algún código, en su mayoria casos ASCII. Es la unidad mínima que se puede abstraer de una cadena de caracteres.
- La unidad minima en **REGEX** es `.` el punto. Es decir si colocamos `.` en una busqueda el resultado seran todos lo caracteres del archivo uno a uno incluso espacios.
- Si buscamos `.....` **REGEX** traera una busqueda mas especifica para conjuntos de 5 caracteres agrupados.

### Las clases predefinidas y construidas de REGEX
- `\d` = Selecciona dígitos. Equivalente: `[0-9]` $\to$ Todos los Numeros. `[7-9]` $\to$ Numeros del 7 al 9
- `\w` = Resalta caracteres. Equivalente: `[a-zA-Z0-9]` Busca lo que puede ser equivalente a una palabra. 
- `\s` = Muestra los espacios en blanco. Equivalente: `[ ]` o Espacios en blanco.
- `[ \.]` = Busca el símbolo de punto

