---
title: MAP_INSERT (Lakehouse v1)
description: MAP_INSERT — gibt eine neue MAP zurück, die aus der Eingabe-MAP mit einem eingefügten neuen Schlüssel-Wert-Paar besteht (ein vorhandener Schlüssel wird mit einem neuen Wert aktualisiert).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-insert.md
---

Gibt eine neue MAP zurück, die aus der Eingabe-MAP mit einem eingefügten neuen Schlüssel-Wert-Paar besteht (ein vorhandener Schlüssel wird mit einem neuen Wert aktualisiert).

## SQL-Syntax

```sql
MAP_INSERT( <map>, <key>, <value> [, <updateFlag> ] )
```

## Argumente

| Argumente      | Beschreibung                                                                                                    |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| `<map>`        | Die Eingabe-MAP.                                                                                                |
| `<key>`        | Der neue Schlüssel, der in die MAP eingefügt wird.                                                              |
| `<value>`      | Der neue Wert, der in die MAP eingefügt wird.                                                                   |
| `<updateFlag>` | Das boolesche Flag gibt an, ob ein vorhandener Schlüssel überschrieben werden darf. Der Standardwert ist FALSE. |

## Rückgabetyp

Map.

## SQL-Beispiele

```sql
SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'd', 4);
┌─────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'd', 4) │
├─────────────────────────────────────────┤
│ {'a':1,'b':2,'c':3,'d':4}               │
└─────────────────────────────────────────┘

SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'a', 5, true);
┌───────────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'a', 5, TRUE) │
├───────────────────────────────────────────────┤
│ {'a':5,'b':2,'c':3}                           │
└───────────────────────────────────────────────┘
```
