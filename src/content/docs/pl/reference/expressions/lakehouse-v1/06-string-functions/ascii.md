---
title: ASCII (Lakehouse v1)
description: ASCII — zwraca wartość liczbową pierwszego znaku od lewej w ciągu znaków str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

Zwraca wartość liczbową pierwszego znaku od lewej w ciągu znaków str.

## Składnia Analyze

```python
func.ascii(<expr>)
```

## Przykłady Analyze

```python
func.ascii('2')
┌─────────────────┐
│ func.ascii('2') │
├─────────────────┤
│              50 │
└─────────────────┘
```

## Składnia SQL

```sql
ASCII(<expr>)
```

## Argumenty

| Argumenty | Opis           |
|-----------|----------------|
| `<expr>`  | Ciąg znaków.   |

## Typ zwracany

`TINYINT`

## Przykłady SQL

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
