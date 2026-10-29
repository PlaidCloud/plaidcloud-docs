---
title: MAP_KEYS (Lakehouse v1)
description: MAP_KEYS — retorna as chaves de um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-keys.md
---

Retorna as chaves de um mapa.

## Sintaxe SQL

```sql
MAP_KEYS( <map> )
```

## Argumentos

| Argumentos | Descrição          |
|-----------|---------------------|
| `<map>`   | O mapa de entrada.  |

## Tipo de retorno

Array.

## Exemplos de SQL

```sql
SELECT MAP_KEYS({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_keys({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ ['a','b','c']                 │
└───────────────────────────────┘
```
