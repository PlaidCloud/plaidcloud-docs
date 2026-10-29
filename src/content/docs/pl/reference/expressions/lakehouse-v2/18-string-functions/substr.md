---
title: SUBSTR (Lakehouse v2)
description: SUBSTR — zwraca podciąg zaczynający się od podanej pozycji, z opcjonalną długością.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substr.md
---

Zwraca podciąg zaczynający się od podanej pozycji, z opcjonalną długością.

## Składnia Analyze

```python
func.substr(<str>, <pos>[, <len>])
```

## Przykłady Analyze

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Składnia SQL

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## Przykłady SQL

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
