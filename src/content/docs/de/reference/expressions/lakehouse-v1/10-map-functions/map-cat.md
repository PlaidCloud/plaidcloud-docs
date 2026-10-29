---
title: MAP_CAT (Lakehouse v1)
description: MAP_CAT — gibt die Verkettung zweier MAPs zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

Gibt die Verkettung zweier MAPs zurück.

## SQL-Syntax

```sql
MAP_CAT( <map1>, <map2> )
```

## Argumente

| Argumente | Beschreibung                              |
|-----------|-------------------------------------------|
| `<map1>`  | Die Quell-MAP.                            |
| `<map2>`  | Die an map1 anzuhängende MAP.             |

:::note
- Haben sowohl map1 als auch map2 einen Wert mit demselben Schlüssel, enthält die Ausgabe-MAP den Wert aus map2.
- Ist eines der Argumente NULL, gibt die Funktion NULL zurück, ohne einen Fehler zu melden.
:::

## Rückgabetyp

Map.

## SQL-Beispiele

```sql
SELECT MAP_CAT({'a':1,'b':2,'c':3}, {'c':5,'d':6});
┌─────────────────────────────────────────────┐
│ map_cat({'a':1,'b':2,'c':3}, {'c':5,'d':6}) │
├─────────────────────────────────────────────┤
│ {'a':1,'b':2,'c':5,'d':6}                   │
└─────────────────────────────────────────────┘
```
