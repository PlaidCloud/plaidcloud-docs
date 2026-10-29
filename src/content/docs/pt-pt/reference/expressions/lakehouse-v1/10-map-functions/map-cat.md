---
title: MAP_CAT (Lakehouse v1)
description: MAP_CAT — devolve a concatenação de dois MAP.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

Devolve a concatenação de dois MAP.

## Sintaxe SQL

```sql
MAP_CAT( <map1>, <map2> )
```

## Argumentos

| Argumentos | Descrição                       |
|-----------|---------------------------------|
| `<map1>`  | O MAP de origem.                |
| `<map2>`  | O MAP a acrescentar a map1.     |

:::note
- Se map1 e map2 tiverem um valor com a mesma chave, o mapa de saída contém o valor de map2.
- Se qualquer um dos argumentos for NULL, a função devolve NULL sem comunicar qualquer erro.
:::

## Tipo de retorno

Map.

## Exemplos de SQL

```sql
SELECT MAP_CAT({'a':1,'b':2,'c':3}, {'c':5,'d':6});
┌─────────────────────────────────────────────┐
│ map_cat({'a':1,'b':2,'c':3}, {'c':5,'d':6}) │
├─────────────────────────────────────────────┤
│ {'a':1,'b':2,'c':5,'d':6}                   │
└─────────────────────────────────────────────┘
```
