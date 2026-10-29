---
title: MAP_PICK (Lakehouse v1)
description: MAP_PICK — retorna um novo MAP contendo os pares chave-valor especificados de um MAP existente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-pick.md
---

Retorna um novo MAP contendo os pares chave-valor especificados de um MAP existente.

## Sintaxe SQL

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## Argumentos

| Argumentos | Descrição                                                    |
|-----------|--------------------------------------------------------------|
| `<map>`   | O MAP de entrada.                                            |
| `<keyN>`  | As KEYs a serem incluídas no MAP retornado.                  |
| `<array>` | O Array de KEYs a serem incluídas no MAP retornado.          |

:::note
- Os tipos das expressões de chave e das chaves do mapa devem ser iguais.
- Valores de chave não encontrados no mapa serão ignorados.
:::

## Tipo de retorno

Map.

## Exemplos de SQL

```sql
SELECT MAP_PICK({'a':1,'b':2,'c':3}, 'a', 'c');
┌─────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, 'a', 'c') │
├─────────────────────────────────────────┤
│ {'a':1,'c':3}                           │
└─────────────────────────────────────────┘

SELECT MAP_PICK({'a':1,'b':2,'c':3}, ['a', 'b']);
┌───────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, ['a', 'b']) │
├───────────────────────────────────────────┤
│ {'a':1,'b':2}                             │
└───────────────────────────────────────────┘
```
