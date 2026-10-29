---
title: MAP_INSERT (Lakehouse v1)
description: MAP_INSERT — retorna um novo MAP formado pelo MAP de entrada com um novo par chave-valor inserido (ou uma chave existente atualizada com um novo valor).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-insert.md
---

Retorna um novo MAP formado pelo MAP de entrada com um novo par chave-valor inserido (ou uma chave existente atualizada com um novo valor).

## Sintaxe SQL

```sql
MAP_INSERT( <map>, <key>, <value> [, <updateFlag> ] )
```

## Argumentos

| Argumentos     | Descrição                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------|
| `<map>`        | O MAP de entrada.                                                                                      |
| `<key>`        | A nova chave a inserir no MAP.                                                                         |
| `<value>`      | O novo valor a inserir no MAP.                                                                         |
| `<updateFlag>` | O sinalizador booleano indica se uma chave existente pode ser sobrescrita. O padrão é FALSE.           |

## Tipo de retorno

Map.

## Exemplos de SQL

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
