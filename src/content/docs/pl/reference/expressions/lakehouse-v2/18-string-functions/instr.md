---
title: INSTR (Lakehouse v2)
description: INSTR — zwraca pozycję pierwszego wystąpienia podciągu w ciągu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/instr.md
---

Zwraca pozycję pierwszego wystąpienia podciągu w ciągu.

## Składnia Analyze

```python
func.instr(<str>, <substr>)
```

## Przykłady Analyze

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## Składnia SQL

```sql
INSTR(<str>, <substr>)
```

## Przykłady SQL

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
