---
title: BIT_LENGTH (Lakehouse v1)
description: BIT_LENGTH — devuelve la longitud de una cadena en bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

Devuelve la longitud de una cadena en bits.

## Sintaxis de Analyze

```python
func.bit_length(<expr>)
```

## Ejemplos de Analyze

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## Sintaxis SQL

```sql
BIT_LENGTH(<expr>)
```

## Argumentos

| Argumentos | Descripción |
|-----------| ----------- |
| `<expr>`  | La cadena. |

## Tipo de retorno

`BIGINT`

## Ejemplos de SQL

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
