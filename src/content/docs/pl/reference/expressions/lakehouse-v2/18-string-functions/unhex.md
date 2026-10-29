---
title: UNHEX (Lakehouse v2)
description: UNHEX — zamienia ciąg szesnastkowy na ciąg znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

Zamienia ciąg szesnastkowy na ciąg znaków.

## Składnia Analyze

```python
func.unhex(<hex_str>)
```

## Przykłady Analyze

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Składnia SQL

```sql
UNHEX(<hex_str>)
```

## Przykłady SQL

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
