---
title: JQ (Lakehouse v1)
description: JQ — Die Funktion JQ ist eine mengenliefernde SQL-Funktion, mit der Sie jq anwenden können.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/jq.md
---

Die Funktion JQ ist eine mengenliefernde SQL-Funktion, mit der Sie [jq](https://jqlang.github.io/jq/)-Filter auf JSON-Daten in Variant-Spalten anwenden können. Damit verarbeiten Sie JSON-Daten, indem Sie einen angegebenen jq-Filter anwenden und die Ergebnisse als Menge von Zeilen zurückgeben.

## SQL Syntax

```sql
JQ (<jq_expression>, <json_data>)
```

| Parameter       | Beschreibung |
|-----------------|--------------|
| `jq_expression` | Ein `jq`-Filterausdruck, der mit der `jq`-Syntax festlegt, wie JSON-Daten verarbeitet und umgewandelt werden. Der Ausdruck kann angeben, wie Daten in JSON-Objekten und -Arrays ausgewählt, geändert und bearbeitet werden. Informationen zu Syntax, Filtern und Funktionen, die jq unterstützt, finden Sie im [jq-Handbuch](https://jqlang.github.io/jq/manual/#basic-filters). |
| `json_data`     | Die JSON-formatierte Eingabe, die Sie mit dem `jq`-Filterausdruck verarbeiten oder umwandeln möchten. Es kann ein JSON-Objekt, ein Array oder eine beliebige gültige JSON-Datenstruktur sein. |

## Return Type

Die Funktion JQ gibt eine Menge von JSON-Werten zurück. Jeder Wert entspricht einem Element des umgewandelten oder extrahierten Ergebnisses auf Basis von `<jq_expression>`.

## SQL Examples

Zunächst erstellen wir eine Tabelle namens `customer_data` mit den Spalten `id` und `profile`, wobei `profile` ein JSON-Typ zum Speichern von Benutzerinformationen ist:

```sql
CREATE TABLE customer_data (
    id INT,
    profile JSON
);

INSERT INTO customer_data VALUES
    (1, '{"name": "Alice", "age": 30, "city": "New York"}'),
    (2, '{"name": "Bob", "age": 25, "city": "Los Angeles"}'),
    (3, '{"name": "Charlie", "age": 35, "city": "Chicago"}');
```

Dieses Beispiel extrahiert bestimmte Felder aus den JSON-Daten:

```sql
SELECT
    id,
    jq('.name', profile) AS customer_name
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   customer_name   │
├─────────────────┼───────────────────┤
│               1 │ "Alice"           │
│               2 │ "Bob"             │
│               3 │ "Charlie"         │
└─────────────────────────────────────┘
```

Dieses Beispiel wählt die Benutzer-ID und das um 1 erhöhte Alter jedes Benutzers aus:

```sql
SELECT
    id,
    jq('.age + 1', profile) AS updated_age
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │    updated_age    │
├─────────────────┼───────────────────┤
│               1 │ 31                │
│               2 │ 26                │
│               3 │ 36                │
└─────────────────────────────────────┘
```

Dieses Beispiel wandelt Städtenamen in Großbuchstaben um:

```sql
SELECT
    id,
    jq('.city | ascii_upcase', profile) AS city_uppercase
FROM
    customer_data;

┌─────────────────────────────────────┐
│        id       │   city_uppercase  │
├─────────────────┼───────────────────┤
│               1 │ "NEW YORK"        │
│               2 │ "LOS ANGELES"     │
│               3 │ "CHICAGO"         │
└─────────────────────────────────────┘
```
