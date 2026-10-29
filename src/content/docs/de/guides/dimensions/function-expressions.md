---
title: Dimensionsfunktionen für Ausdrücke und Aggregationen
description: Verwenden Sie Funktionsausdrücke in PlaidCloud-Dimensionen, um berechnete Werte, bedingte Logik und dynamische Mitgliedseigenschaften zu definieren.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## Funktionen für Ausdrücke in Dimensionshierarchien

Auf dem Bildschirm „Dimensionshierarchie“ können „Aggregationen“ und „Ausdrücke“ hinzugefügt werden. Eine Beschreibung finden Sie unten.

## Aggregationen
Eine Aggregation zeigt einen aggregierten Wert aus einer Tabelle an (mögliche Funktionen: „Sum“, „Count“, „Min“ oder „Max“).
Die folgende Abbildung zeigt eine Aggregation, die so konfiguriert ist, dass sie Werte aus einer Tabelle „Line Item Values“ abruft, damit für jede „Periode“ in der Hierarchie Werte angezeigt werden können.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_1_agg.png)

Aggregationen können gefiltert werden, sodass nur Elemente angezeigt werden, die dem Filter entsprechen. In der folgenden Abbildung wurde die Aggregation so eingerichtet, dass sie Werte für ein ausgewähltes Element der Dimension „Konto“ anzeigt.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_2_agg.png)

Wenn diese Filter leer bleiben, können die Daten über die Dimensionsfilterleiste am oberen Bildschirmrand gefiltert werden, wie die folgende Abbildung zeigt:

![Dimension laden](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## Ausdrücke

Mit Ausdrücken lassen sich Werte anzeigen, die auf Grundlage der für die Dimension angezeigten Werte aus Aggregationen berechnet werden.
Ausdrücke werden aus mathematischen Formeln aufgebaut, die viele Arten von Operatoren und einige Spezialfunktionen enthalten können. Siehe die [Liste der Operatoren](https://mathjs.org/docs/expressions/syntax.html). Die verfügbaren Funktionen werden unten beschrieben.


## Funktionen
### Column(`<column_name>`)
Ruft einen Wert aus einer benannten Spalte für die aktuelle Zeile bzw. den aktuellen Knoten ab.

Unten sehen Sie ein Beispiel für einen Ausdruck, der das Ergebnis der Multiplikation des Line Item Value mit 2 anzeigt.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![Dimension laden](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

Gibt die Anzahl der Kinder der aktuellen Zeile bzw. des aktuellen Knotens zurück. Ist die aktuelle Zeile bzw. der aktuelle Knoten ein Blattelement, wird 0 zurückgegeben.

Im folgenden Beispiel wird dies verwendet, um den Durchschnittswert der untergeordneten Knoten eines übergeordneten Knotens zurückzugeben.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![Dimension laden](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
Gibt die Anzahl der im Baum gefundenen Blattelemente für die aktuelle Zeile bzw. den aktuellen Knoten zurück. Ist die aktuelle Zeile bzw. der aktuelle Knoten ein Blattelement, wird 1 zurückgegeben.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
Gibt die Gesamtzahl der im Baum gefundenen Elemente für die aktuelle Zeile bzw. den aktuellen Knoten zurück. Ist die aktuelle Zeile bzw. der aktuelle Knoten ein Blattelement, wird 0 zurückgegeben.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
Gibt die Anzahl der Geschwisterelemente der aktuellen Zeile bzw. des aktuellen Knotens zurück. Der zurückgegebene Wert schließt den aktuellen Knoten ein.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
Gibt den Wert aus einer benannten Spalte für einen benannten Knoten zurück.
Hier ein Beispiel, das den prozentualen Anteil am Gesamtwert „LIV“ für jede Zeile bzw. jeden Knoten anzeigt.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![Dimension laden](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
Gibt den Wert aus einer angegebenen Spalte für das Elternelement des aktuellen Knotens zurück.
Dieses Beispiel zeigt den prozentualen Anteil des Werts eines übergeordneten Knotens, der von einem untergeordneten Knoten verwendet wird.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![Dimension laden](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

Gibt ein numerisches Ergebnis zurück, das angibt, ob der Text in einer benannten Spalte größer als, kleiner als oder gleich einem angegebenen Wert ist.

Wenn der Text aus der Spalte dem angegebenen Text entspricht, gibt diese Funktion 0 zurück.

Wenn der Text aus der Spalte kleiner als der angegebene Text ist, gibt diese Funktion -1 zurück.

Wenn der Text aus der Spalte größer als der angegebene Text ist, gibt diese Funktion 0 zurück.


Das folgende Beispiel vergleicht den Namen der Periode mit „Jun“


![Dimension laden](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![Dimension laden](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## Bedingte Ausdrücke
Die oben gezeigten Beispiele sind recht einfach. Mit Bedingungen innerhalb von Ausdrücken lassen sich komplexere Ausdrücke erstellen.
Bedingungen in Ausdrücken haben die folgende Form:
`<condition>` ? `<value_if_true>` : `<value_if_false>`
z. B. '12 > 6 ? 1000: 0'

Durch die Kombination von Ausdrücken mit Bedingungen und Funktionen können wir komplexere Ausdrücke bauen, etwa dieses Beispiel, in dem 100.000 zu einem Line Item Value addiert werden, wenn der Monat „Jun“ ist.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![Dimension laden](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## Ein weiteres Beispiel: Einfache Umlage

Dieses Beispiel zeigt den Anteil am Line Item Value eines Elternelements, der über den Resource Driver Value für einen Blattknoten verbraucht wird.

![Dimension laden](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![Dimension laden](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## Einschränkungen:
Derzeit ist es nicht möglich, Ausdrücke zu erstellen, die auf Werten anderer Ausdrücke basieren. Ausdrücke können nur aus Werten von Aggregationen aufgebaut werden.
