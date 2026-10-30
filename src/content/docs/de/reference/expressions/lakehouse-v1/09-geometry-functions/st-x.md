---
title: ST_X (Lakehouse v1)
description: ST_X — gibt den Längengrad (X-Koordinate) eines durch ein GEOMETRY-Objekt dargestellten Points zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-x.md
---

Gibt den Längengrad (X-Koordinate) eines durch ein GEOMETRY-Objekt dargestellten Points zurück.

## SQL-Syntax

```sql
ST_X(<geometry>)
```

## Argumente

| Argumente    | Beschreibung                                                                            |
|--------------|-----------------------------------------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein und einen Point enthalten.         |

## Rückgabetyp

Double.

## SQL-Beispiele

```sql
SELECT
  ST_X(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_x;

┌────────────┐
│ pipeline_x │
├────────────┤
│       37.5 │
└────────────┘
```
