---
title: MAP_SIZE (Lakehouse v1)
description: MAP_SIZE — devolve o tamanho de um MAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-size.md
---

Devolve o tamanho de um MAP.

## Sintaxe SQL

```sql
MAP_SIZE( <map> )
```

## Argumentos

| Argumentos | Descrição          |
|-----------|--------------------|
| `<map>`   | O mapa de entrada. |

## Tipo de retorno

UInt64.

## Exemplos de SQL

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
