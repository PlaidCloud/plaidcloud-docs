---
title: MAP_CONTAINS_KEY (Lakehouse v1)
description: MAP_CONTAINS_KEY — determina se o MAP especificado contém a chave especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-contains-key.md
---

Determina se o MAP especificado contém a chave especificada.

## Sintaxe SQL

```sql
MAP_CONTAINS_KEY( <map>, <key> )
```

## Argumentos

| Argumentos | Descrição                    |
|-----------|-------------------------------|
| `<map>`   | O mapa a ser pesquisado.      |
| `<key>`   | A chave a ser encontrada.     |

## Tipo de retorno

Boolean.

## Exemplos de SQL

```sql
SELECT MAP_CONTAINS_KEY({'a':1,'b':2,'c':3}, 'c');
┌────────────────────────────────────────────┐
│ map_contains_key({'a':1,'b':2,'c':3}, 'c') │
├────────────────────────────────────────────┤
│ true                                       │
└────────────────────────────────────────────┘

SELECT MAP_CONTAINS_KEY({'a':1,'b':2,'c':3}, 'x');
┌────────────────────────────────────────────┐
│ map_contains_key({'a':1,'b':2,'c':3}, 'x') │
├────────────────────────────────────────────┤
│ false                                      │
└────────────────────────────────────────────┘
```
