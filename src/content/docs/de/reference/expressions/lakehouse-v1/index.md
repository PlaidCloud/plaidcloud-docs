---
title: Lakehouse-v1-Ausdrücke
description: Lakehouse-v1-Ausdrücke auf Basis der Databend-SQL-Funktionen mit SQLAlchemy-Verweisen über das Präfix func.
sidebar:
  label: Lakehouse v1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/index.md
---

Lakehouse v1 basiert auf der SQL-Engine [Databend](https://databend.com/). Zu jeder der unten aufgeführten Funktionen bietet diese Website Syntax und Beispiele im PlaidCloud-Stil. Die maßgebliche Upstream-Referenz (mit allen Sonderfällen und Argumentvarianten) finden Sie in der **[Databend-SQL-Funktionsreferenz](https://docs.databend.com/sql/sql-functions/)**.

## Skalare Funktionen

- [Array-Funktionen](./00-array-functions) — Array-Operationen ausführen
- [Bitweise Ausdrucksfunktionen](./01-bitmap-functions) — Bitweise Operationen und Manipulationen ausführen
- [Bedingte Ausdrucksfunktionen](./03-conditional-functions) — Bedingte Logik und Case-Anweisungen umsetzen
- [Kontextfunktionen](./15-context-functions) — Informationen zum aktuellen SQL-Ausführungskontext bereitstellen
- [Konvertierungsfunktionen](./02-conversion-functions) — Datentypen konvertieren und Werte umwandeln
- [Datums- und Zeitfunktionen](./05-datetime-functions) — Datums- und Zeitwerte bearbeiten und formatieren
- [Geodatenfunktionen](./09-geo-functions) — Geodaten verarbeiten und bearbeiten
- [Geometriefunktionen](./09-geometry-functions) — Geometriedaten von Geodaten verarbeiten und bearbeiten
- [Intervallfunktionen](./05-interval-functions) — Zeitintervalle erstellen und bearbeiten
- [Map-Funktionen](./10-map-functions) — Map-Datenstrukturen erstellen und bearbeiten
- [Numerische Funktionen](./04-numeric-functions) — Berechnungen und numerische Operationen ausführen
- [Suchfunktionen](./10-search-functions) — Werte mithilfe von Ausdrücken finden
- [Funktionen für semistrukturierte und strukturierte Daten](./10-semi-structured-functions) — Mit JSON und anderen strukturierten Datenformaten arbeiten
- [Zeichenfolgenfunktionen](./06-string-functions) — Zeichenfolgen bearbeiten und Operationen mit regulären Ausdrücken ausführen

## Aggregatfunktionen

- [Aggregatfunktionen](./07-aggregate-functions) — Zusammenfassungen wie Summe, Durchschnitt, Anzahl usw. berechnen
- [Fensterfunktionen](./08-window-functions) — Aggregatberechnungen über einen angegebenen Bereich von Zeilen bereitstellen

## KI-Funktionen

- [KI-Funktionen](./11-ai-functions) — KI- und Machine-Learning-Funktionen nutzen

## Spezialfunktionen

- [Hash-Funktionen](./12-hash-functions) — Hash-Werte für Datensicherheit und Vergleiche erzeugen
- [IP-Adressfunktionen](./14-ip-address-functions) — IP-Adressdaten bearbeiten und analysieren
- [UUID-Funktionen](./13-uuid-functions) — UUIDs erzeugen und bearbeiten

## System- und Tabellenfunktionen

- [Sequenzfunktionen](./18-sequence-functions) — Fortlaufende Werte erzeugen
- [Systemfunktionen](./16-system-functions) — Auf Informationen auf Systemebene zugreifen und Steuerungsoperationen ausführen
- [Tabellenfunktionen](./17-table-functions) — Ergebnisse in tabellarischer Form zurückgeben

## Weitere Funktionen

- [Dictionary-Funktionen](./19-dictionary-functions) — Mit Dictionary-Datenstrukturen arbeiten
- [Weitere verschiedene Funktionen](./20-other-functions) — Eine Sammlung weiterer Funktionen
- [Testfunktionen](./19-test-functions) — Funktionen für Testzwecke
