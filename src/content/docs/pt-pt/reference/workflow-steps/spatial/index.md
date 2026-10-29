---
title: Passos geoespaciais
description: Todos os passos de fluxo de trabalho geoespaciais da PlaidCloud — importar ficheiros espaciais, criar zonas-tampão, fazer correspondências, medir e construir geometria, com cobertura total das ferramentas espaciais do Alteryx.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

Passos de fluxo de trabalho que leem, constroem, transformam e comparam geometria. Em conjunto com as
[expressões de geometria](/pt-pt/reference/workflow-steps/spatial/spatial-sql-recipes/), cobrem
todo o conjunto de ferramentas espaciais do Alteryx — consulte a
[matriz de conversão do Alteryx](/pt-pt/reference/alteryx-conversion-matrix/) para o
mapeamento ferramenta a ferramenta.

## A geometria é WKT

Todos os passos espaciais leem e escrevem a geometria como **WKT** (well-known text) numa
coluna de texto vulgar. Não é preciso declarar nenhum tipo de geometria especial nem converter entre passos:
uma coluna de geometria produzida por
[Spatial File Import](/pt-pt/reference/workflow-steps/spatial/spatial-file-import/) pode ser usada
diretamente por [Spatial Buffer](/pt-pt/reference/workflow-steps/spatial/spatial-buffer/),
[Spatial Match](/pt-pt/reference/workflow-steps/spatial/spatial-match/) ou por uma expressão SQL,
por qualquer ordem.

## Duas vias de execução

Cada passo é executado pela via mais simples que dá o resultado correto.

| Via | O que é executado aí | Porquê |
|---|---|---|
| **SQL** — na base de dados | Find Nearest, Match, mais as [expressões de geometria](/pt-pt/reference/workflow-steps/spatial/spatial-sql-recipes/) | As junções por predicado e as expressões de coluna escalam com a tabela; nenhuma linha sai do armazém de dados |
| **Motor de fluxos de trabalho** — Shapely e GDAL | Tudo o que remodela geometria | Criar zonas-tampão, suavizar e dissolver não são exprimíveis em SQL de base de dados |

Não escolhe a via; cada tipo de passo tem uma só. A distinção importa quando
está a dimensionar uma tarefa: os passos da via SQL escalam com o armazém de dados e os passos da via do motor
escalam com o pod do fluxo de trabalho.

## Carregar e escrever geometria

- [Spatial File Import](/pt-pt/reference/workflow-steps/spatial/spatial-file-import/) — lê um ficheiro MapInfo `.TAB`, ESRI `.shp`, `.kml` ou `.geojson` e os respetivos ficheiros auxiliares
- [Spatial File Export](/pt-pt/reference/workflow-steps/spatial/spatial-file-export/) — escreve geometria WKT e os respetivos atributos num ficheiro shapefile, GeoJSON, GeoPackage, KML, GML ou MapInfo
- [Geometry in SQL](/pt-pt/reference/workflow-steps/spatial/spatial-sql-recipes/) — cria pontos a partir de colunas de longitude/latitude

## Corresponder e medir

- [Spatial Find Nearest](/pt-pt/reference/workflow-steps/spatial/spatial-find-nearest/) — as N linhas mais próximas de uma tabela para cada linha de outra, com a distância
- [Spatial Match](/pt-pt/reference/workflow-steps/spatial/spatial-match/) — emparelha linhas cuja geometria se interseta, está dentro ou contém
- [Spatial Match (Intersect / Unmatched)](/pt-pt/reference/workflow-steps/spatial/spatial-match-executor/) — a mesma correspondência, emitindo a geometria da sobreposição ou as linhas sem correspondência
- [Spatial Info](/pt-pt/reference/workflow-steps/spatial/spatial-info/) — área, comprimento, centroide e retângulo delimitador, medidos de forma geodésica
- [Spatial Reproject](/pt-pt/reference/workflow-steps/spatial/spatial-reproject/) — transforma geometria de um sistema de referência de coordenadas para outro

## Remodelar geometria

- [Spatial Buffer](/pt-pt/reference/workflow-steps/spatial/spatial-buffer/) — aumenta cada geometria numa distância fixa
- [Spatial Trade Area](/pt-pt/reference/workflow-steps/spatial/spatial-trade-area/) — zonas-tampão concêntricas dimensionadas em unidades do mundo real
- [Spatial Generalize](/pt-pt/reference/workflow-steps/spatial/spatial-generalize/) — simplifica até uma tolerância
- [Spatial Smooth](/pt-pt/reference/workflow-steps/spatial/spatial-smooth/) — suaviza ao longo de um número de passagens
- [Spatial Process](/pt-pt/reference/workflow-steps/spatial/spatial-process/) — interseta, une ou corta duas colunas de geometria

## Construir e decompor

- [Spatial Poly-Build](/pt-pt/reference/workflow-steps/spatial/spatial-poly-build/) — constrói um polígono ou invólucro convexo por grupo de pontos
- [Spatial Poly-Split](/pt-pt/reference/workflow-steps/spatial/spatial-poly-split/) — uma linha por vértice, polígono componente ou buraco
- [Spatial Combine](/pt-pt/reference/workflow-steps/spatial/spatial-combine/) — dissolve as geometrias de cada grupo numa só
- [Spatial Centroid](/pt-pt/reference/workflow-steps/spatial/spatial-centroid/) — adiciona o ponto central de cada geometria
- [Spatial Point to Line](/pt-pt/reference/workflow-steps/spatial/spatial-point-to-line/) — une os pontos de cada grupo numa linha
- [Spatial Line to Polygon](/pt-pt/reference/workflow-steps/spatial/spatial-line-to-polygon/) — fecha cada linha num polígono
- [Spatial Make Grid](/pt-pt/reference/workflow-steps/spatial/spatial-make-grid/) — divide uma extensão em células quadradas

## Referência de expressões

- [Funções de geometria (Lakehouse v1)](/pt-pt/reference/expressions/lakehouse-v1/09-geometry-functions/) — a família `ST_*`
- [Funções de geografia (Lakehouse v1)](/pt-pt/reference/expressions/lakehouse-v1/09-geo-functions/) — indexação hexagonal H3 e geohashes
- [Funções espaciais (Lakehouse v2)](/pt-pt/reference/expressions/lakehouse-v2/17-spatial-functions/)

## Relacionado

- [Análise geoespacial](/pt-pt/guides/workflows/geospatial-analytics/) — um percurso prático, do ficheiro de origem ao mapa publicado
- [Migrar fluxos de trabalho espaciais do Alteryx](/pt-pt/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map](/pt-pt/reference/workflow-steps/reports/report-map/) — apresenta geometria num relatório
- [Passos de macros empacotadas](/pt-pt/reference/workflow-steps/macros/) — Heat Map e Pie Wedge Trade Area
