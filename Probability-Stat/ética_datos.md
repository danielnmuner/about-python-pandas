
## Curso de Ética y Manejo de Datos para Data Science
 
**¿Qué son los datos personales?**
Información que permite identificar a una persona de manera directa o indirecta.

  - Edad
  - Teléfono
  - Domicilio
  - Correo Electrónico
  - Documento nacional de identidad (INE en México)
  - Número de seguridad social
  - Ingresos
  - Fecha de nacimiento

Se pueden clasificar por jerarquía de riesgo de importancia:

  - Datos personales ordinarios $\to$ Nombre, dirección, finanzas personales, etc.
  - Datos personales sensibles $\to$ Origen étnico, opiniones políticas y religiosas, orientación sexual.
  - Datos especiales $\to$ Genéticos, biométricos y de salud (Vienen de fuentes no convencionales.

**¿Qué datos no son personales?**

  - Los datos anónimos (información anonimizada)
  - Los datos de personas jurídicas (instituciones)
  - Información que no permita identificar a la persona.
 
**Los datos biométricos**: Se consideran datos personales $\to$ Permiten identificar a una persona

  - Reconocimiento facial
  - Reconocimiento por retina
  - Reconocimiento vascular
  - Reconocimiento por firma
  - Reconocimiento de escritura
  - Acceso por voz
  - Reconocimiento de escritura de teclado

**Clasificación de los datos biométricos**
**Por naturaleza**

  - Universal
  - único (un análisis clínico)
  - Permanente (huella digital)

**Por característica**

  - Rasgos del orden físico o de su fisiología
  - Rasgos de comportamiento o su personalidad (Se sacan a partir de múltiples interacciones)

### Escándalos históricos de uso de información

- En **1940** en Holanda el 1.5% de la Población era Judia. La fuga de datos de la población Judia permitio que Alemania cometiera el genocidio en Holanda.
- En **2016** el Instituto Nacional Electoral de Mexico **INE** publico por error en un repositorio abierto de S3-Amazon todos datos personales de una mayoria importante de la población Mexicana.

### Interés creciente por la información

Actualmente se pueden analizar todo tipo de Blobs es decir binarios con Sonido, Imagenes, Video, Lenguaje Natural etc. Entre mas información recolectada de un usuario potencial las Empresas tendran mas oportunidad de Negocio. En consecuencia de la cantidad de información que esta siendo recolectada se han creado regulaciónes de uso donde se establece el volumne maximo que pueden manejar y admás se debe justificar los motivos de la recolección. Actualmente se busca regular la compra y venta de datos entre empresas de manera que se llegue a catalogar como ilegal.

### Bias y GIGO en datos

- **Bias** o Sesgo: Consiste en seleccionar muestras no significativas estadisticamente y realizar conluciónes. Empresas que realizan inteligencia para reconocimiento facial han usado en su mayoría personas blancas lo cual sesga el uso de esta inteligencia respecto a personas de color.

- **GIGO** Garbarge in Garbarge out: La calidad del resultado o **output** depende de la calidad de la entrada de los datos o **input**

### Advertencias de uso en marketing Pelicula $\to$ **The Social Dilemma**

- Evitar campañas discriminatorias
- Precios por información Privilegiada
- Manipulación de campañas politicas.
- Fomento de conductas adictivas y ataques emocionales.


### Advertencias de uso en campañas políticas $\to$ **The Great Hack**

Cambridge Analytical ofrecia negocios a partidos politicos con la posiblidad de cambiar/manipular el comportamiento de la audiencia usando datos recolectados en encuestas, redes sociales y estudiando estos datos con modelos de comportamiento predictivos de manera que se pudiera tener un conocimiento mas amplio de la audiencia.

### Reglamentos

- **Reglamento General de Protección de Datos (GDPR)** La ley general más reciente vigente en Europa es la GDPR que significa General Data Protection Regulation que tiene por objeto regular el uso de datos de los ciudadanos europeos.

-La Ley Federal de Protección de Datos Personales en Posesión de Particulares

### Ética y deep learning: vehículos autónomos

Tesla es un vehiculo inteligente que analiza su entorno para evitar accidentes. A pesar de que la tecnologia existe hace tiempo el sistema de reconocimiento de entorno tiene vulnerabilidades en la seguridad de los datos es así que la etica prevalece aun sobre casos de tecnología actuales.

### Ética y deep learning: reconocimiento facial

Se basa en el reconocimiento de vectores en de una imagen y busca facilitar el acceso  espacios fisicos y virtuales, sin embargo el trade off involucra nuestra información biometrica a cambio de acceso. Eticamente el individuo es quien decide por lo cual si decide no entregar su información biometrica el individuo puede usar otro tipo de accesos.La línea entre la usabilidad y la invasión de la privacidad es delgada.

### Ética con datos en la pandemia

La pandemia permitio el desarrollo y ejecucion de todo tipo de controles regulatorios para evitar el crecimiento del virus lo cuales involucraban monitoreos de lugares fisicos incluso de individuos esto cambia entre paises y su nivel de inversion para la mitigación la emfermedad.

### Ética en las relaciones interpersonales

El uso de plataformas para crear reuniones Virtuales. Aplicaciones de citas que buscan segmentar perfiles de interes de un usuario. Existen aplicaciones que pueden ser gratuitas pero eso implica que nosotros somos el producto en la medida que recolectan nuestra informacion personal. Actualmente se determino que era importante heradar la administracion de las redes sociales a un familiar cercano cuando una persona passed away.


### Ética y Procesamiento de Lenguaje Natural (NLP)

Se encarga de investigar la interaccion entre las computadoras y el lenguaje humano mediante el uso de lenguas naturales. Existen 3 retos creados por Microsoft & Alibaba donde retaban a estudiantes de Stanford a medir su comprension lectora contra un algoritmo de lenguaje natural. El NPL tambien busca comunicarse diferente segun sea la edad de la persona con la que se pretende cominucar. GPT3 es un Lenguaje autoregresivo(Entiende una comprension del pasado de manera lineal) en base a datos historicos para realizar prediciones de documentos como la historia de la humanidad, medicina y tegnologia para plantear el futuro.   

### ¿Qué son las políticas públicas?

  - Se pude realizar a partir de normas, Instituciones, servicios.
  - Nacional-municipal, Educación-medio ambiente, destinatarios(jovenes-adultos),Elaboración(participativa o autoritaria), Planificación(anticipativa[acción de anticipar en el tiempo la ejecución de una cosa]-reactiva) 
  - La creación de **semaforos** se considera una politica publica puesto que busca **monitorear** y **contribuir a una necesidad social** a partir de los datos desde el **gobierno o estado**. 

### Datos y prevención de crímenes

1. Recolección de evidencia por parte de las camaras(Reactivo) video, imagenes, coordenadas geograficas sobre el tipo de crime, genero, a quien?, cuando?. Se puede crear una mapa de calor para ver por horarios cual es la distribución de crimenes en una ciudad y la tipologia de lo crimenes. 
2. Facilitar el acceso a la plataforma para interponer denuncias de manera que se puedan sugerir mas camaras en zonas donde estan ocurriendo mas crimenes. 

### Datos y salud

- El Apple Watch monitorea frecucia cardica, catidad de pasos, se basa en historicos y puede generar alertas para notificar a familiares acerca de una problema de salud
- Dipositivos para determinar que tepo de tratamiento se debe aplicar a una persona con cancer. 

### Datos y movilidad
El sector de movilidad tiene muchas singularidades. Es una sector en el cual se recolecta mucha información he identificar el flujo vehicular y busca facilitar la movilidad. Las cuidades que desarrollan este tipo de tecnonogía como singapur consideradon una smart city que recolecta data y la deja a disposicion de los cuidadanos.

- El dilema etico surge cuando se llega al punto de discriminar espacios geograficos que se consideran peligrosos o inseguras.

### Datos y Educación

Las escuelas pueden monitorear información de sus estudiantes como desempeño, horas de conexion y en general identificar patrones de comportamiento en la medida que se conectan los usuarios e interactuan con el contenido de la plataforma educativa.

### Datos y Ambiente

Identificar contaminación, fenomenos naturales, plagas, calidad del subsuelo. 
