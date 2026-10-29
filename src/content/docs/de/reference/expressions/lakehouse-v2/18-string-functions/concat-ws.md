---
title: CONCAT_WS (Lakehouse v2)
description: CONCAT_WS — verkettet Zeichenfolgen mit einem Trennzeichen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat-ws.md
---

Verkettet Zeichenfolgen mit einem Trennzeichen.

## Analyze-Syntax

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Analyze-Beispiele

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL-Syntax

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## SQL-Beispiele

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
