---
title: Lakehouse-v2-Ausdrücke
description: Lakehouse-v2-Ausdrücke auf Basis der SQL-Funktionen von StarRocks 4.1 mit SQLAlchemy-Referenzen.
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

Lakehouse v2 basiert auf [StarRocks](https://www.starrocks.io/) 4.1. Für jede der folgenden Funktionen bietet diese Website Syntax und Beispiele im PlaidCloud-Stil. Die maßgebliche Upstream-Referenz mit allen Sonderfällen und Argumentvarianten finden Sie in der **[SQL-Funktionsreferenz von StarRocks](https://docs.starrocks.io/docs/sql-reference/sql-functions/)**.

## Aggregatfunktionen

- [Aggregatfunktionen](./01-aggregate-functions) — Zusammenfassungen wie Summe, Durchschnitt und Anzahl berechnen
- [Perzentilfunktionen](./15-percentile-functions) — Perzentilwerte berechnen und Perzentilzustände verwalten

## Skalarfunktionen

- [Array-Funktionen](./02-array-functions) — Array-Operationen ausführen
- [Binärfunktionen](./03-binary-functions) — Zwischen Binär- und Zeichenfolgenformaten umwandeln
- [Bitfunktionen](./04-bit-functions) — Bitweise Operationen ausführen
- [Bitmap-Funktionen](./05-bitmap-functions) — Bitmap-Operationen und -Manipulationen ausführen
- [Bedingungsfunktionen](./06-condition-functions) — Bedingte Logik und CASE-Anweisungen umsetzen
- [Kryptografische Funktionen](./07-cryptographic-functions) — Daten ver- und entschlüsseln sowie hashen
- [Datums- und Zeitfunktionen](./08-date-time-functions) — Datums- und Zeitwerte bearbeiten und formatieren
- [Wörterbuchfunktionen](./09-dictionary-functions) — Werte in Wörterbuchtabellen nachschlagen
- [Hash-Funktionen](./10-hash-functions) — Hash-Werte mit MurmurHash und xxHash erzeugen
- [JSON-Funktionen](./11-json-functions) — JSON-Daten erstellen, abfragen und bearbeiten
- [Map-Funktionen](./12-map-functions) — Map-Datenstrukturen erstellen und bearbeiten
- [Mathematische Funktionen](./13-math-functions) — Berechnungen und numerische Operationen ausführen
- [Mustervergleichsfunktionen](./14-pattern-matching-functions) — Zeichenfolgen mit LIKE und regulären Ausdrücken abgleichen
- [Skalarfunktionen (HLL)](./16-scalar-functions) — HyperLogLog-Funktionen zur Kardinalitätsschätzung
- [Räumliche Funktionen](./17-spatial-functions) — Geodaten verarbeiten und bearbeiten
- [Zeichenfolgenfunktionen](./18-string-functions) — Zeichenfolgen bearbeiten und Textoperationen ausführen
- [Struct-Funktionen](./19-struct-functions) — Struct-Datentypen erstellen und verwenden
- [Variant-Funktionen](./22-variant-functions) — VARIANT-Datentypen abfragen und untersuchen

## Tabellenfunktionen

- [Tabellenfunktionen](./20-table-functions) — Ergebnisse in tabellarischer Form zurückgeben

## Hilfs- und Meta-Funktionen

- [Hilfsfunktionen](./21-utility-functions) — Auf Systeminformationen und Sitzungshilfen zugreifen
- [Meta-Funktionen](./23-meta-functions) — Materialisierte Ansichten, Speicher und Diagnose untersuchen

## Lakehouse verwalten

- [Lakehouse-Verwaltung](./lakehouse-management/) — Abfragen ausführen, den Katalog durchsuchen, Warehouses verwalten und die Rechenleistung überwachen
