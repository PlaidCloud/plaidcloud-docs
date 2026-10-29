---
title: MAP_DELETE (Lakehouse v1)
description: MAP_DELETE — retorna um MAP existente com uma ou mais chaves removidas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-delete.md
---

Retorna um MAP existente com uma ou mais chaves removidas.

## Sintaxe SQL

```sql
MAP_DELETE( <map>, <key1> [, <key2>, ... ] )
MAP_DELETE( <map>, <array> )
```

## Argumentos

| Argumentos | Descrição                                                  |
|-----------|-------------------------------------------------------------|
| `<map>`   | O MAP que contém a KEY a ser removida.                      |
| `<keyN>`  | As KEYs a serem omitidas do MAP retornado.                  |
| `<array>` | O Array de KEYs a serem omitidas do MAP retornado.          |

:::note
- Os tipos das expressões de chave e das chaves do mapa devem ser iguais.
- Valores de chave não encontrados no mapa serão ignorados.
:::

## Tipo de retorno

Map.

## Exemplos de SQL

```sql
SELECT MAP_DELETE({'a':1,'b':2,'c':3}, 'a', 'c');
┌───────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, 'a', 'c') │
├───────────────────────────────────────────┤
│ {'b':2}                                   │
└───────────────────────────────────────────┘

SELECT MAP_DELETE({'a':1,'b':2,'c':3}, ['a', 'b']);
┌─────────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, ['a', 'b']) │
├─────────────────────────────────────────────┤
│ {'c':3}                                     │
└─────────────────────────────────────────────┘
```
