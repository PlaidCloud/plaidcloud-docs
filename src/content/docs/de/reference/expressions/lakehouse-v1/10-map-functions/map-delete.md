---
title: MAP_DELETE (Lakehouse v1)
description: MAP_DELETE — gibt eine vorhandene MAP zurück, aus der ein oder mehrere Schlüssel entfernt wurden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-delete.md
---

Gibt eine vorhandene MAP zurück, aus der ein oder mehrere Schlüssel entfernt wurden.

## SQL-Syntax

```sql
MAP_DELETE( <map>, <key1> [, <key2>, ... ] )
MAP_DELETE( <map>, <array> )
```

## Argumente

| Argumente | Beschreibung                                                          |
|-----------|-----------------------------------------------------------------------|
| `<map>`   | Die MAP, die den zu entfernenden KEY enthält.                         |
| `<keyN>`  | Die KEYs, die in der zurückgegebenen MAP weggelassen werden sollen.   |
| `<array>` | Das Array der KEYs, die in der zurückgegebenen MAP weggelassen werden sollen. |

:::note
- Die Typen der Schlüsselausdrücke und der Schlüssel in der Map müssen identisch sein.
- Schlüsselwerte, die in der Map nicht gefunden werden, werden ignoriert.
:::

## Rückgabetyp

Map.

## SQL-Beispiele

```sql
SELECT MAP_DELETE({'a':1,'b':2,'c':3}, 'a', 'c');
┌───────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, 'a', 'c') │
├───────────────────────────────────────────┤
│ {'b':2}                                   │
└───────────────────────────────────────────┘

SELECT MAP_DELETE({'a':1,'b':2,'c':3}, ['a', 'b']);
┌─────────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, ['a', 'b']) │
├─────────────────────────────────────────────┤
│ {'c':3}                                     │
└─────────────────────────────────────────────┘
```
