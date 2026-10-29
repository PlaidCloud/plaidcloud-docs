---
title: Zahlen und andere Datentypen formatieren
description: Formatieren Sie Zahlen in PlaidCloud-Dashboards, einschließlich Währung, Prozentwerten, Dezimalstellen und benutzerdefinierten Mustern für die Zahlenanzeige.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/formatting-numbers.md
---

## Zahlen und andere Datentypen formatieren

In PlaidCloud gibt es zwei Möglichkeiten, Zahlen zu formatieren. Die eine besteht darin, die Werte direkt in den Tabellen zu transformieren. Die zweite (und gebräuchlichere) besteht darin, sie bei der Anzeige zu formatieren, damit die Werte in der Tabelle keine Genauigkeit verlieren und der Benutzer die Werte in einer übersichtlicheren, passenderen Form sieht.

Wie formatiere ich einen Wert, den ich in einem Dashboard anzeige, so, wie ich es möchte?
Der wichtigste Weg, einen Wert anzuzeigen, ist ein Diagrammobjekt in einem Dashboard. Diagramme können Tabellen, Kennzahlen (Big Numbers), Balkendiagramme und mehr sein. Jedes Diagrammobjekt hat möglicherweise eine etwas andere Stelle oder Möglichkeit, die Werte darzustellen. In Tabellen können Sie beispielsweise das Format für jede Spalte ändern, und bei einer Big Number können Sie das Format der Zahl ändern.

Um das Format zu ändern, bearbeiten Sie das Diagramm und suchen Sie das Feld `D3 FORMAT` oder `NUMBER FORMAT`. Klicken Sie bei einem Big-Number-Diagramm auf die Registerkarte `CUSTOMIZE`, dort sehen Sie `NUMBER FORMAT`. Klicken Sie bei einer Tabelle auf die Registerkarte `CUSTOMIZE`, wählen Sie unter `CUSTOMIZE COLUMN` eine Zahlenspalte (mit # dargestellt) aus, und Sie sehen das Feld `D3 FORMAT`.

Der Standardwert ist `Adaptive formatting`. Dabei wird das Format an die Werte angepasst. Wenn Sie jedoch ein festes Format möchten (z. B. $12.23 oder 12,345,678), wählen Sie das gewünschte Format aus der Dropdown-Liste oder geben Sie von Hand einen anderen Wert ein (sofern das Feld dies zulässt).

## D3-Formatierung – was ist das?

Die D3-Formatierung ist ein strukturiertes, formalisiertes Mittel, um Datenergebnisse in einem bestimmten Format darzustellen. In manchen Situationen möchten Sie beispielsweise einen großen Wert als 3B (3 Milliarden) anzeigen, im D3-Format `.3s`, oder als 3,001,238,383 im Format `,d`. Ein weiteres häufiges Beispiel ist die Entscheidung, Dollarwerte mit zwei Dezimalstellen darzustellen oder auf den nächsten Dollar zu runden: $,d oder $,.2f zeigt Dollarzeichen, Kommas, zwei Dezimalstellen und eine Festkommadarstellung.
Eine ausführlichere Einführung in D3 finden Sie auf der folgenden Website: [GitHub D3](https://github.com/d3/d3-format)


## Allgemeines D3-Format

Die allgemeine Struktur von D3 sieht wie folgt aus:

`[​[fill]align][sign][symbol][0][width][,][.precision][~][type]`

Das Füllzeichen (fill) kann ein beliebiges Zeichen sein (etwa ein Punkt, ein x oder etwas anderes). Wenn Sie ein Füllzeichen verwenden, folgt darauf ein `align`-Zeichen, das eines der folgenden sein muss:

`>` - Rechtsbündig im verfügbaren Platz. (Standardverhalten.)
`<` - Linksbündig im verfügbaren Platz.
`^` - Zentriert im verfügbaren Platz.
`=` - wie >, aber mit Vorzeichen und Symbol links von jeder Auffüllung.

Das `sign` kann sein:
`-` - leer für null oder positiv und ein Minuszeichen für negativ. (Standardverhalten.)
`+` - ein Pluszeichen für null oder positiv und ein Minuszeichen für negativ.
`(` - nichts für null oder positiv und Klammern für negativ.
(space) - ein Leerzeichen für null oder positiv und ein Minuszeichen für negativ.

Das `symbol` kann sein:
`$` - Währungssymbol anwenden.

Die Option `zero` (0) aktiviert das Auffüllen mit Nullen; dadurch wird implizit fill auf 0 und align auf = gesetzt.

Die `width` legt die Mindestfeldbreite fest; wird sie nicht angegeben, richtet sich die Breite nach dem Inhalt. Bei 8 beispielsweise ist das Feld 8 Zeichen breit.

Die Option `comma` (,) aktiviert Kommas als Trennzeichen (z. B. für Tausender).

Je nach Typ kann die `precision` entweder die Anzahl der Ziffern nach dem Dezimalzeichen angeben (Typen f und %) oder die Anzahl der signifikanten Stellen (Typen ​, g, r, s und p). Wird die Genauigkeit nicht angegeben, gilt der Standardwert 6 für alle Typen außer (none), dessen Standardwert 12 ist.

Die Option `tilde` ~ entfernt unbedeutende nachgestellte Nullen bei allen Formattypen. Sie wird meist zusammen mit den Typen r, s und % verwendet.

`types`
|Typ |   Beschreibung                                                                              |
|-----|---------------------------------------------------------------------------------------------|
|f    |Festkommadarstellung. **(häufig)**
|d    |Dezimaldarstellung, auf eine ganze Zahl gerundet. **(häufig)**
|%    |mit 100 multiplizieren und dann Dezimaldarstellung mit Prozentzeichen. **(häufig)**
|g    |entweder Dezimal- oder Exponentialdarstellung, auf signifikante Stellen gerundet.
|r    |Dezimaldarstellung, auf signifikante Stellen gerundet.
|s    |Dezimaldarstellung mit SI-Präfix, auf signifikante Stellen gerundet.
|p    |mit 100 multiplizieren, auf signifikante Stellen runden und dann Dezimaldarstellung mit Prozentzeichen.

## Beispiele
|Ausdruck|Eingabe|Ausgabe|Hinweise|
|----------|-----|------|-----|
|,d|12345.67|12,346|rundet den Wert auf die nächste ganze Zahl und fügt Kommas hinzu
|,.2f|12345.678|12,345.68|Fügt Kommas und 2 Dezimalstellen hinzu, rundet auf die zweite Dezimalstelle
|$,.2f|12345.67|$12,345.67|Fügt ein $-Symbol hinzu, hat Kommas, 2 Stellen nach dem Dezimalzeichen
|$,d|12345.67|$12,346|
|.&lt;10,|151925|151,925...|Punkte links vom Wert, 10 Zeichen breit, mit Kommas
|0>10|12345|0000012345|füllt den Wert links mit Nullen auf, 10 Zeichen breit. Das eignet sich gut, um die Breite eines Codewerts festzulegen 
|,.2%|13.215|1,321.50%|mit Kommas, 2 Stellen rechts vom Dezimalzeichen, in Prozent umgerechnet, mit %-Symbol
|x^+$16,.2f|123456|xx+$123,456.00xx| mit „x“ auffüllen, zentriert, mit Plus-/Minuszeichen, $-Symbol, 16 Zeichen breit, mit Kommas, 2 Dezimalstellen
