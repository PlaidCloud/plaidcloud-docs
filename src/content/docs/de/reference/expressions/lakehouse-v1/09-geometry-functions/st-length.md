---
title: ST_LENGTH (Lakehouse v1)
description: ST_LENGTH — gibt die euklidische Länge der LineStrings in einem GEOMETRY-Objekt zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-length.md
---

Gibt die euklidische Länge der LineStrings in einem GEOMETRY-Objekt zurück.

## SQL-Syntax

```sql
ST_LENGTH(<geometry>)
```

## Argumente

| Argumente    | Beschreibung                                                                          |
|--------------|---------------------------------------------------------------------------------------|
| `<geometry>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein, der LineStrings enthält.        |

:::note
- Ist `<geometry>` weder ein `LineString` noch ein `MultiLineString` noch eine `GeometryCollection`, die LineStrings enthält, wird 0 zurückgegeben.
- Ist `<geometry>` eine `GeometryCollection`, wird die Summe der Längen der LineStrings in der Collection zurückgegeben.
:::

## Rückgabetyp

Double.

## SQL-Beispiele

```sql
SELECT
  ST_LENGTH(TO_GEOMETRY('POINT(1 1)')) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘

SELECT
  ST_LENGTH(TO_GEOMETRY('LINESTRING(0 0, 1 1)')) AS length

┌─────────────┐
│    length   │
├─────────────┤
│ 1.414213562 │
└─────────────┘

SELECT
  ST_LENGTH(
    TO_GEOMETRY('POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')
  ) AS length

┌─────────┐
│  length │
├─────────┤
│       0 │
└─────────┘
```
