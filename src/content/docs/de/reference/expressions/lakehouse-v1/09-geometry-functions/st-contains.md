---
title: ST_CONTAINS (Lakehouse v1)
description: ST_CONTAINS — gibt TRUE zurück, wenn das zweite GEOMETRY-Objekt vollständig innerhalb des ersten liegt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geometry-functions/st-contains.md
---

Gibt TRUE zurück, wenn das zweite GEOMETRY-Objekt vollständig innerhalb des ersten GEOMETRY-Objekts liegt.

## SQL-Syntax

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## Argumente

| Argumente     | Beschreibung                                                                                                      |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| `<geometry1>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein, der keine GeometryCollection ist.                          |
| `<geometry2>` | Das Argument muss ein Ausdruck vom Typ GEOMETRY sein, der keine GeometryCollection ist.                          |

:::note
- Die Funktion meldet einen Fehler, wenn die beiden eingegebenen GEOMETRY-Objekte unterschiedliche SRIDs haben.
:::

## Rückgabetyp

Boolean.

## SQL-Beispiele

```sql
SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('POLYGON((-1 0, 0 1, 1 0, -1 0))')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-1 1, 0 2, 1 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ false    │
└──────────┘

SELECT ST_CONTAINS(TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))'), TO_GEOMETRY('LINESTRING(-2 0, 0 0, 0 1)')) AS contains

┌──────────┐
│ contains │
├──────────┤
│ true     │
└──────────┘

```
