---
title: UNHEX (Lakehouse v1)
description: UNHEX — dla argumentu tekstowego str funkcja UNHEX(str) interpretuje każdą parę znaków argumentu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/unhex.md
---

Dla argumentu tekstowego str funkcja UNHEX(str) interpretuje każdą parę znaków argumentu jako liczbę szesnastkową i konwertuje ją na bajt reprezentowany przez tę liczbę. Zwracaną wartością jest ciąg binarny.

## Składnia Analyze

```python
func.unhex(<expr>)
```

## Przykłady Analyze

```python
func.unhex('6461746162656e64')
┌────────────────────────────────┐
│ func.unhex('6461746162656e64') │
├────────────────────────────────┤
│ 6461746162656E64               │
└────────────────────────────────┘
```

## Składnia SQL

```sql
UNHEX(<expr>)
```

## Aliasy

- [FROM_HEX](../from-hex)

## Przykłady SQL

```sql
SELECT UNHEX('6461746162656e64') as c1, typeof(c1),UNHEX('6461746162656e64')::varchar as c2, typeof(c2), FROM_HEX('6461746162656e64');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           c1              │     typeof(c1)         │       c2         |    typeof(c2)     |   from_hex('6461746162656e64')  |
├───────────────────────────┼────────────────────────|──────────────────┤───────────────────|─────────────────────────────────┤
│ 6461746162656E64          │      binary            │      databend    |    varchar        |   6461746162656E64              |
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT UNHEX(HEX('string')), unhex(HEX('string'))::varchar;

┌──────────────────────────────────────────────────────┐
│ unhex(hex('string')) │ unhex(hex('string'))::varchar │
├──────────────────────┼───────────────────────────────┤
│ 737472696E67         │ string                        │
└──────────────────────────────────────────────────────┘
```
