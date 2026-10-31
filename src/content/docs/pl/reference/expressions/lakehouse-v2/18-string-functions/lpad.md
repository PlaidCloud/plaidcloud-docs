---
title: LPAD (Lakehouse v2)
description: LPAD — dopełnia ciąg z lewej strony do podanej długości za pomocą ciągu wypełniającego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

Dopełnia ciąg z lewej strony do podanej długości za pomocą ciągu wypełniającego.

## Składnia Analyze

```python
func.lpad(<str>, <len>, <pad>)
```

## Przykłady Analyze

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## Składnia SQL

```sql
LPAD(<str>, <len>, <pad>)
```

## Przykłady SQL

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
