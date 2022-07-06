# Analisis de Datos con Power BI
Renzo Roca [Fuentes de Datos](https://drive.google.com/drive/folders/1Fj0pAHTaFrQpIub3yEQ_4-aZDFAiV6Jt)

## Business Intelligence con Power BI
Flujo de BI 
  - **ETL**: Extraccion Consolidacion de Fuentes de limpieza y Transformacion.
  - **Modelacion**: Relaciones, Indicadores, optimizacion
  - **Reporting**: Visualizacion de Datos(PowerBI-Solucion Integral(Suit Microsoft) en BI pero Especialista en Visualizaciones), dashboards, History Telling

Opciones de Power BI
- **Desktop**: Orientado al desarrollo y la creacion de Reportes
- **Service**: Orientado al Trabajo Colaborativo.
- **Mobile**: Orientado a la facilidad de acceso.

## Arquitectura de Power BI

Power BI Free
  - Incluye 1 GB de almacenamiento.
  - No permite la colaboración simultánea.

Power BI PRO
  - Incluye 10 GB de almacenamiento.
Se puede compartir con usuarios internos siempre que también cuenten con una licencia PRO. 
Cuenta con una opción de puerta de enlace (Power BI Gateway). Soporta hasta 8 recargas de aplicación al día.
![gateway](https://user-images.githubusercontent.com/60556632/177362781-c8011f06-4820-48b0-9af2-e45c71a4fd34.png)


Power BI Premium
  - Incluye 100 TB de almacenamiento.
  - Se puede compartir con usuarios internos sin que tengan Power BI Pro.
  - Mayor escalabilidad y rendimiento que la capacidad compartida en Power BI Service.
  - Cuenta con Power BI Gateway. Soporta hasta 48 recargas por día.

Tipos de conexiones
  - **Importación**: Se crea una copia para analizar los datos.
  - **Direct Query**: Los datos no se copian puesto que cambia con el tiempo, cada interacción hace una consulta a la base de datos. 
  - **Live Connection o dinámica**: Lectura desde SSAS o desde un conjunto de datos de Power BI Service.
  - **Modelos Compuestos**: Combina las tecnologías de Importación y Direct Query. Permite utilizar múltiples conjuntos de datos.

Datos Base de Datos SQL Server
  - **Servidor**: renzoroca.database.windows.net
  - **BD**: Ciclismo
  - **Usuario**: practicas
  - **Contraseña**: pr@acticasRR2021.
  - **Owner**: https://www.flowcode.com/page/renzoroca
  
¿Qué es ETL?
  - **Extract**: Extraer datos desde cualquier fuente, ya sea archivos planos, binarios, bases de datos o servicios cloud.
  - **Transform**: Transformar, limpiar o enriquecer la información extraída sin modificar la fuente.
  - **Load**: Cargar los datos ya transformados al modelo de datos.

Transformar datos con Power Query

- **¿Qué hace Power Query?**: Extrae , transforma y carga en Power BI los datos para su posterior análisis, es decir no analiza los dato solo los prepara. **Magia**:Es similar a los macros de Excel, podemos movernos en el flujo de trabajo.Simplemente seleccionamos la tabla que queremos procesar y hacemos clic en **Transformar datos**. Podemos observar cada tipo de dato. Power Query maneja distintos tipos de datos que Excel. Al conectarse a una fuente de datos, crea diversos **Pasos aplicados**.

Las transformaciones más comunes que podemos realizar en Power Query son:
  - Cambiar tipo de dato
  - Anexar consultas
  - Dividir columnas
  - Combinar consultas
  - Reemplazar valores
  - También podemos hacer combinaciones:
  - Combinar binarios
  - Agregar columnas
  - Filtrar datos.

**Tipos de combinaciones en Power BI**
- **Anexar**: Permite unir dos o más tablas de manera vertical. Se recomienda que ambas tablas tengan la misma estructura. Si este no es el caso, el sistema añade al conjunto final los campos de todas demás con valores nulos.

Similar a una operación UNION de SQL.
Los resultados pueden ser una nueva consulta o ser agregada a un paso de la existente.
Combinar consultas
Nos permite tomar dos tablas y cruzarlas mediante una columna en común.
Usualmente utilizado para complementar información de una tabla.
Es el equivalente más cercano a la función JOIN del estándar SQL.
Los distintos tipos de combinaciones (y su equivalente en SQL) son:
Externa izquierda (LEFT JOIN)
Externa derecha (RIGHT JOIN)
Externa completa (FULL OUTER JOIN)
Interna (INNER JOIN)
Anti izquierda (LEFT EXCLUSIVE JOIN)
Anti derecha (RIGHT EXCLUSIVE JOIN)
Combinar binarios:
Permite extraer las tablas de los archivos mediante un proceso automatizado.
Usualmente utilizado mediante el conector de carpeta.
Es de especialidad utilidad cuando la fuente de información se encuentra demasiado fragmentada como para la operación de anexar.


## Crear Visualizaciones

**Metodologia Storytelling**: Una metodología dentro del data storytelling es SCRAP, que se refiere a:
- Spaced: Respetar espacios tanto dentro del gráfico como entre visualizaciones.
- Contrast: Aplicar colores contrastantes para destacar algo en vez de tener informes monocromáticos ayudará a enfocar la atención del usuario en donde queremos.
- Repeat: Aplicar de manera consistente tipografías, esquemas de diseño, tamaño de fuente, etc.
- Alineado: Las visualizaciones deben estar ordenadas y alineadas. Un informe desordenado puede distraer la atención del usuario.
- Proximity: Los objetos visuales que estén relacionados deben estar próximos entre sí.
SCRAP está relacionado con los principios de diseño de Gestalt.

**Tips para una buena visualización**
- Menos es más
- Los colores son importantes, úsalos bien. (Usar los colores de la Empresa)
- Mantén tus elementos bien alineados.
- No siempre es bueno mostrar todo en una cifra. (Apoyarse de un catalogo de Visualizaciones)
- Muestra solo información relacionada. 
- Una mala elección de un visual puede ocasionar que la información no se transmita de manera correcta, llegando incluso a tergiversar el entendimiento de la misma. 



