---
title: Pasos geoespaciales
description: "Todos los pasos de flujo de trabajo geoespaciales de PlaidCloud: importar archivos espaciales, aplicar búferes, hacer coincidir, medir y construir geometrías, con cobertura completa de las herramientas espaciales de Alteryx."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

Pasos de flujo de trabajo que leen, construyen, transforman y comparan geometrías. Junto con las
[expresiones de geometría](/es/reference/workflow-steps/spatial/spatial-sql-recipes/) cubren
todo el conjunto de herramientas espaciales de Alteryx; consulte la
[matriz de conversión de Alteryx](/es/reference/alteryx-conversion-matrix/) para ver la
correspondencia herramienta por herramienta.

## La geometría es WKT

Todos los pasos espaciales leen y escriben la geometría como **WKT** (well-known text) en una
columna de texto normal. No hay ningún tipo de geometría especial que declarar ni conversión entre pasos:
una columna de geometría producida por
[Importación de archivo espacial](/es/reference/workflow-steps/spatial/spatial-file-import/) se puede
usar directamente en [Spatial Buffer (paso)](/es/reference/workflow-steps/spatial/spatial-buffer/),
[Coincidencia espacial](/es/reference/workflow-steps/spatial/spatial-match/) o en una expresión
SQL, en cualquier orden.

## Dos rutas de ejecución

Cada paso se ejecuta por la ruta más sencilla que da la respuesta correcta.

| Ruta | Qué se ejecuta allí | Por qué |
|---|---|---|
| **SQL**: en la base de datos | Find Nearest, Match, además de las [expresiones de geometría](/es/reference/workflow-steps/spatial/spatial-sql-recipes/) | Las combinaciones con predicado y las expresiones de columna escalan con la tabla; ninguna fila sale del almacén de datos |
| **Motor de flujos de trabajo**: Shapely y GDAL | Todo lo que remodela geometrías | Aplicar búferes, suavizar y disolver no se puede expresar en SQL de base de datos |

Usted no elige la ruta; cada tipo de paso tiene una. La distinción importa cuando
dimensiona un trabajo: los pasos de la ruta SQL escalan con el almacén de datos, y los pasos de la ruta del motor
escalan con el pod del flujo de trabajo.

## Cargar y escribir geometrías

- [Importación de archivo espacial](/es/reference/workflow-steps/spatial/spatial-file-import/): lee un archivo MapInfo `.TAB`, ESRI `.shp`, `.kml` o `.geojson` y sus archivos complementarios
- [Exportación de archivo espacial](/es/reference/workflow-steps/spatial/spatial-file-export/): escribe geometría WKT y sus atributos en un archivo shapefile, GeoJSON, GeoPackage, KML, GML o MapInfo
- [Geometry in SQL (paso)](/es/reference/workflow-steps/spatial/spatial-sql-recipes/): construye puntos a partir de columnas de longitud/latitud

## Coincidir y medir

- [Spatial Find Nearest (paso)](/es/reference/workflow-steps/spatial/spatial-find-nearest/): las N filas más cercanas de una tabla a cada fila de otra, con la distancia
- [Coincidencia espacial](/es/reference/workflow-steps/spatial/spatial-match/): empareja filas cuya geometría intersecta, está dentro o contiene
- [Spatial Match (Intersect / Unmatched) (paso)](/es/reference/workflow-steps/spatial/spatial-match-executor/): la misma coincidencia, que emite la geometría de superposición o las filas que no coincidieron
- [Spatial Info (paso)](/es/reference/workflow-steps/spatial/spatial-info/): área, longitud, centroide y rectángulo delimitador, medidos de forma geodésica
- [Reproyección espacial](/es/reference/workflow-steps/spatial/spatial-reproject/): transforma la geometría de un sistema de referencia de coordenadas a otro

## Remodelar geometrías

- [Spatial Buffer (paso)](/es/reference/workflow-steps/spatial/spatial-buffer/): amplía cada geometría en una distancia fija
- [Spatial Trade Area (paso)](/es/reference/workflow-steps/spatial/spatial-trade-area/): búferes concéntricos dimensionados en unidades del mundo real
- [Spatial Generalize (paso)](/es/reference/workflow-steps/spatial/spatial-generalize/): simplifica según una tolerancia
- [Spatial Smooth (paso)](/es/reference/workflow-steps/spatial/spatial-smooth/): suaviza en un número de pasadas
- [Proceso espacial](/es/reference/workflow-steps/spatial/spatial-process/): intersecta, une o recorta dos columnas de geometría

## Construir y descomponer

- [Spatial Poly-Build (paso)](/es/reference/workflow-steps/spatial/spatial-poly-build/): construye un polígono o una envolvente convexa por grupo de puntos
- [Spatial Poly-Split (paso)](/es/reference/workflow-steps/spatial/spatial-poly-split/): una fila por vértice, polígono componente o hueco
- [Combinación espacial](/es/reference/workflow-steps/spatial/spatial-combine/): disuelve las geometrías de cada grupo en una sola
- [Spatial Centroid (paso)](/es/reference/workflow-steps/spatial/spatial-centroid/): agrega el punto central de cada geometría
- [Spatial Point to Line (paso)](/es/reference/workflow-steps/spatial/spatial-point-to-line/): une los puntos de cada grupo en una línea
- [Spatial Line to Polygon (paso)](/es/reference/workflow-steps/spatial/spatial-line-to-polygon/): cierra cada línea en un polígono
- [Spatial Make Grid (paso)](/es/reference/workflow-steps/spatial/spatial-make-grid/): divide una extensión en celdas cuadradas

## Referencia de expresiones

- [Funciones de geometría (Lakehouse v1)](/es/reference/expressions/lakehouse-v1/09-geometry-functions/): la familia `ST_*`
- [Funciones de geografía (Lakehouse v1)](/es/reference/expressions/lakehouse-v1/09-geo-functions/): indexación hexagonal H3 y geohashes
- [Funciones espaciales (Lakehouse v2)](/es/reference/expressions/lakehouse-v2/17-spatial-functions/)

## Elementos relacionados

- [Análisis geoespacial](/es/guides/workflows/geospatial-analytics/): un recorrido práctico desde el archivo de origen hasta el mapa publicado
- [Migrar flujos de trabajo espaciales de Alteryx](/es/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map (paso)](/es/reference/workflow-steps/reports/report-map/): representa geometrías en un informe
- [Pasos de macro empaquetados](/es/reference/workflow-steps/macros/): Heat Map y Pie Wedge Trade Area
