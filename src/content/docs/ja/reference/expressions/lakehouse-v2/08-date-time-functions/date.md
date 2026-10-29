---
title: DATE (Lakehouse v2)
description: DATE — 日時の式から日付部分を抽出します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/date.md
---

日時の式から日付部分を抽出します。

## Analyzeの構文

```python
func.date(<datetime>)
```

## Analyzeの例

```python
func.date('2024-06-15 14:30:00')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## SQLの構文

```sql
DATE(<datetime>)
```

## SQLの例

```sql
SELECT DATE('2024-06-15 14:30:00');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
