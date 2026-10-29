---
title: CURDATE (Lakehouse v2)
description: CURDATE — 現在の日付を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/curdate.md
---

現在の日付を返します。

## Analyzeの構文

```python
func.curdate()
```

## Analyzeの例

```python
func.curdate()

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQLの構文

```sql
CURDATE()
```

## SQLの例

```sql
SELECT CURDATE();

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
