---
title: TRANSLATE (Lakehouse v2)
description: TRANSLATE — zastępuje znaki w ciągu zgodnie z mapowaniem znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

Zastępuje znaki w ciągu zgodnie z mapowaniem znaków.

## Składnia Analyze

```python
func.translate(<str>, <from>, <to>)
```

## Przykłady Analyze

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## Składnia SQL

```sql
TRANSLATE(<str>, <from>, <to>)
```

## Przykłady SQL

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
