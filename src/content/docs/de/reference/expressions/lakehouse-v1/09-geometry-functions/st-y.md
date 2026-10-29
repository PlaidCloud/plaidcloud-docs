---
title: ST_Y (Lakehouse v1)
description: ST_Y — gibt den Breitengrad (Y-Koordinate) eines durch ein GEOMETRY-Objekt dargestellten Points zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-y.md
---

Gibt den Breitengrad (Y-Koordinate) eines durch ein GEOMETRY-Objekt dargestellten Points zurück.

## SQL-Syntax

```sql
ST_Y(<geometry>)
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
  ST_Y(
    ST_MAKEGEOMPOINT(
      37.5, 45.5
    )
  ) AS pipeline_y;

┌────────────┐
│ pipeline_y │
├────────────┤
│       45.5 │
└────────────┘
```
