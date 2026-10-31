---
title: MINUTE (Lakehouse v2)
description: MINUTE — 日時から分を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/minute.md
---

日時から分を返します。

## Analyzeの構文

```python
func.minute(<datetime>)
```

## Analyzeの例

```python
func.minute('2024-06-15 14:30:00')

┌────┐
│ 30  │
└────┘
```

## SQLの構文

```sql
MINUTE(<datetime>)
```

## SQLの例

```sql
SELECT MINUTE('2024-06-15 14:30:00');

┌────┐
│ 30  │
└────┘
```
