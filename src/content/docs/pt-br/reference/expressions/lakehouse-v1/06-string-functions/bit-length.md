---
title: BIT_LENGTH (Lakehouse v1)
description: BIT_LENGTH — retorna o comprimento de uma string em bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

Retorna o comprimento de uma string em bits.

## Sintaxe do Analyze

```python
func.bit_length(<expr>)
```

## Exemplos do Analyze

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
BIT_LENGTH(<expr>)
```

## Argumentos

| Argumentos | Descrição   |
|-----------| ----------- |
| `<expr>`  | A string.   |

## Tipo de retorno

`BIGINT`

## Exemplos de SQL

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
