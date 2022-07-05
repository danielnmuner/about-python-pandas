# Analisis de Datos con Power BI
Renzo Roca

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
  
