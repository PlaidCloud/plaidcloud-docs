---
title: Geodaten-Schritte
description: Alle Geodaten-Workflow-Schritte von PlaidCloud — Geodateien importieren, puffern, abgleichen, messen und Geometrien erstellen, mit vollständiger Abdeckung der räumlichen Alteryx-Tools.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

Workflow-Schritte, die Geometrien lesen, erstellen, transformieren und abgleichen. Zusammen mit den
[Geometrieausdrücken](/de/reference/workflow-steps/spatial/spatial-sql-recipes/) decken sie das
gesamte räumliche Toolset von Alteryx ab — die Zuordnung Tool für Tool finden Sie in der
[Alteryx-Konvertierungsmatrix](/de/reference/alteryx-conversion-matrix/).

## Geometrie ist WKT

Jeder räumliche Schritt liest und schreibt Geometrie als **WKT** (Well-Known Text) in einer
gewöhnlichen Textspalte. Es gibt keinen speziellen Geometrietyp, den Sie deklarieren müssten, und keine
Konvertierung zwischen Schritten: Eine Geometriespalte, die von
[Räumlicher Dateiimport](/de/reference/workflow-steps/spatial/spatial-file-import/) erzeugt wird, ist
direkt in [Spatial Buffer (Schritt)](/de/reference/workflow-steps/spatial/spatial-buffer/),
[Räumlicher Abgleich](/de/reference/workflow-steps/spatial/spatial-match/) oder einem SQL-Ausdruck
verwendbar, in beliebiger Reihenfolge.

## Zwei Ausführungswege

Jeder Schritt läuft auf dem einfachsten Weg, der das richtige Ergebnis liefert.

| Weg | Was dort läuft | Warum |
|---|---|---|
| **SQL** — in der Datenbank | Find Nearest, Match sowie die [Geometrieausdrücke](/de/reference/workflow-steps/spatial/spatial-sql-recipes/) | Prädikat-Joins und Spaltenausdrücke skalieren mit der Tabelle; keine Zeilen verlassen das Data Warehouse |
| **Workflow-Engine** — Shapely und GDAL | Alles, was Geometrie umformt | Puffern, Glätten und Auflösen (Dissolve) lassen sich nicht in Datenbank-SQL ausdrücken |

Sie wählen den Weg nicht selbst; jeder Schrittyp hat genau einen. Der Unterschied ist wichtig,
wenn Sie einen Job dimensionieren: Schritte auf dem SQL-Weg skalieren mit dem Data Warehouse, Schritte auf dem Engine-Weg
skalieren mit dem Workflow-Pod.

## Geometrie laden und schreiben

- [Räumlicher Dateiimport](/de/reference/workflow-steps/spatial/spatial-file-import/) — liest eine MapInfo-Datei (`.TAB`), eine ESRI-Datei (`.shp`), `.kml` oder `.geojson` samt Begleitdateien
- [Geodatei-Export](/de/reference/workflow-steps/spatial/spatial-file-export/) — schreibt WKT-Geometrie und ihre Attribute in ein Shapefile, GeoJSON, GeoPackage, KML, GML oder eine MapInfo-Datei
- [Geometry in SQL](/de/reference/workflow-steps/spatial/spatial-sql-recipes/) — erstellt Punkte aus Längen- und Breitengradspalten

## Abgleichen und messen

- [Spatial Find Nearest (Schritt)](/de/reference/workflow-steps/spatial/spatial-find-nearest/) — die N nächstgelegenen Zeilen einer Tabelle zu jeder Zeile einer anderen, mit Distanz
- [Räumlicher Abgleich](/de/reference/workflow-steps/spatial/spatial-match/) — verbindet Zeilen, deren Geometrie sich schneidet, innerhalb liegt oder enthält
- [Spatial Match (Intersect / Unmatched) (Schritt)](/de/reference/workflow-steps/spatial/spatial-match-executor/) — derselbe Abgleich, gibt die Überlappungsgeometrie oder die nicht abgeglichenen Zeilen aus
- [Spatial Info (Schritt)](/de/reference/workflow-steps/spatial/spatial-info/) — Fläche, Länge, Schwerpunkt und umschließendes Rechteck, geodätisch gemessen
- [Räumlich neu projizieren](/de/reference/workflow-steps/spatial/spatial-reproject/) — transformiert Geometrie von einem Koordinatenreferenzsystem in ein anderes

## Geometrie umformen

- [Spatial Buffer (Schritt)](/de/reference/workflow-steps/spatial/spatial-buffer/) — vergrößert jede Geometrie um eine feste Distanz
- [Spatial Trade Area (Schritt)](/de/reference/workflow-steps/spatial/spatial-trade-area/) — konzentrische Puffer in realen Maßeinheiten
- [Spatial Generalize (Schritt)](/de/reference/workflow-steps/spatial/spatial-generalize/) — vereinfacht bis zu einer Toleranz
- [Spatial Smooth (Schritt)](/de/reference/workflow-steps/spatial/spatial-smooth/) — glättet über mehrere Durchläufe
- [Räumliche Verarbeitung](/de/reference/workflow-steps/spatial/spatial-process/) — schneidet, vereinigt oder schneidet zwei Geometriespalten aus

## Erstellen und zerlegen

- [Spatial Poly-Build (Schritt)](/de/reference/workflow-steps/spatial/spatial-poly-build/) — erstellt pro Punktgruppe ein Polygon oder eine konvexe Hülle
- [Spatial Poly-Split (Schritt)](/de/reference/workflow-steps/spatial/spatial-poly-split/) — eine Zeile pro Stützpunkt, Teilpolygon oder Loch
- [Räumlich kombinieren](/de/reference/workflow-steps/spatial/spatial-combine/) — löst die Geometrien jeder Gruppe zu einer auf
- [Spatial Centroid (Schritt)](/de/reference/workflow-steps/spatial/spatial-centroid/) — fügt den Mittelpunkt jeder Geometrie hinzu
- [Spatial Point to Line (Schritt)](/de/reference/workflow-steps/spatial/spatial-point-to-line/) — verbindet die Punkte jeder Gruppe zu einer Linie
- [Spatial Line to Polygon (Schritt)](/de/reference/workflow-steps/spatial/spatial-line-to-polygon/) — schließt jede Linie zu einem Polygon
- [Spatial Make Grid (Schritt)](/de/reference/workflow-steps/spatial/spatial-make-grid/) — unterteilt eine Ausdehnung in quadratische Zellen

## Ausdrucksreferenz

- [Geometriefunktionen (Lakehouse v1)](/de/reference/expressions/lakehouse-v1/09-geometry-functions/) — die `ST_*`-Familie
- [Geografiefunktionen (Lakehouse v1)](/de/reference/expressions/lakehouse-v1/09-geo-functions/) — hexagonale H3-Indizierung und Geohashes
- [Räumliche Funktionen (Lakehouse v2)](/de/reference/expressions/lakehouse-v2/17-spatial-functions/)

## Weiterführende Informationen

- [Geodaten-Analysen](/de/guides/workflows/geospatial-analytics/) — ein durchgängiges Beispiel von der Quelldatei bis zur veröffentlichten Karte
- [Räumliche Alteryx-Workflows migrieren](/de/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map (Schritt)](/de/reference/workflow-steps/reports/report-map/) — rendert Geometrie in einem Bericht
- [Gepackte Makro-Schritte](/de/reference/workflow-steps/macros/) — Heat Map und Pie Wedge Trade Area
