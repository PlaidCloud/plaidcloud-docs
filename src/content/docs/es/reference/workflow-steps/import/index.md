---
title: Pasos de importación
description: Pasos de flujo de trabajo que llevan datos de orígenes externos a tablas de proyecto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

Pasos de flujo de trabajo que llevan datos de orígenes externos a tablas de proyecto.

Una importación de archivo comprueba la consulta que carga su tabla de destino antes de ejecutarse. Una consulta que contiene algo distinto de una sentencia SQL simple sobre columnas con tipo se rechaza antes de que la tabla de destino se cree, se reemplace o se cargue, de modo que la tabla queda exactamente como estaba.

Un archivo de origen ausente no es un error. La importación emite una advertencia con la ruta y deja la tabla de destino vacía con sus columnas declaradas, de modo que los pasos posteriores leen cero filas. Esto se aplica a las importaciones de CSV, Excel, JSON, ancho fijo, YXDB, dBASE, ORC, Avro, Parquet, XML y extractos de Db2. Una importación XML con etiquetas crea una tabla vacía solo para cada etiqueta que declara campos. Las importaciones de archivos comprimidos y de Access también emiten una advertencia, pero no declaran columnas, por lo que no crean ninguna tabla. Una importación de archivo comprimido que encuentra sus archivos mediante una búsqueda de documentos no emite ninguna advertencia de archivo ausente.

Lo mismo ocurre antes de que se ejecute un paso. **Rellenar** en la asignación de una importación de archivo, y la lectura de las columnas de un archivo a través de la API REST o de un asistente de IA, responden *Nada que rellenar* (una lista de columnas vacía a través de la API) con una advertencia que indica la ruta cuando el archivo no existe o está vacío, en lugar de un error. Importar un archivo ausente a una tabla o un paso nuevos desde Documentos no crea nada, marca el archivo como **omitido** y muestra una advertencia que indica la ruta.

## Pasos

- [Importar Access](/es/reference/workflow-steps/import/import-access/)
- [Importar Alteryx YXDB](/es/reference/workflow-steps/import/import-alteryx-yxdb/)
- [Importar archivo comprimido](/es/reference/workflow-steps/import/import-archive/)
- [Importar Avro](/es/reference/workflow-steps/import/import-avro/)
- [Importar CSV](/es/reference/workflow-steps/import/import-csv/)
- [Importar Delta Lake](/es/reference/workflow-steps/import/import-delta/)
- [Importar extracto de DB2](/es/reference/workflow-steps/import/import-db2-extract/)
- [Paso Import dBASE](/es/reference/workflow-steps/import/import-dbf/)
- [Importar Excel](/es/reference/workflow-steps/import/import-excel/)
- [Paso Import Delimited](/es/reference/workflow-steps/import/import-delimited/)
- [Importar tablas de bases de datos externas](/es/reference/workflow-steps/import/import-external-database-tables/)
- [Importar ancho fijo](/es/reference/workflow-steps/import/import-fixed-width/)
- [Paso Import Google Bigquery](/es/reference/workflow-steps/import/import-google-bigquery/)
- [Importar hoja de cálculo de Google](/es/reference/workflow-steps/import/import-google-spreadsheet/)
- [Paso Import HDF](/es/reference/workflow-steps/import/import-hdf/)
- [Importar JSON](/es/reference/workflow-steps/import/import-json/)
- [Importar Kafka](/es/reference/workflow-steps/import/import-kafka/)
- [Importar Monday](/es/reference/workflow-steps/import/import-monday/)
- [Importar MongoDB](/es/reference/workflow-steps/import/import-mongodb/)
- [Importar ORC](/es/reference/workflow-steps/import/import-orc/)
- [Importar Parquet](/es/reference/workflow-steps/import/import-parquet/)
- [Paso Import Project Table](/es/reference/workflow-steps/import/import-project-table/)
- [Paso Import Quandl](/es/reference/workflow-steps/import/import-quandl/)
- [Paso Import Singer Source](/es/reference/workflow-steps/import/import-singer/)
- [Paso Import SPSS](/es/reference/workflow-steps/import/import-spss/)
- [Importar SQL](/es/reference/workflow-steps/import/import-sql/)
- [Paso Import Stata](/es/reference/workflow-steps/import/import-stata/)
- [Importar XML](/es/reference/workflow-steps/import/import-xml/)
- [Restaurar tablas](/es/reference/workflow-steps/import/restore-tables/)
