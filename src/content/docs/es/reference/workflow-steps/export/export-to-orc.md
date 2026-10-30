---
title: Export to ORC
description: Exporte tablas de proyecto de PlaidCloud a una cuenta de documentos como archivos Apache ORC, en formato columnar y con el códec de compresión que elija.
sidebar:
  order: 13.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-orc.md
---

## Descripción

Escribe tablas de proyecto en una cuenta de documentos como archivos [Apache ORC](https://orc.apache.org/), un archivo por cada tabla. ORC es un formato columnar que leen Hive, Spark y la mayoría de las plataformas de datos en la nube, y el esquema va incluido en el archivo. Combínelo con el paso [Import ORC](/es/reference/workflow-steps/import/import-orc/).

El formulario del paso tiene una página **Parámetros del archivo** para el archivo de destino, el prefijo, la compresión y lo que ocurre cuando el archivo existe, y una página **Parámetros de registro** que enumera las tablas que se exportarán, cada una con su propia selección de datos de la tabla y sus propios filtros de datos. Los [flujos de trabajo de KNIME migrados](/es/guides/workflows/migrate-knime-workflows/) usan este paso para los escritores de ORC.

## Configuración

* **Archivo de destino** (`output_file`): la cuenta de documentos y la carpeta en las que se escriben los archivos.
* **Prefijo del archivo de destino** (`file_name`): el prefijo del archivo. Cada tabla se escribe como `<prefix><table name>.orc`.
* **Opción de compresión** (`compression`): el códec de ORC que se usa dentro del archivo: **Snappy**, **zlib**, **gzip** (se escribe como `zlib`), **Zstandard** o **LZ4**. **Ninguno** escribe el archivo sin comprimir.
* **Parámetros de registro** (`frames`): las tablas que se exportarán. Cada marco lleva su propia configuración de tabla; no se lee una configuración a nivel de tabla colocada en la parte superior del paso en lugar de dentro de un marco.
  * `id`: la etiqueta de la tabla en las advertencias.
  * `source`: la tabla de proyecto que se exportará. Cada archivo recibe su nombre a partir de ella.
  * `source_columns` y `target_columns`: las columnas que se leen y las columnas que se escriben, con cualquier cambio de nombre, tipo y agregación por columna.
  * `source_where`: un filtro sobre las filas de origen.
  * `aggregate` y `aggregation_type`: resumen de las filas; `aggregation_type` es el resumen que se aplica a las columnas que no definen el suyo propio.
  * `having`: un filtro sobre las filas resumidas.
  * `distinct`: escribe solo filas distintas.
  * `use_target_slicer`, `limit_target_start` y `limit_target_end`: escriben solo las filas desde la posición inicial hasta la posición final del resultado.
  * `sort_columns`: se establece con un asistente de IA o con la API REST para ordenar las filas escritas según estas columnas de origen, empezando por la primera clave, cada una como `{source, ascending, nulls}`. No es necesario que se escriba la columna clave. `nulls` es, de forma predeterminada, `first` en orden ascendente y `last` en orden descendente. No se usa con `aggregate` ni `distinct`.
* **Un archivo que ya existe** (`if_exists`), en **Si el archivo existe**: **Sobrescribirlo** (`overwrite`, predeterminado) reemplaza un archivo que ya existe; **Hacer fallar el paso sin escribir nada** (`fail`) detiene el paso sin escribir nada cuando ya existe un archivo que se iba a escribir.

## Relacionado

- [Pasos de exportación](/es/reference/workflow-steps/export/)
- [Import ORC](/es/reference/workflow-steps/import/import-orc/)
- [Export to Parquet](/es/reference/workflow-steps/export/export-to-parquet/)
