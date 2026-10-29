---
title: MAP_VALUES (Lakehouse v1)
description: MAP_VALUES — retorna os valores de um mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-values.md
---

Retorna os valores de um mapa.

## Sintaxe SQL

```sql
MAP_VALUES( <map> )
```

## Argumentos

| Argumentos | Descrição          |
|-----------|---------------------|
| `<map>`   | O mapa de entrada.  |

## Tipo de retorno

Array.

## Exemplos de SQL

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
