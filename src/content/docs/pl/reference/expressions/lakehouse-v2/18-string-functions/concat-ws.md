---
title: CONCAT_WS (Lakehouse v2)
description: CONCAT_WS — łączy ciągi znaków za pomocą separatora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat-ws.md
---

Łączy ciągi znaków za pomocą separatora.

## Składnia Analyze

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Przykłady Analyze

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## Składnia SQL

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## Przykłady SQL

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
