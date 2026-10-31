---
title: RPAD (Lakehouse v2)
description: RPAD — dopełnia ciąg z prawej strony do podanej długości za pomocą ciągu wypełniającego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

Dopełnia ciąg z prawej strony do podanej długości za pomocą ciągu wypełniającego.

## Składnia Analyze

```python
func.rpad(<str>, <len>, <pad>)
```

## Przykłady Analyze

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## Składnia SQL

```sql
RPAD(<str>, <len>, <pad>)
```

## Przykłady SQL

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
