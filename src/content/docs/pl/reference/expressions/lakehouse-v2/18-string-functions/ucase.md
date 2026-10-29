---
title: UCASE (Lakehouse v2)
description: UCASE — zamienia ciąg na wielkie litery. Alias funkcji `UPPER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ucase.md
---

Zamienia ciąg na wielkie litery. Alias funkcji `UPPER`.

## Składnia Analyze

```python
func.ucase(<str>)
```

## Przykłady Analyze

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## Składnia SQL

```sql
UCASE(<str>)
```

## Przykłady SQL

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
