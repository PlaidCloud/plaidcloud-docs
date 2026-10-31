---
title: Étapes géospatiales
description: "Toutes les étapes de workflow géospatiales de PlaidCloud : importer des fichiers spatiaux, créer des zones tampon, mettre en correspondance, mesurer et construire des géométries, avec une couverture complète des outils spatiaux Alteryx."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

Étapes de workflow qui lisent, construisent, transforment et mettent en correspondance des géométries. Avec les
[expressions de géométrie](/fr/reference/workflow-steps/spatial/spatial-sql-recipes/), elles
couvrent l'ensemble des outils spatiaux d'Alteryx — consultez la
[matrice de conversion Alteryx](/fr/reference/alteryx-conversion-matrix/) pour la
correspondance outil par outil.

## La géométrie est en WKT

Chaque étape spatiale lit et écrit la géométrie en **WKT** (well-known text) dans une
colonne de texte ordinaire. Il n'y a aucun type géométrique spécial à déclarer et aucune
conversion entre les étapes : une colonne de géométrie produite par
[Spatial File Import](/fr/reference/workflow-steps/spatial/spatial-file-import/) est
directement utilisable par [Spatial Buffer](/fr/reference/workflow-steps/spatial/spatial-buffer/),
[Spatial Match](/fr/reference/workflow-steps/spatial/spatial-match/) ou une expression
SQL, dans n'importe quel ordre.

## Deux voies d'exécution

Chaque étape s'exécute par la voie la plus simple qui donne le bon résultat.

| Voie | Ce qui s'y exécute | Pourquoi |
|---|---|---|
| **SQL** — dans la base de données | Find Nearest, Match, ainsi que les [expressions de géométrie](/fr/reference/workflow-steps/spatial/spatial-sql-recipes/) | Les jointures par prédicat et les expressions de colonne passent à l'échelle avec la table ; aucune ligne ne quitte l'entrepôt |
| **Moteur de workflow** — Shapely et GDAL | Tout ce qui remodèle la géométrie | La création de zones tampon, le lissage et la fusion ne sont pas exprimables en SQL de base de données |

Vous ne choisissez pas la voie ; chaque type d'étape en a une seule. La distinction compte
lorsque vous dimensionnez un traitement : les étapes de la voie SQL évoluent avec l'entrepôt, celles de la voie moteur
évoluent avec le pod du workflow.

## Charger et écrire des géométries

- [Spatial File Import](/fr/reference/workflow-steps/spatial/spatial-file-import/) — lit un fichier MapInfo `.TAB`, ESRI `.shp`, `.kml` ou `.geojson` et ses fichiers associés
- [Spatial File Export](/fr/reference/workflow-steps/spatial/spatial-file-export/) — écrit la géométrie WKT et ses attributs dans un fichier shapefile, GeoJSON, GeoPackage, KML, GML ou MapInfo
- [Geometry in SQL](/fr/reference/workflow-steps/spatial/spatial-sql-recipes/) — construit des points à partir de colonnes de longitude et de latitude

## Mettre en correspondance et mesurer

- [Spatial Find Nearest](/fr/reference/workflow-steps/spatial/spatial-find-nearest/) — les N lignes d'une table les plus proches de chaque ligne d'une autre, avec la distance
- [Spatial Match](/fr/reference/workflow-steps/spatial/spatial-match/) — associe les lignes dont la géométrie se croise, est incluse ou contient
- [Spatial Match (Intersect / Unmatched)](/fr/reference/workflow-steps/spatial/spatial-match-executor/) — la même correspondance, avec émission de la géométrie de chevauchement ou des lignes sans correspondance
- [Spatial Info](/fr/reference/workflow-steps/spatial/spatial-info/) — surface, longueur, centroïde et rectangle englobant, mesurés de façon géodésique
- [Spatial Reproject](/fr/reference/workflow-steps/spatial/spatial-reproject/) — transforme une géométrie d'un système de coordonnées de référence à un autre

## Remodeler les géométries

- [Spatial Buffer](/fr/reference/workflow-steps/spatial/spatial-buffer/) — élargit chaque géométrie d'une distance fixe
- [Spatial Trade Area](/fr/reference/workflow-steps/spatial/spatial-trade-area/) — zones tampon concentriques dimensionnées en unités réelles
- [Spatial Generalize](/fr/reference/workflow-steps/spatial/spatial-generalize/) — simplifie selon une tolérance
- [Spatial Smooth](/fr/reference/workflow-steps/spatial/spatial-smooth/) — lisse sur un certain nombre de passes
- [Spatial Process](/fr/reference/workflow-steps/spatial/spatial-process/) — intersection, union ou soustraction de deux colonnes de géométrie

## Construire et décomposer

- [Spatial Poly-Build](/fr/reference/workflow-steps/spatial/spatial-poly-build/) — construit un polygone ou une enveloppe convexe par groupe de points
- [Spatial Poly-Split](/fr/reference/workflow-steps/spatial/spatial-poly-split/) — une ligne par sommet, polygone composant ou trou
- [Spatial Combine](/fr/reference/workflow-steps/spatial/spatial-combine/) — fusionne en une seule les géométries de chaque groupe
- [Spatial Centroid](/fr/reference/workflow-steps/spatial/spatial-centroid/) — ajoute le point central de chaque géométrie
- [Spatial Point to Line](/fr/reference/workflow-steps/spatial/spatial-point-to-line/) — relie les points de chaque groupe en une ligne
- [Spatial Line to Polygon](/fr/reference/workflow-steps/spatial/spatial-line-to-polygon/) — referme chaque ligne en polygone
- [Spatial Make Grid](/fr/reference/workflow-steps/spatial/spatial-make-grid/) — découpe une étendue en cellules carrées

## Référence des expressions

- [Fonctions de géométrie (Lakehouse v1)](/fr/reference/expressions/lakehouse-v1/09-geometry-functions/) — la famille `ST_*`
- [Fonctions de géographie (Lakehouse v1)](/fr/reference/expressions/lakehouse-v1/09-geo-functions/) — indexation hexagonale H3 et geohashes
- [Fonctions spatiales (Lakehouse v2)](/fr/reference/expressions/lakehouse-v2/17-spatial-functions/)

## Voir aussi

- [Analyse géospatiale](/fr/guides/workflows/geospatial-analytics/) — un parcours complet du fichier source à la carte publiée
- [Migrer des workflows Alteryx spatiaux](/fr/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map](/fr/reference/workflow-steps/reports/report-map/) — restitue la géométrie dans un rapport
- [Étapes de macros empaquetées](/fr/reference/workflow-steps/macros/) — Heat Map et Pie Wedge Trade Area
