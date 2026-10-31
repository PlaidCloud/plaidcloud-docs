---
title: ST_DISTANCE (Lakehouse v1)
description: ST_DISTANCE — gibt den minimalen euklidischen Abstand zwischen zwei GEOMETRY-Objekten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-distance.md
---

Gibt den minimalen [euklidischen Abstand](https://en.wikipedia.org/wiki/Euclidean_distance) zwischen zwei GEOMETRY-Objekten zurück.

## SQL-Syntax

```sql
ST_DISTANCE(<geometry1>, <geometry2>)
```

## Argumente

| Argumente     | Beschreibung                                                                                      |
|---------------|---------------------------------------------------------------------------------------------------|
| `<geometry1>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein und einen Point enthalten.                   |
| `<geometry2>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein und einen Point enthalten.                   |

:::note
- Gibt NULL zurück, wenn ein oder mehrere eingegebene Punkte NULL sind.
- Die Funktion meldet einen Fehler, wenn die beiden eingegebenen GEOMETRY-Objekte unterschiedliche SRIDs haben.
:::

## Rückgabetyp

Double.

## SQL-Beispiele

```sql
SELECT
  ST_DISTANCE(
    TO_GEOMETRY('POINT(0 0)'),
    TO_GEOMETRY('POINT(1 1)')
  ) AS distance

┌─────────────┐
│   distance  │
├─────────────┤
│ 1.414213562 │
└─────────────┘
```
