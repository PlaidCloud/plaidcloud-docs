---
title: Matriz de conversión de Alteryx
description: Cómo PlaidCloud convierte las herramientas de Alteryx en pasos de flujo de trabajo avanzado nativos, macros, variables y ejecutores administrados, con el estado de compatibilidad de cada herramienta.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

PlaidCloud convierte flujos de trabajo, aplicaciones y macros de Alteryx en flujos
de trabajo avanzados nativos. El importador asigna cada herramienta de Alteryx a un paso de flujo de trabajo, una
construcción de macro, una variable controlada, una operación de archivo respaldada por documentos o un ejecutor
de trabajos administrado, de modo que un flujo de trabajo convertido se ejecuta de forma nativa en la nube, no como una emulación.

**Casi todas las herramientas estándar de Alteryx se convierten por completo.** El estado de compatibilidad
que se muestra a continuación es por herramienta:

- **Completo**: se convierte en un paso, macro, variable, artefacto o ejecutor administrado nativo de
  PlaidCloud y ejecuta la función de la herramienta. La mayoría de las herramientas están aquí.
- **Parcial**: se convierte y se ejecuta para su uso habitual, pero un *modo de capacidad* distinto
  de la herramienta aún no se reproduce. Poco frecuente.
- **No compatible**: no hay conversión; la capacidad se reconstruye de forma nativa.

Los conectores de sistemas externos (Salesforce, HTTP, Google Analytics, Cassandra,
correo electrónico, Hadoop, Spark y similares) están **conectados, no convertidos**; consulte
[Conexión con sistemas externos](#conexión-con-sistemas-externos).

## Compatibilidad de herramientas

| Alteryx Tool | Estado | Equivalente en PlaidCloud | Qué convierte |
| --- | --- | --- | --- |
| Action | Completo | Vinculación de variables y configuración condicional de pasos | Actualiza la configuración de los pasos posteriores a partir de las entradas de aplicación convertidas. |
| Analytic App interface (`.yxwz`) | Parcial | Interfaz de Panel "App Runner" publicada | El diseño `<Questions>` de la aplicación se materializa en una aplicación Panel funcional que recopila las entradas del usuario y controla el flujo de trabajo convertido, y se publica automáticamente como parte de la conversión (una aplicación sin widgets de entrada se omite). Los tipos de pregunta habituales (texto, numérico (Numeric Up Down), fecha, casilla de verificación, botón de opción, lista desplegable, cuadro de lista, árbol, selección de archivo y selección de carpeta) se convierten en widgets de App Runner. Una pregunta cuyo valor no se vincula a ninguna variable de flujo de trabajo se muestra con una nota visible, en lugar de recopilar en silencio un valor inútil, y los tipos de pregunta menos habituales se marcan para revisión en lugar de materializarse. Consulte [Usar aplicaciones de Alteryx convertidas](/es/guides/workflows/use-converted-alteryx-apps/#la-interfaz-app-runner). |
| Append Fields | Completo | Transformación de anexar campos | Anexa campos de un flujo a otro. |
| Auto Field | Completo | Transformación de tamaño automático de campos | Conserva el tamaño de campo inferido. |
| AutoML | Completo | [ML: entrenar modelo](/es/reference/workflow-steps/machine-learning/ml-train/) | Fusiona las selecciones de método de modelo, destino y algoritmo candidato en un paso ML Train, igual que Classification y Regression. AutoML nunca registra qué algoritmo candidato ganó realmente en el momento de ejecución en Alteryx, por lo que la conversión elige el primer algoritmo marcado que ML Train admite y deja constancia de la elección. Compare un paso AutoML convertido con sus propios resultados de Alteryx. |
| Barcode | Completo | Ejecutor de códigos de barras | Lee o escribe códigos de barras en la simbología configurada. |
| Batch Macro | Parcial | Macro desplegada sobre su tabla de anclaje de control | El llamador ejecuta la macro completa una vez por cada registro de su entrada de control, vinculando en cada pasada los parámetros de control del interior, incluido un parámetro de control que el llamador renombró con una etiqueta de visualización cuando solo hay uno en juego, y una Action `UpdateRawXml` que reescribe la lista de campos de un Select a partir de una variable. Las formas cuyo valor por pasada no se puede reproducir de forma segura fallan de forma segura indicando su nombre, en lugar de convertirse incorrectamente: un `UpdateRawXml` que reescribe algo distinto de la lista de campos de un Select, y una Action que reemplaza toda la expresión de un Filter por una variable (su sintaxis sin procesar por pasada se evaluaría mal). |
| Browse | Completo | Browse / paso directo | Se conserva para inspección sin costo en tiempo de ejecución. |
| Buffer | Completo | [Spatial Buffer](/es/reference/workflow-steps/spatial/spatial-buffer/) | Hace crecer cada geometría una distancia fija. |
| Build Features | Parcial | [Build Features](/es/reference/workflow-steps/tables/table-build-features/) | Convierte primitivas aritméticas y de interacción, extracción de partes de fecha, agrupación con umbrales explícitos, escalado por puntuación z y mín-máx, y codificación one-hot. La agregación entre tablas (Deep Feature Synthesis a través de la pestaña Manage Relationships), PCA, la codificación de destino y la agrupación automática basada en datos no tienen equivalente; cada una se señala por su nombre en el informe de conversión en lugar de omitirse en silencio. |
| Calgary Cross Count | Completo | Agregado de [base de datos Calgary](/es/guides/workflows/migrate-alteryx-workflows/#bases-de-datos-calgary) | Agrupa los campos indexados y cuenta los valores con nombre de cada campo personalizado. |
| Calgary Cross Count Append | Completo | [Calgary Cross Count Append](/es/guides/workflows/migrate-alteryx-workflows/#calgary-join-y-cross-count-append) | Compara cada registro de entrada con un índice de valores y luego cuenta cuántos registros de la base de datos coincidieron. |
| Calgary Input | Completo | Entrada de [base de datos Calgary](/es/guides/workflows/migrate-alteryx-workflows/#bases-de-datos-calgary) | Lee la base de datos aplicando su consulta guardada como filtro. |
| Calgary Join | Completo | [Calgary Join](/es/guides/workflows/migrate-alteryx-workflows/#calgary-join-y-cross-count-append) | Compara cada registro con un índice de valores de la base de datos y conserva los registros que coincidieron. |
| Calgary Loader | Completo | Escritor de [base de datos Calgary](/es/guides/workflows/migrate-alteryx-workflows/#bases-de-datos-calgary) | Escribe la tabla sustituta a la que se vincula cada lector de Calgary. |
| Centroid | Completo | Operación del ejecutor Centroid | Reduce cada geometría a su punto central, anexado como una columna `Centroid`. |
| Check Box | Completo | Variable de flujo de trabajo controlada | Convierte las opciones de casilla de verificación de la aplicación en una entrada controlada. |
| Classification | Completo | [ML: entrenar modelo](/es/reference/workflow-steps/machine-learning/ml-train/) | Fusiona la cadena de Assisted Modeling en un único paso ML Train con su algoritmo, destino, características e hiperparámetros. |
| Comment / Annotation / Link | Completo | Anotación del lienzo | Se conserva como contexto del flujo de trabajo. |
| Condition | Completo | Condición de paso | Dispara advertencias, errores o bifurcaciones a partir de una expresión. |
| Control Parameter | Completo | Parámetro de control de macro | Se asigna a los parámetros de macro de PlaidCloud. |
| Convex Hull | Completo | Operación del ejecutor Convex Hull | Construye el polígono convexo más pequeño que encierra cada geometría, anexado como una columna `ConvexHull`. |
| Create Points | Completo | [Table Extract](/es/reference/workflow-steps/spatial/spatial-sql-recipes/) con `geom_point` | Construye geometría de puntos a partir de columnas de longitud/latitud, en SQL. |
| Create Samples | Completo | Table Extract, uno por salida | Divide la entrada en Estimation, Validation y Holdout con los porcentajes configurados. |
| Cross Tab | Completo | Transformación de pivote / tabulación cruzada | Convierte filas en columnas con todos los métodos de agregación y los totales derivados. |
| Data Cleansing | Completo | Transformación de limpieza de datos | Limpia espacios en blanco, valores nulos, puntuación y mayúsculas/minúsculas. |
| Date | Completo | Variable de flujo de trabajo (fecha) | Emite valores de fecha ISO para pasos y condiciones. |
| DateTime | Completo | Transformación de fecha/hora | Convierte el análisis y el formato de fecha y hora. |
| Detour | Completo | Enrutamiento de bifurcación condicional | Convierte la selección de ruta en condiciones del DAG. |
| Detour End | Completo | Combinación de bifurcaciones condicionales | Reúne las bifurcaciones seleccionadas condicionalmente. |
| Directory | Completo | Listado de directorio de documentos | Lista archivos de una ruta de documentos. |
| Distance | Completo | [Table Extract](/es/reference/workflow-steps/spatial/spatial-sql-recipes/) con `ST_DISTANCE_SPHERE` | Distancia geodésica y rumbo de punto a punto, en SQL. |
| Download | Completo | Paso [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) con una conexión REST | Descarga datos o artefactos externos; asigne una conexión REST al paso convertido antes de ejecutarlo. |
| Drop Down | Completo | Variable de flujo de trabajo controlada | Convierte las opciones de lista desplegable de la aplicación en una entrada controlada. |
| Dynamic Input | Parcial | Entrada dinámica de documentos | Resuelve patrones de archivo y entradas controladas por variables en tiempo de ejecución. Una *ReadList* de Excel (una hoja de cálculo leída de cada libro que lista una herramienta Directory y luego unida) se convierte en una lectura de hoja con comodín de carpeta cuando un Filter anterior fija la hoja a un único nombre mediante coincidencia exacta. Una hoja elegida mediante Contains, una desigualdad o un filtro OR, o una lectura que abarque más de una hoja, se rechaza en lugar de leer la hoja equivocada. |
| Dynamic Rename | Completo | Transformación de cambio de nombre dinámico | Cambia el nombre de los campos a partir de metadatos o reglas. |
| Dynamic Replace | Completo | Transformación de reemplazo dinámico | Aplica reglas de reemplazo de un segundo flujo. |
| Dynamic Select | Completo | Transformación de selección dinámica de campos | Selecciona campos por tipo, nombre o regla. |
| Error | Completo | Condición de paso (error) | Convierte el comportamiento de error configurado en condiciones de paso. |
| Feature Types | Completo | Configuración de características de [ML: entrenar modelo](/es/reference/workflow-steps/machine-learning/ml-train/) | Traslada la función de modelo asignada a cada campo al paso ML Train fusionado. |
| File Browse | Completo | Variable de archivo de documentos controlada | Permite a los usuarios elegir un archivo para una ejecución de aplicación convertida. |
| Filter | Completo | Transformación de filtro | Divide los registros por expresión en rutas verdadera y falsa. |
| Fit | Completo | [ML: entrenar modelo](/es/reference/workflow-steps/machine-learning/ml-train/) | Se integra en el paso ML Train fusionado. |
| Folder Browse | Completo | Variable de carpeta de documentos controlada | Permite a los usuarios elegir una carpeta para una ejecución de aplicación convertida. |
| Formatted Excel output into a styled template | Parcial | Escritor de Excel con plantilla ([Export to Excel Sheets](/es/reference/workflow-steps/export/export-to-excel-sheets/) para varias hojas) | Escribir en una plantilla con estilos conserva el formato de la plantilla: valores, formatos numéricos, fuentes, rellenos, bordes, celdas combinadas y anchos de columna se trasladan a la hoja y el rango indicados. Esto cubre tanto una sola hoja como varias salidas ensambladas en distintas hojas de un mismo libro, rellenadas en una sola pasada para que las hojas ya no se sobrescriban entre sí. Un caso sigue siendo parcial: una plantilla que contiene tablas dinámicas o gráficos pierde esos objetos al escribir sus hojas. La salida de Excel simple (sin estilos) es Completo; consulte Output Data. |
| Formula | Completo | Transformación de fórmula | Convierte expresiones de campo en expresiones de PlaidCloud o SQL. |
| Fuzzy Match | Completo | Ejecutor de coincidencia aproximada | Compara por claves, umbrales y revisión de candidatos. |
| Generalize | Completo | [Spatial Generalize](/es/reference/workflow-steps/spatial/spatial-generalize/) | Simplifica la geometría hasta una tolerancia, conservando la topología. |
| HTML | Completo | Texto de informe / artefacto HTML | Conserva el contenido como salida de informe o de artefacto. |
| Image Processing | Completo | Ejecutor de transformación de imágenes | Aplica escala de grises, escalado, recorte y rotación en el orden del lienzo. |
| Image Profile | Completo | Ejecutor de perfil de imagen | Informa dimensiones, modo, formato, canales y estadísticas de luminancia. |
| Image to Text | Completo | Ejecutor de OCR | Extrae texto de imágenes mediante OCR administrado. |
| Input Data | Completo | Entrada de archivo respaldada por documentos | Carga archivos de origen `.yxdb`, `.dbf`, Excel y `.flat` de ancho fijo en los datos del flujo de trabajo. |
| Insights | Completo | Salida de panel de control / artefacto | Crea un artefacto de revisión nativo de la nube. |
| Interactive Chart | Completo | Artefacto de gráfico | Crea un artefacto de gráfico a partir de los datos convertidos. |
| Join | Completo | Transformación de combinación | Produce flujos combinados, solo izquierdos y solo derechos con una clave de uno o varios campos o por posición. |
| Join Multiple | Completo | Transformación de combinación múltiple | Combina varios flujos de entrada. |
| Key/Value Pairs | Completo | [Text: NLP AI](/es/reference/workflow-steps/text-documents/nlp-ai/) (tarea keyvalue) | Extrae pares clave/valor de una columna de texto mediante el paso NLP AI respaldado por LLM, con claves candidatas opcionales y coincidencia aproximada o exacta. |
| Line To Polygon | Completo | Operación del ejecutor Line To Polygon | Cierra cada línea en un anillo de polígono, anexado como una columna `Polygon`. |
| List Box | Completo | Variable de flujo de trabajo controlada | Convierte las selecciones de lista de la aplicación en una entrada controlada. |
| Location Optimizer | Parcial | [Optimizador de ubicaciones](/es/reference/workflow-steps/optimization/location-optimizer/) | Convierte el caso lineal de minimización de distancia (elegir K sitios para minimizar la distancia total o ponderada a la demanda) en el paso nativo de MIP de p-mediana. Una puntuación de núcleo gravitacional, una macro de puntuación a medida o cualquier otro objetivo de búsqueda de candidatos sigue rechazándose; consulte [Migrar flujos de trabajo de Alteryx](/es/guides/workflows/migrate-alteryx-workflows/#macros-en-un-flujo-de-trabajo-convertido). |
| Macro calls | Completo | Invocación de macro | Importa orígenes de macro conocidos y asigna las llamadas a macro a pasos de macro de PlaidCloud. |
| Macro Input / Macro Output | Completo | Puerto de entrada / salida de macro | Se asignan directamente a los puertos de macro de PlaidCloud. |
| Make Grid | Completo | [Spatial Make Grid](/es/reference/workflow-steps/spatial/spatial-make-grid/) | Divide una extensión en celdas cuadradas, una fila por celda. |
| Map | Completo | Artefacto de mapa | Crea un artefacto de mapa de PlaidCloud. |
| Map Input | Completo | [Importación de archivo espacial](/es/reference/workflow-steps/spatial/spatial-file-import/) | Lee archivos MapInfo, ESRI, KML y GeoJSON con sus archivos complementarios. |
| Master Selector | Parcial | Variable de flujo de trabajo controlada y visibilidad condicional de pasos | Convierte las condiciones de mostrar/ocultar de la herramienta sobre los elementos de la interfaz en visibilidad condicional de pasos. Convierte el subflujo de trabajo que ejecuta la selección con el mejor esfuerzo; la validación con aplicaciones reales en el inquilino aún está pendiente, así que revise el destino de ejecución seleccionado antes de depender de él en producción. |
| Message | Completo | Condición de paso (mensaje) | Emite una advertencia, un mensaje o un error del flujo de trabajo a partir de una condición. |
| Modeling | Completo | [ML: entrenar modelo](/es/reference/workflow-steps/machine-learning/ml-train/) | Se fusiona en el paso ML Train con la elección de modelo de la canalización. |
| Multi-Field Formula | Completo | Transformación de fórmula multicampo | Aplica una fórmula a los campos seleccionados. |
| Multi-Row Formula | Completo | Transformación de fórmula de ventana / con conocimiento de filas | Convierte la lógica relativa a filas en comportamiento de ventana, particionado por Agrupar por. |
| Named Entity Recognition (NER) | Completo | [Text: NLP AI](/es/reference/workflow-steps/text-documents/nlp-ai/) (tarea ner) | Extrae entidades (personas, organizaciones, ubicaciones, fechas, cantidades o una lista de tipos personalizada) de una columna de texto mediante el paso NLP AI respaldado por LLM. |
| Numeric Up Down | Completo | Variable numérica controlada | Convierte la entrada numérica de la aplicación en una variable tipada. |
| Output Data | Completo | Salida a documentos / tablas | Escribe la salida en documentos o tablas de PlaidCloud, incluidos archivos Parquet y Avro; las salidas `.yxdb`, `.hyper` y `.dbf` se escriben como Parquet. |
| Overlay | Completo | [Proceso espacial](/es/reference/workflow-steps/spatial/spatial-process/) | Intersecta, une o recorta dos columnas de geometría. |
| PDF Input | Completo | Ejecutor de extracción de PDF | Extrae texto o tablas de PDF. |
| Point To Line | Completo | Operación del ejecutor Point To Line | Enlaza los puntos de cada grupo en una `SequenceLine` por grupo, ordenada por el campo de secuencia. |
| Poly-Build | Completo | [Spatial Poly-Build](/es/reference/workflow-steps/spatial/spatial-poly-build/) | Construye un polígono o un casco convexo por cada grupo de puntos. |
| Poly-Split | Completo | [Spatial Poly-Split](/es/reference/workflow-steps/spatial/spatial-poly-split/) | Una fila por vértice, polígono componente o agujero. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | Completo | Artefactos de informe | Convierten el contenido, el diseño y la representación de informes en salida de informe de PlaidCloud. |
| POS Tagger | Completo | [Text: NLP AI](/es/reference/workflow-steps/text-documents/nlp-ai/) (tarea pos) | Etiqueta la categoría gramatical de cada token de una columna de texto mediante el paso NLP AI respaldado por LLM. |
| Predict | Completo | [ML: puntuar](/es/reference/workflow-steps/machine-learning/ml-score/) | Puntúa los datos con la tabla del modelo entrenado y anexa una columna de predicción. |
| Radio Button | Completo | Variable de flujo de trabajo controlada | Convierte las opciones de botón de opción de la aplicación en una entrada controlada. |
| Random % Sample | Completo | Table Extract (aleatorio) | Devuelve el recuento o porcentaje exacto de registros solicitado. |
| Record ID | Completo | Transformación de identificador de fila | Agrega un identificador de registro determinista con el tipo y el valor inicial configurados, que se reinicia por grupo. |
| Redistribute | Completo | Operación del ejecutor Redistribute | Reasigna una medida de un conjunto de zonas geográficas a otro según el área de superposición, anexada como una columna `Redistributed`. |
| RegEx | Completo | Transformación de expresión regular | Analiza, compara o reemplaza texto. |
| Regression | Completo | [ML: entrenar modelo](/es/reference/workflow-steps/machine-learning/ml-train/) | Fusiona la cadena de Assisted Modeling en un único paso ML Train. |
| Report Map | Completo | Artefacto de informe de mapa | Produce un artefacto de mapa/informe nativo de la nube. |
| Run Command | Parcial | Paso [Solicitud REST](/es/reference/workflow-steps/general/rest-request/) con una conexión REST (solo `curl`/`wget`) | Convierte una línea de comandos `curl` o `wget` en un paso REST Request. Los comandos de intérprete y de script (`cscript`, PowerShell, Python y similares), la automatización de Excel-COM, las operaciones del sistema de archivos y los comandos opacos o que inician flujos de trabajo se señalan por su nombre para revisión manual en lugar de convertirse automáticamente. |
| Sample | Completo | Transformación de muestra | Conserva registros por recuento, porcentaje o agrupación. |
| Select | Completo | Paso de selección y proyección de esquema | Selecciona, renombra, reordena y cambia el tipo de los campos. |
| Smooth | Completo | [Spatial Smooth](/es/reference/workflow-steps/spatial/spatial-smooth/) | Suaviza cada geometría durante un número de pasadas. |
| Sort | Completo | Transformación de ordenación | Ordena los registros por los campos y las direcciones configurados. |
| Spatial Info | Completo | [Spatial Info](/es/reference/workflow-steps/spatial/spatial-info/) | Área, longitud, centroide y rectángulo delimitador como medidas geodésicas. |
| Spatial Match | Completo | [Coincidencia espacial](/es/reference/workflow-steps/spatial/spatial-match/) / [Spatial Match (Intersect / Unmatched)](/es/reference/workflow-steps/spatial/spatial-match-executor/) | Convierte todas las relaciones (Within, Contains, Intersects, Touches, Crosses, Overlaps y Centroid-In), comparadas en la base de datos o en el motor de flujos de trabajo. |
| Spatial Process | Completo | [Proceso espacial](/es/reference/workflow-steps/spatial/spatial-process/) | Intersecta, une o recorta columnas de geometría. |
| Summarize | Completo | Transformación de agregación | Agrupa y agrega: suma, recuento, promedio, mínimo, máximo, mediana, moda, desviación estándar, varianza y recuento de valores distintos. |
| Tab | Completo | Agrupación de pestañas de aplicación | Se conserva como estructura de la aplicación convertida. |
| Test | Completo | Condición de paso | Convierte las aserciones de prueba en condiciones de paso. |
| Text Box | Completo | Variable de texto controlada | Convierte la entrada de texto de la aplicación en una variable tipada. |
| Text Input | Completo | Entrada de tabla en línea | Crea datos en línea para el flujo de trabajo. |
| Text Pre-processing | Completo | Ejecutor de preprocesamiento de NLP | Normaliza y preprocesa texto. |
| Text Summary | Completo | [Text: NLP AI](/es/reference/workflow-steps/text-documents/nlp-ai/) (tarea summary) | Resume una columna de texto hasta un número máximo de oraciones configurado mediante el paso NLP AI respaldado por LLM. |
| Text To Columns | Completo | Transformación de división de columnas | Divide el texto en campos o filas. |
| Tile | Completo | Transformación de mosaico / agrupación | Asigna grupos de mosaico según la regla configurada. |
| Tool Container | Completo | Contenedor del lienzo / grupo de ejecución | Se conserva como organización del flujo de trabajo. |
| Topic Modeling | Completo | Ejecutor de modelado de temas | Ejecuta el modelado de temas mediante NLP administrado. |
| Transformation | Completo | Paso de transformación | Convierte la lógica de transformación en expresiones de PlaidCloud o SQL. |
| Transpose | Completo | Transformación de anulación de dinamización | Convierte columnas en filas en un par Name/Value. |
| Tree | Completo | Variable de flujo de trabajo controlada | Convierte la selección de árbol de la aplicación en una entrada controlada. |
| Union | Completo | Transformación de unión | Combina flujos por nombre, posición o reglas configuradas. |
| Unique | Completo | Transformación de separación de únicos / duplicados | Separa los primeros registros únicos de los duplicados. |
| Visual Layout | Completo | Metadatos de diseño del lienzo | Se conserva como contexto de diseño. |
| Word Cloud | Completo | Artefacto de visualización de texto | Crea un artefacto de visualización a partir del análisis de texto. |
| XML Parse | Completo | Transformación de análisis de XML | Extrae campos XML a los datos del flujo de trabajo. |
| Zero-shot Text Classification | Completo | [Text: NLP AI](/es/reference/workflow-steps/text-documents/nlp-ai/) (tarea zeroshot) | Clasifica una columna de texto frente a una lista de etiquetas candidatas por fila, de una o varias etiquetas, mediante el paso NLP AI respaldado por LLM. |
| Find Nearest | Completo | [Spatial Find Nearest](/es/reference/workflow-steps/spatial/spatial-find-nearest/) | Combinación de vecino más cercano ordenada por distancia: en línea recta y por tiempo de conducción (ordenada por minutos en una red viaria) mediante el motor de enrutamiento autoalojado de PlaidCloud. El tiempo de conducción se habilita por espacio de trabajo. |
| Trade Area | Completo | [Spatial Trade Area](/es/reference/workflow-steps/spatial/spatial-trade-area/) | Áreas de influencia concéntricas dimensionadas en unidades del mundo real: de radio fijo y por tiempo de conducción (minutos en una red viaria) mediante el motor de enrutamiento autoalojado. El tiempo de conducción se habilita por espacio de trabajo. |
| Image Template | Completo | Operación del ejecutor Image Template | El modo manual recorta la imagen en cada región que dibuje sobre la plantilla. El modo automático detecta por usted las regiones de la página con un modelo de diseño de estándar abierto y emite una fila por región, cada una con sus límites detectados y su confianza para revisión; una página que el modelo no puede leer con confianza se señala por su nombre en lugar de recortarse. La detección de estándar abierto puede diferir de la propia de Alteryx: revise las regiones detectadas o use el modo manual para un control exacto. |
| Image Recognition | Completo | Ejecutor de reconocimiento de imágenes | Entrena un clasificador de imágenes en el flujo de trabajo y puntúa imágenes nuevas con él, en el mismo lugar: sin cuenta externa y sin que ningún dato salga de PlaidCloud. El clasificador se vuelve a entrenar en lugar de copiarse de Alteryx, por lo que los resultados son una aproximación fiel y no una coincidencia exacta bit a bit, y el entrenamiento se ejecuta en CPU. Se habilita por espacio de trabajo. |
| Geocoder | Completo | Geocodificador autoalojado | Geocodifica direcciones a coordenadas y geocodifica de forma inversa coordenadas a direcciones con el propio geocodificador de PlaidCloud: sin cuenta externa y sin que ningún dato salga de PlaidCloud. Se habilita por espacio de trabajo. |

Los widgets de interfaz (listas desplegables, cuadros de lista, casillas de verificación,
entradas de texto/numéricas/de fecha, selectores de archivos y carpetas), los objetos del lienzo (comentarios, vínculos,
contenedores) y los puertos de macro se convierten, todos ellos, en variables controladas o
objetos de lienzo nativos. El diseño completo de la interfaz de una aplicación de Alteryx, es decir, la definición
`<Questions>` del archivo `.yxwz`, también se materializa en una interfaz de Panel "App
Runner" publicada, de modo que convertir la aplicación produce un formulario de entrada funcional
que recopila los mismos valores y controla el flujo de trabajo convertido, y no solo las
variables controladas individuales. Consulte la fila Analytic App interface anterior y
[Usar aplicaciones de Alteryx convertidas](/es/guides/workflows/use-converted-alteryx-apps/#la-interfaz-app-runner).

**Una nota sobre la salida de Excel.** Un libro nuevo simple, con los datos escritos con el
formato predeterminado, se convierte por completo. Escribir en una *plantilla con estilos*, rellenando hojas
y rangos con nombre y conservando su formato, se convierte para una sola
hoja y para varias salidas ensambladas en distintas hojas de un mismo libro
(el paso [Export to Excel Sheets](/es/reference/workflow-steps/export/export-to-excel-sheets/)
rellena todas las hojas en una sola pasada). Las plantillas que contienen tablas dinámicas o gráficos
pierden esos objetos cuando se escriben sus hojas; las manipulaciones de archivo a nivel de hoja controladas
desde Run Command (Excel COM/VBS) se señalan por su nombre para revisión manual en lugar de
convertirse automáticamente.

## Cobertura de herramientas espaciales

Toda herramienta de la paleta **Spatial** de Alteryx tiene una ruta en PlaidCloud, y cada
una de esas rutas es un paso que también puede crear a mano: la conversión es una
comodidad, no la única vía de entrada. Consulte los [pasos geoespaciales](/es/reference/workflow-steps/spatial/)
para la referencia completa y [Análisis geoespacial](/es/guides/workflows/geospatial-analytics/)
para ver cómo encajan entre sí.

| Alteryx Spatial Tool | Ruta en PlaidCloud | Se ejecuta en |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/es/reference/workflow-steps/spatial/spatial-buffer/) | Motor de flujos de trabajo |
| Centroid | Operación del ejecutor Centroid | Motor de flujos de trabajo |
| Convex Hull | Operación del ejecutor Convex Hull | Motor de flujos de trabajo |
| Create Points | [Expresión de Table Extract](/es/reference/workflow-steps/spatial/spatial-sql-recipes/) | Base de datos |
| Distance | [Expresión de Table Extract](/es/reference/workflow-steps/spatial/spatial-sql-recipes/) | Base de datos |
| Find Nearest | [Spatial Find Nearest](/es/reference/workflow-steps/spatial/spatial-find-nearest/) | Base de datos; servicio de enrutamiento para el tiempo de conducción |
| Generalize | [Spatial Generalize](/es/reference/workflow-steps/spatial/spatial-generalize/) | Motor de flujos de trabajo |
| Heat Map | [Heat Map (macro)](/es/reference/workflow-steps/macros/macro-heat-map/) | Motor de flujos de trabajo |
| Line To Polygon | Operación del ejecutor Line To Polygon | Motor de flujos de trabajo |
| Make Grid | [Spatial Make Grid](/es/reference/workflow-steps/spatial/spatial-make-grid/) | Motor de flujos de trabajo |
| Point To Line | Operación del ejecutor Point To Line | Motor de flujos de trabajo |
| Poly-Build | [Spatial Poly-Build](/es/reference/workflow-steps/spatial/spatial-poly-build/) | Motor de flujos de trabajo |
| Poly-Split | [Spatial Poly-Split](/es/reference/workflow-steps/spatial/spatial-poly-split/) | Motor de flujos de trabajo |
| Redistribute | Operación del ejecutor Redistribute | Motor de flujos de trabajo |
| Smooth | [Spatial Smooth](/es/reference/workflow-steps/spatial/spatial-smooth/) | Motor de flujos de trabajo |
| Spatial Info | [Spatial Info](/es/reference/workflow-steps/spatial/spatial-info/) | Motor de flujos de trabajo |
| Spatial Match | [Coincidencia espacial](/es/reference/workflow-steps/spatial/spatial-match/) | Base de datos |
| Spatial Match — intersection object, Unmatched | [Spatial Match (Intersect / Unmatched)](/es/reference/workflow-steps/spatial/spatial-match-executor/) | Motor de flujos de trabajo |
| Spatial Process | [Proceso espacial](/es/reference/workflow-steps/spatial/spatial-process/) | Motor de flujos de trabajo |
| Trade Area (fixed-radius + drive-time) | [Spatial Trade Area](/es/reference/workflow-steps/spatial/spatial-trade-area/) | Motor de flujos de trabajo; servicio de enrutamiento para el tiempo de conducción |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/es/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Motor de flujos de trabajo |
| Spatial file input | [Importación de archivo espacial](/es/reference/workflow-steps/spatial/spatial-file-import/) | Motor de flujos de trabajo |
| Summarize — SpatialObjCombine, SpatialObjConvexHull | [Combinación espacial](/es/reference/workflow-steps/spatial/spatial-combine/) | Motor de flujos de trabajo |
| Report Map | [Report Map](/es/reference/workflow-steps/reports/report-map/) | Motor de flujos de trabajo |

**Áreas de influencia y vecino más cercano por tiempo de conducción**: los anillos de tiempo de conducción de Trade Area y la
clasificación por tiempo de conducción de Find Nearest se ejecutan en el motor de enrutamiento autoalojado de PlaidCloud
(isócronas de la red viaria y matrices de tiempo de viaje), no en una API alojada de
terceros, por lo que las coordenadas de origen nunca salen de la plataforma. El tiempo de conducción se habilita por
espacio de trabajo. El enrutamiento y las áreas de tiempo de conducción usan datos de OpenStreetMap:
© colaboradores de OpenStreetMap, disponibles bajo la [Open Database License
(ODbL)](https://www.openstreetmap.org/copyright).

### Requisitos previos espaciales conocidos

Las propias herramientas espaciales se convierten; estos son requisitos previos de la entrada.

- **El formato de GeoFile `.geo`.** El GeoFile binario propietario de Alteryx no tiene
  lector abierto, por lo que su importación falla de forma segura en lugar de bloquearse en tiempo de
  ejecución. En Alteryx, vuelva a exportar la capa a un formato espacial estándar
  (shapefile o GeoJSON) e impórtela en su lugar; los demás formatos espaciales no se
  ven afectados. Consulte
  [Migrar flujos de trabajo espaciales de Alteryx](/es/guides/workflows/migrate-spatial-alteryx-workflows/#empaquetar-las-entradas-espaciales).
- **La medida de clave Peano de Spatial Info.** La clave Peano es un índice espacial propietario de Alteryx
  sin especificación pública, por lo que un Spatial Info que la solicite
  omite esa columna y lo indica en una nota. Todas las demás medidas de Spatial Info
  (área, longitud, centroide, rectángulo delimitador, tipo de objeto, recuentos de partes y puntos,
  y puntos finales) se convierten.
- **Coordenadas proyectadas de Create Points.** Create Points convierte directamente
  coordenadas de lon/lat de punto flotante y enteras (×1.000.000).
  Las coordenadas que ya están en un sistema proyectado deben reproyectarse antes a lon/lat WGS84,
  porque el flujo de trabajo no registra qué proyección usan.

## Cobertura de herramientas de Calgary

Una base de datos Calgary (`.cydb`) de Alteryx es un almacén indexado propietario que PlaidCloud no puede abrir. La conversión trata cada una como el equivalente de una tabla ordinaria de PlaidCloud, llamada `calgary_<database name>`, de modo que las herramientas creadas a su alrededor se convierten en operaciones de tabla ordinarias en lugar de rechazarse sin más. Consulte [Bases de datos Calgary](/es/guides/workflows/migrate-alteryx-workflows/#bases-de-datos-calgary) para saber cómo funciona la tabla sustituta, y [Calgary Join y Cross Count Append](/es/guides/workflows/migrate-alteryx-workflows/#calgary-join-y-cross-count-append) para las herramientas de coincidencia de índices.

| Alteryx Calgary Tool | Ruta en PlaidCloud | ¿Se convierte? |
| --- | --- | --- |
| Calgary Loader | Table Extract que escribe `calgary_<database>` | Sí, una vez que la base de datos tiene nombre y almacena al menos un campo de datos. |
| Calgary Input | Entrada dinámica de documentos que lee `calgary_<database>`, con la consulta guardada como filtro | Sí, incluida una consulta construida con un Or o envuelta en un Not, y un filtro contains o starts-with (reconstruido como un SQL LIKE). Se rechaza ante una consulta de búsqueda espacial y ante límites de Skip Records/Max Records. |
| Calgary Input (Count Only) / Calgary Cross Count | Transformación de agregación sobre `calgary_<database>` | Sí, incluido un grupo construido con un Or o envuelto en un Not. Se rechaza ante un cruce de más de un campo personalizado y ante una lectura de solo recuento que no nombra ninguna columna sobre la que contar. |
| Calgary Join | Entrada dinámica de documentos que compara cada registro de su entrada con `calgary_<database>` | Cuando el campo entrante es un valor simple comparado con un índice de valores, incluido el modo Count Only, que cuenta los registros de la base de datos con los que coincidió cada registro de entrada, y un registro sin coincidencias cuenta cero. Se rechaza cuando el campo es espacial (reconstruya como Spatial Match) o su tipo no está resuelto, ante Joins de índice de rango o con la salida de no coincidentes conectada, ante un Join que no nombra ningún campo de coincidencia y ante un Join sin nada conectado a su entrada. |
| Calgary Cross Count Append | Entrada dinámica de documentos que compara cada registro, y luego una combinación con recuento sobre `calgary_<database>` | Cuando el campo entrante es un valor simple comparado con un índice de valores: cuenta, por cada registro de entrada, los registros de la base de datos con los que coincidió, y un registro sin coincidencias cuenta cero. Se rechaza ante un índice espacial o no resuelto (reconstruya como Spatial Match), una cuadrícula de recuento cruzado de valores personalizados, un índice de rango y una coincidencia que no nombra ningún campo. |

### Requisitos previos de Calgary conocidos

La mayoría de estos son requisitos previos de la entrada y no límites de la conversión.

- **Una coincidencia con un índice espacial debe reconstruirse como Spatial Match.** Un Calgary Join o Cross Count Append comparado con un índice espacial se rechaza e indica la tabla sustituta: el flujo de trabajo registra el nombre del índice pero no si contiene valores ordinarios o geometría espacial, y una coincidencia de valores (una combinación por igualdad) y una coincidencia espacial (punto en polígono) son operaciones distintas. Exporte la base de datos a una tabla y reconstruya la coincidencia como un Join (índice de valores) o un Spatial Match (índice espacial).
- **Una lectura limitada por Skip Records o Max Records necesita un orden explícito.** La tabla sustituta exportada no conserva el orden de los registros, así que agregue una columna de orden al exportar si necesita tomar los primeros o los últimos N registros por posición.
- **Una base de datos demográfica o de referencia debe cargarse primero.** Una lectura de Calgary antes de que se haya cargado su base de datos se detiene e indica la tabla que debe crearse. El propio archivo `.cydb` no tiene lector abierto, así que vuelva a exportarlo en Alteryx (un Calgary Input hacia una herramienta Output Data que escriba CSV o Parquet) e impórtelo como la tabla indicada; consulte [Bases de datos .cydb (Calgary) ilegibles](/es/guides/workflows/troubleshoot-alteryx-imports/#bases-de-datos-cydb-calgary-ilegibles). Este es el caso habitual de los archivos `.cydb` demográficos y de referencia con licencia que distribuye Alteryx (Experian, Census y similares): ningún convertidor puede reproducir esos datos de terceros, así que aporte sus propios datos de referencia con licencia y cárguelos en la tabla indicada, igual que con los datos de referencia de Geocoder.
- **Un Calgary Loader que no almacena ningún campo de datos no se convierte**, porque la tabla que escribiera no tendría columnas.
- **Una cuadrícula de recuento cruzado de valores personalizados aún no se convierte.** Un único campo de recuento cruzado simple se convierte (cuenta, por cada registro de entrada, los registros coincidentes de la base de datos), pero una cuadrícula de valores personalizados *con nombre* anexaría una columna de recuento por valor, y Alteryx no documenta cuántas columnas son ni cómo se llaman. Está previsto para una versión futura, a la espera de una exportación de referencia para aplicar ingeniería inversa al contrato de columnas.

Las consultas de valor, rango, contains y starts-with se convierten todas en un filtro; solo una consulta de búsqueda espacial, una operación de índice sin equivalente a nivel de columna, no se convierte.

## Conexión con sistemas externos

Los endpoints de conectores de Alteryx (Salesforce, HTTP, Google Analytics, Cassandra,
correo electrónico, Hadoop y Spark, en ambas direcciones) no se convierten, porque
PlaidCloud accede a estos sistemas mediante una conexión y no mediante una
herramienta en el lienzo. Cada uno se rechaza indicando su nombre y señala dónde
corresponde el trabajo:

| Alteryx Tool | Dónde va en PlaidCloud |
| --- | --- |
| Salesforce Input / Output | Una conexión **Salesforce** |
| Anaplan | Una conexión **Anaplan** |
| HTTP Input | Un paso **Solicitud REST** con una conexión **REST** |
| Google Analytics Input | **Importar: origen Singer** con el tap de Google Analytics |
| Cassandra Input | **Importar: origen Singer** con el tap de Cassandra |
| Email Input | **Importar: origen Singer** con el tap de GMail |
| Hadoop Input / Output | **Importar: SQL** / **Exportar: SQL** mediante una conexión de Hive, Impala o Presto |
| Spark Input / Output | **Importar: SQL** / **Exportar: SQL** mediante una conexión de Databricks |

Cuatro de ellos no tienen ninguna vía de escritura. PlaidCloud lee Google Analytics
y Cassandra pero nunca escribe en ellos, por lo que una herramienta Google Analytics Output o
Cassandra Output se convierte en un **Exportar: SQL** hacia un destino compatible.
El correo electrónico tampoco es un destino de datos: **Notificar: correo electrónico** envía una
notificación a personas, por lo que una herramienta Email Output se convierte en un paso de exportación más una
notificación aparte. La conexión **Anaplan** es de solo lectura del mismo
modo: lee una vista guardada, ejecuta una acción de exportación preexistente o carga
listas en una dimensión de PlaidCloud, pero no existe ningún paso de PlaidCloud que
escriba de vuelta en Anaplan.

## Validación de un flujo de trabajo convertido

Para los flujos de trabajo de producción, valide las salidas convertidas con salidas de Alteryx
de confianza: la validación de PlaidCloud se centra en el esquema, el recuento de filas y los valores de las filas,
y omite el orden de las filas a menos que el flujo de trabajo dependa de él. Las operaciones
especializadas (espaciales, coincidencia aproximada, OCR, NLP, informes) se ejecutan mediante ejecutores de
trabajos administrados que mantienen el flujo de trabajo nativo de la nube; las canalizaciones de aprendizaje automático
se convierten en los pasos nativos [ML: entrenar modelo](/es/reference/workflow-steps/machine-learning/ml-train/)
y [ML: puntuar](/es/reference/workflow-steps/machine-learning/ml-score/).
Consulte [Migrar flujos de trabajo de Alteryx](/es/guides/workflows/migrate-alteryx-workflows/)
para la guía completa de importación y validación.
