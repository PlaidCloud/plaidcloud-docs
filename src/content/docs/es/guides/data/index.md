---
title: Gestión de datos - Tabular
description: Gestione datos tabulares en PlaidCloud mediante tablas, vistas y el motor Lakehouse de alto rendimiento para procesar datos a cualquier escala.
sidebar:
  label: Descripción general
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

La capa de datos de PlaidCloud se basa en **tablas** (datos estructurados en filas y columnas) y **vistas** (consultas guardadas sobre tablas). Ambas residen dentro de un proyecto y funcionan con el motor Lakehouse, que escala desde pequeñas tablas de referencia hasta conjuntos de datos analíticos de miles de millones de filas sin cambios de configuración.

## Contenido de esta sección

- [Tablas y vistas](/es/guides/data/tables-views/): qué es cada una, cuándo usar cada una y cómo interactúan
- [Explorador de tablas](/es/guides/data/table-explorer/): examine e inspeccione las tablas de su proyecto
- [Tipo de datos Currency](/es/guides/data/currency-data-type/): un tipo de columna exacto y de ancho medio para valores monetarios, y cuándo elegirlo en lugar de Numeric
- [Tipo de datos Vector](/es/guides/data/vector-data-type/): almacene incrustaciones precalculadas en una tabla de proyecto, declare el ancho esperado y busque las filas más cercanas
- [Instantáneas de tablas](/es/guides/data/table-snapshots/): examine el historial de instantáneas, vea los datos tal como estaban en una instantánea anterior y revierta o restaure una tabla
- [Publicación de datos](/es/guides/data/publish/): ponga las tablas del proyecto a disposición de paneles de control, herramientas de BI y sistemas posteriores, y consulte sus recomendaciones de rendimiento
- [Selección del registro más reciente en una tabla de historial grande](/es/guides/data/selecting-latest-record-in-large-history-table/): un patrón habitual con una solución que tiene en cuenta el rendimiento
- [API de geocodificación](/es/guides/data/geocoding-api/): migre una integración de geocodificación de Google o Mapbox a los endpoints REST de geocodificación de PlaidCloud
- [API de enrutamiento por tiempo de conducción](/es/guides/data/drive-time-routing-api/): vista previa opcional: isócronas de tiempo de conducción y clasificación por cercanía en tiempo de conducción mediante REST

## De dónde proceden los datos

Las tablas suelen rellenarse mediante **flujos de trabajo**: canalizaciones automatizadas que importan datos, los transforman y escriben los resultados de nuevo. Consulte [Flujos de trabajo](/es/guides/workflows/) para saber cómo crearlos y la [referencia de pasos de flujo de trabajo](/es/reference/workflow-steps/) para ver todos los tipos de paso que puede usar.

Para conectar sistemas externos como orígenes de datos, consulte [Conexiones (guía)](/es/guides/connections/) y [Conectores (referencia)](/es/reference/connectors/).

## Temas relacionados

- [Conceptos](/es/get-started/concepts/): cómo se relacionan las tablas con los flujos de trabajo, las dimensiones y el modelo de datos en general
- [Proyectos](/es/guides/projects/): los proyectos son propietarios de las tablas; las tablas no existen fuera de un proyecto
- [Paneles de control](/es/guides/dashboards/): consumen tablas publicadas para la visualización
