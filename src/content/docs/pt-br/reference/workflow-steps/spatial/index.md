---
title: Etapas geoespaciais
description: Todas as etapas de fluxo de trabalho geoespaciais do PlaidCloud — importar arquivos espaciais, criar buffers, fazer correspondências, medir e construir geometrias, com cobertura completa das ferramentas espaciais do Alteryx.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

Etapas de fluxo de trabalho que leem, constroem, transformam e comparam geometrias. Junto com as
[expressões de geometria](/pt-br/reference/workflow-steps/spatial/spatial-sql-recipes/), elas
cobrem todo o conjunto de ferramentas espaciais do Alteryx — consulte a
[matriz de conversão do Alteryx](/pt-br/reference/alteryx-conversion-matrix/) para ver o
mapeamento ferramenta por ferramenta.

## A geometria é WKT

Todas as etapas espaciais leem e gravam a geometria como **WKT** (well-known text) em uma
coluna de texto comum. Não há um tipo de geometria especial a declarar nem conversão entre etapas: uma coluna de geometria produzida por
[Importar arquivo espacial](/pt-br/reference/workflow-steps/spatial/spatial-file-import/) pode ser
usada diretamente por [Spatial Buffer](/pt-br/reference/workflow-steps/spatial/spatial-buffer/),
[Correspondência espacial](/pt-br/reference/workflow-steps/spatial/spatial-match/) ou por uma
expressão SQL, em qualquer ordem.

## Duas rotas de execução

Cada etapa é executada pela rota mais simples que dá a resposta correta.

| Rota | O que é executado nela | Por quê |
|---|---|---|
| **SQL** — no banco de dados | Find Nearest, Match, além das [expressões de geometria](/pt-br/reference/workflow-steps/spatial/spatial-sql-recipes/) | Junções por predicado e expressões de coluna escalam com a tabela; nenhuma linha sai do data warehouse |
| **Mecanismo de fluxo de trabalho** — Shapely e GDAL | Tudo o que remodela geometrias | Criar buffers, suavizar e dissolver não podem ser expressos em SQL de banco de dados |

Você não escolhe a rota; cada tipo de etapa tem uma só. A diferença importa
ao dimensionar um trabalho: as etapas da rota SQL escalam com o data warehouse, e as da rota do mecanismo
escalam com o pod do fluxo de trabalho.

## Carregar e gravar geometrias

- [Importar arquivo espacial](/pt-br/reference/workflow-steps/spatial/spatial-file-import/) — lê um arquivo MapInfo `.TAB`, ESRI `.shp`, `.kml` ou `.geojson` e seus arquivos auxiliares
- [Exportação de arquivo espacial](/pt-br/reference/workflow-steps/spatial/spatial-file-export/) — grava a geometria WKT e seus atributos em um arquivo shapefile, GeoJSON, GeoPackage, KML, GML ou MapInfo
- [Geometry in SQL](/pt-br/reference/workflow-steps/spatial/spatial-sql-recipes/) — cria pontos a partir de colunas de longitude e latitude

## Correspondência e medição

- [Spatial Find Nearest](/pt-br/reference/workflow-steps/spatial/spatial-find-nearest/) — as N linhas mais próximas de uma tabela para cada linha de outra, com a distância
- [Correspondência espacial](/pt-br/reference/workflow-steps/spatial/spatial-match/) — pareia linhas cuja geometria faz interseção, está dentro ou contém
- [Spatial Match (Intersect / Unmatched)](/pt-br/reference/workflow-steps/spatial/spatial-match-executor/) — a mesma correspondência, emitindo a geometria de sobreposição ou as linhas sem correspondência
- [Spatial Info](/pt-br/reference/workflow-steps/spatial/spatial-info/) — área, comprimento, centroide e retângulo delimitador, medidos de forma geodésica
- [Reprojeção espacial](/pt-br/reference/workflow-steps/spatial/spatial-reproject/) — transforma a geometria de um sistema de referência de coordenadas para outro

## Remodelar geometrias

- [Spatial Buffer](/pt-br/reference/workflow-steps/spatial/spatial-buffer/) — expande cada geometria por uma distância fixa
- [Spatial Trade Area](/pt-br/reference/workflow-steps/spatial/spatial-trade-area/) — buffers concêntricos dimensionados em unidades do mundo real
- [Spatial Generalize](/pt-br/reference/workflow-steps/spatial/spatial-generalize/) — simplifica até uma tolerância
- [Spatial Smooth](/pt-br/reference/workflow-steps/spatial/spatial-smooth/) — suaviza ao longo de um número de passagens
- [Processo espacial](/pt-br/reference/workflow-steps/spatial/spatial-process/) — faz a interseção, a união ou o recorte de duas colunas de geometria

## Construir e dividir

- [Spatial Poly-Build](/pt-br/reference/workflow-steps/spatial/spatial-poly-build/) — constrói um polígono ou uma envoltória convexa por grupo de pontos
- [Spatial Poly-Split](/pt-br/reference/workflow-steps/spatial/spatial-poly-split/) — uma linha por vértice, polígono componente ou furo
- [Combinação espacial](/pt-br/reference/workflow-steps/spatial/spatial-combine/) — dissolve as geometrias de cada grupo em uma só
- [Spatial Centroid](/pt-br/reference/workflow-steps/spatial/spatial-centroid/) — adiciona o ponto central de cada geometria
- [Spatial Point to Line](/pt-br/reference/workflow-steps/spatial/spatial-point-to-line/) — une os pontos de cada grupo em uma linha
- [Spatial Line to Polygon](/pt-br/reference/workflow-steps/spatial/spatial-line-to-polygon/) — fecha cada linha em um polígono
- [Spatial Make Grid](/pt-br/reference/workflow-steps/spatial/spatial-make-grid/) — divide uma extensão em células quadradas

## Referência de expressões

- [Funções de geometria (Lakehouse v1)](/pt-br/reference/expressions/lakehouse-v1/09-geometry-functions/) — a família `ST_*`
- [Funções de geografia (Lakehouse v1)](/pt-br/reference/expressions/lakehouse-v1/09-geo-functions/) — indexação hexagonal H3 e geohashes
- [Funções espaciais (Lakehouse v2)](/pt-br/reference/expressions/lakehouse-v2/17-spatial-functions/)

## Relacionados

- [Análise geoespacial](/pt-br/guides/workflows/geospatial-analytics/) — um caminho completo do arquivo de origem ao mapa publicado
- [Migrar fluxos de trabalho espaciais do Alteryx](/pt-br/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map](/pt-br/reference/workflow-steps/reports/report-map/) — renderiza geometrias em um relatório
- [Etapas de macro empacotadas](/pt-br/reference/workflow-steps/macros/) — Heat Map e Pie Wedge Trade Area
