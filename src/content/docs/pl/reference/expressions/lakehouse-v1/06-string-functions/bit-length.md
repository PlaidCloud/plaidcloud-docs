---
title: BIT_LENGTH (Lakehouse v1)
description: BIT_LENGTH — zwraca długość ciągu znaków w bitach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

Zwraca długość ciągu znaków w bitach.

## Składnia Analyze

```python
func.bit_length(<expr>)
```

## Przykłady Analyze

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## Składnia SQL

```sql
BIT_LENGTH(<expr>)
```

## Argumenty

| Argumenty | Opis         |
|-----------| ------------ |
| `<expr>`  | Ciąg znaków. |

## Typ zwracany

`BIGINT`

## Przykłady SQL

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
