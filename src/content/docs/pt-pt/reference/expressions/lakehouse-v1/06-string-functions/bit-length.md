---
title: BIT_LENGTH (Lakehouse v1)
description: BIT_LENGTH — devolve o comprimento de uma cadeia de caracteres em bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

Devolve o comprimento de uma cadeia de caracteres em bits.

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

| Argumentos | Descrição               |
|-----------| ----------------------- |
| `<expr>`  | A cadeia de caracteres. |

## Tipo de Retorno

`BIGINT`

## Exemplos SQL

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
