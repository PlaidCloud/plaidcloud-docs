---
title: MAP_PICK (Lakehouse v1)
description: MAP_PICK — gibt eine neue MAP zurück, die die angegebenen Schlüssel-Wert-Paare einer vorhandenen MAP enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-pick.md
---

Gibt eine neue MAP zurück, die die angegebenen Schlüssel-Wert-Paare einer vorhandenen MAP enthält.

## SQL-Syntax

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## Argumente

| Argumente | Beschreibung                                                              |
|-----------|---------------------------------------------------------------------------|
| `<map>`   | Die Eingabe-MAP.                                                          |
| `<keyN>`  | Die KEYs, die in der zurückgegebenen MAP enthalten sein sollen.           |
| `<array>` | Das Array der KEYs, die in der zurückgegebenen MAP enthalten sein sollen. |

:::note
- Die Typen der Schlüsselausdrücke und der Schlüssel in der Map müssen identisch sein.
- Schlüsselwerte, die in der Map nicht gefunden werden, werden ignoriert.
:::

## Rückgabetyp

Map.

## SQL-Beispiele

```sql
SELECT MAP_PICK({'a':1,'b':2,'c':3}, 'a', 'c');
┌─────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, 'a', 'c') │
├─────────────────────────────────────────┤
│ {'a':1,'c':3}                           │
└─────────────────────────────────────────┘

SELECT MAP_PICK({'a':1,'b':2,'c':3}, ['a', 'b']);
┌───────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, ['a', 'b']) │
├───────────────────────────────────────────┤
│ {'a':1,'b':2}                             │
└───────────────────────────────────────────┘
```
