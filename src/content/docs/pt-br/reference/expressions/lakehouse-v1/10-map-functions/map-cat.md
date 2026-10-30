---
title: MAP_CAT (Lakehouse v1)
description: MAP_CAT — retorna a concatenação de dois MAPs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

Retorna a concatenação de dois MAPs.

## Sintaxe SQL

```sql
MAP_CAT( <map1>, <map2> )
```

## Argumentos

| Argumentos | Descrição                          |
|-----------|-------------------------------------|
| `<map1>`  | O MAP de origem.                    |
| `<map2>`  | O MAP a ser anexado a map1.         |

:::note
- Se map1 e map2 tiverem um valor com a mesma chave, o mapa de saída conterá o valor de map2.
- Se qualquer um dos argumentos for NULL, a função retorna NULL sem relatar nenhum erro.
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
