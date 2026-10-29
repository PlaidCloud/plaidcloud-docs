---
title: TIMESTAMPDIFF (Lakehouse v2)
description: TIMESTAMPDIFF — 2つの日時の差を、指定した単位で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/timestampdiff.md
---

2つの日時の差を、指定した単位で返します。

## Analyzeの構文

```python
func.timestampdiff(<unit>, <start>, <end>)
```

## Analyzeの例

```python
func.timestampdiff('DAY', '2024-01-01', '2024-03-01')

┌────┐
│ 60  │
└────┘
```

## SQLの構文

```sql
TIMESTAMPDIFF(<unit>, <start>, <end>)
```

## SQLの例

```sql
SELECT TIMESTAMPDIFF(DAY, '2024-01-01', '2024-03-01');

┌────┐
│ 60  │
└────┘
```
