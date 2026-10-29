---
title: Kroki geoprzestrzenne
description: Wszystkie geoprzestrzenne kroki przepływu pracy PlaidCloud — importuj pliki przestrzenne, twórz bufory, dopasowuj, mierz i buduj geometrię, z pełnym pokryciem narzędzi przestrzennych Alteryx.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

Kroki przepływu pracy, które odczytują, budują, przekształcają i dopasowują geometrię. Razem z
[wyrażeniami geometrii](/pl/reference/workflow-steps/spatial/spatial-sql-recipes/) obejmują
cały zestaw narzędzi przestrzennych Alteryx — zobacz
[macierz konwersji Alteryx](/pl/reference/alteryx-conversion-matrix/), aby poznać
mapowanie narzędzie po narzędziu.

## Geometria jako WKT

Każdy krok przestrzenny odczytuje i zapisuje geometrię jako **WKT** (well-known text) w
zwykłej kolumnie tekstowej. Nie trzeba deklarować specjalnego typu geometrii ani
konwertować danych między krokami: kolumna geometrii utworzona przez
[Import pliku przestrzennego](/pl/reference/workflow-steps/spatial/spatial-file-import/) jest
bezpośrednio użyteczna w [Spatial Buffer (krok)](/pl/reference/workflow-steps/spatial/spatial-buffer/),
[Dopasowanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-match/) lub wyrażeniu SQL,
w dowolnej kolejności.

## Dwie ścieżki wykonania

Każdy krok jest wykonywany najprostszą ścieżką, która daje poprawny wynik.

| Ścieżka | Co tam działa | Dlaczego |
|---|---|---|
| **SQL** — w bazie danych | Find Nearest, Match oraz [wyrażenia geometrii](/pl/reference/workflow-steps/spatial/spatial-sql-recipes/) | Złączenia predykatowe i wyrażenia kolumn skalują się wraz z tabelą; żadne wiersze nie opuszczają hurtowni danych |
| **Silnik przepływu pracy** — Shapely i GDAL | Wszystko, co zmienia kształt geometrii | Buforowania, wygładzania i rozpuszczania nie da się wyrazić w SQL bazy danych |

Nie wybierasz ścieżki samodzielnie; każdy typ kroku ma jedną. To rozróżnienie ma znaczenie
przy szacowaniu zadania: kroki ze ścieżki SQL skalują się wraz z hurtownią danych, a kroki ze ścieżki silnika
skalują się wraz z podem przepływu pracy.

## Ładowanie i zapisywanie geometrii

- [Import pliku przestrzennego](/pl/reference/workflow-steps/spatial/spatial-file-import/) — odczytaj plik MapInfo `.TAB`, ESRI `.shp`, `.kml` lub `.geojson` wraz z plikami towarzyszącymi
- [Eksport pliku przestrzennego](/pl/reference/workflow-steps/spatial/spatial-file-export/) — zapisz geometrię WKT i jej atrybuty do pliku shapefile, GeoJSON, GeoPackage, KML, GML lub MapInfo
- [Geometry in SQL (krok)](/pl/reference/workflow-steps/spatial/spatial-sql-recipes/) — buduj punkty z kolumn długości i szerokości geograficznej

## Dopasowywanie i pomiary

- [Spatial Find Nearest (krok)](/pl/reference/workflow-steps/spatial/spatial-find-nearest/) — N najbliższych wierszy jednej tabeli dla każdego wiersza innej, wraz z odległością
- [Dopasowanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-match/) — łącz w pary wiersze, których geometria przecina się, zawiera się w innej lub ją zawiera
- [Spatial Match (Intersect / Unmatched) (krok)](/pl/reference/workflow-steps/spatial/spatial-match-executor/) — to samo dopasowanie, zwracające geometrię części wspólnej lub wiersze, które nie zostały dopasowane
- [Spatial Info (krok)](/pl/reference/workflow-steps/spatial/spatial-info/) — pole powierzchni, długość, centroid i prostokąt ograniczający, mierzone geodezyjnie
- [Przekształcenie odwzorowania](/pl/reference/workflow-steps/spatial/spatial-reproject/) — przekształć geometrię z jednego układu współrzędnych odniesienia do innego

## Zmiana kształtu geometrii

- [Spatial Buffer (krok)](/pl/reference/workflow-steps/spatial/spatial-buffer/) — powiększ każdą geometrię o stałą odległość
- [Spatial Trade Area (krok)](/pl/reference/workflow-steps/spatial/spatial-trade-area/) — koncentryczne bufory o rozmiarach w rzeczywistych jednostkach
- [Spatial Generalize (krok)](/pl/reference/workflow-steps/spatial/spatial-generalize/) — uprość do zadanej tolerancji
- [Spatial Smooth (krok)](/pl/reference/workflow-steps/spatial/spatial-smooth/) — wygładzaj w zadanej liczbie przebiegów
- [Przetwarzanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-process/) — wyznacz przecięcie, sumę lub odetnij dwie kolumny geometrii

## Budowanie i rozbijanie

- [Spatial Poly-Build (krok)](/pl/reference/workflow-steps/spatial/spatial-poly-build/) — zbuduj wielokąt lub otoczkę wypukłą dla każdej grupy punktów
- [Spatial Poly-Split (krok)](/pl/reference/workflow-steps/spatial/spatial-poly-split/) — jeden wiersz na wierzchołek, wielokąt składowy lub otwór
- [Łączenie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-combine/) — rozpuść geometrie każdej grupy w jedną
- [Spatial Centroid (krok)](/pl/reference/workflow-steps/spatial/spatial-centroid/) — dodaj punkt środkowy każdej geometrii
- [Spatial Point to Line (krok)](/pl/reference/workflow-steps/spatial/spatial-point-to-line/) — połącz punkty każdej grupy w linię
- [Spatial Line to Polygon (krok)](/pl/reference/workflow-steps/spatial/spatial-line-to-polygon/) — zamknij każdą linię w wielokąt
- [Spatial Make Grid (krok)](/pl/reference/workflow-steps/spatial/spatial-make-grid/) — podziel zasięg na kwadratowe komórki

## Dokumentacja wyrażeń

- [Funkcje geometrii (Lakehouse v1)](/pl/reference/expressions/lakehouse-v1/09-geometry-functions/) — rodzina `ST_*`
- [Funkcje geografii (Lakehouse v1)](/pl/reference/expressions/lakehouse-v1/09-geo-functions/) — indeksowanie heksagonalne H3 i geohashe
- [Funkcje przestrzenne (Lakehouse v2)](/pl/reference/expressions/lakehouse-v2/17-spatial-functions/)

## Powiązane

- [Analityka geoprzestrzenna](/pl/guides/workflows/geospatial-analytics/) — przykładowa ścieżka od pliku źródłowego do opublikowanej mapy
- [Migracja przestrzennych przepływów pracy Alteryx](/pl/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map (krok)](/pl/reference/workflow-steps/reports/report-map/) — renderuj geometrię w raporcie
- [Kroki makr pakietowych](/pl/reference/workflow-steps/macros/) — Heat Map i Pie Wedge Trade Area
