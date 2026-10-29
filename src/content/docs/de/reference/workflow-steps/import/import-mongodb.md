---
title: MongoDB importieren
description: Lesen Sie als Workflow-Schritt eine MongoDB-Collection oder das Ergebnis einer Aggregations-Pipeline in eine PlaidCloud-Tabelle.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-mongodb.md
---

## Beschreibung

Liest die Dokumente einer MongoDB-Collection in eine Projekttabelle, eine Zeile pro Dokument. Verwenden Sie einen Filter, um nur die benötigten Dokumente zu lesen, oder eine Aggregations-Pipeline, um sie in MongoDB umzuformen, bevor sie landen. Der Schritt erreicht MongoDB über eine [MongoDB-Verbindung](/de/reference/connectors/databases/mongodb/).

## Quelle und Ziel

| Einstellung | Erforderlich | Funktion |
| --- | --- | --- |
| MongoDB-Verbindung | Ja | Die Verbindung, über die gelesen wird. |
| Datenbank | Nein | Die zu lesende Datenbank. Lassen Sie das Feld leer, um die **Standarddatenbank** der Verbindung zu verwenden. |
| Collection | Ja | Die zu lesende Collection. |
| Zieltabelle | Ja | Die Tabelle, in der die Dokumente landen. Sie muss eine Tabelle sein, keine Ansicht. |

## Abfrage

| Einstellung | Funktion |
| --- | --- |
| Filter (JSON) | Ein MongoDB-Abfragefilter als JSON-Objekt, etwa `{"status": "open"}`. Es werden nur passende Dokumente gelesen. |
| Aggregations-Pipeline (JSON) | Eine Aggregations-Pipeline als JSON-Array, etwa `[{"$match": {"status": "open"}}]`. Wenn gesetzt, wird die Collection aggregiert statt gefiltert. Eine Pipeline mit einer `$out`- oder `$merge`-Stufe wird abgelehnt, weil sie in MongoDB schreiben würde. |
| Zeilenlimit (0 = alle) | Die höchste Anzahl zu lesender Dokumente. `0` liest alle. |
| Zeitlimit (Sekunden) | Wie lange MongoDB für das Lesen aufwenden darf, bevor es abgebrochen wird. |
| Für Spalten untersuchte Dokumente | Wenn der Schritt keine Spalten deklariert: wie viele Dokumente, vom ersten an, die Spalten und ihre Typen bestimmen – jedes darin enthaltene Feld der obersten Ebene wird zu einer Spalte. Der Standard ist 1000. |

Der Filter und die Pipeline akzeptieren Workflow-Variablen in der Schreibweise `{name}`, etwa `{"region": "{region}"}`. Der Wert jeder Variable wird als einzelne JSON-Zeichenfolge oder -Zahl eingesetzt, sodass eine Variable der Abfrage keine Schlüssel oder Operatoren hinzufügen kann. Eine nicht definierte Variable stoppt den Schritt mit einem Fehler, der sie nennt.

## Spaltenzuordnung

Ordnen Sie auf der Registerkarte „Zuordnung“ jedes Dokumentfeld einer Spalte der Zieltabelle zu. Eine Spalte liest das gleichnamige Dokumentfeld. Eine Collection, die nicht existiert, endet mit einer Warnung und lässt die Zieltabelle leer.

## Verwandte Themen

- [MongoDB exportieren](/de/reference/workflow-steps/export/export-mongodb/)
- [MongoDB-Verbindung](/de/reference/connectors/databases/mongodb/)
