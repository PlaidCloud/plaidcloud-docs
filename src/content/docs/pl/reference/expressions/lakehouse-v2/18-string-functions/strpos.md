---
title: STRPOS (Lakehouse v2)
description: STRPOS — zwraca pozycję pierwszego wystąpienia podciągu. Alias funkcji `LOCATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strpos.md
---

Zwraca pozycję pierwszego wystąpienia podciągu. Alias funkcji `LOCATE`.

## Składnia Analyze

```python
func.strpos(<str>, <substr>)
```

## Przykłady Analyze

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## Składnia SQL

```sql
STRPOS(<str>, <substr>)
```

## Przykłady SQL

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
