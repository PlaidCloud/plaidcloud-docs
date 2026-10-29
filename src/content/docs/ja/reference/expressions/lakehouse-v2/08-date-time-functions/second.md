---
title: SECOND (Lakehouse v2)
description: SECOND — 日時から秒を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/second.md
---

日時から秒を返します。

## Analyzeの構文

```python
func.second(<datetime>)
```

## Analyzeの例

```python
func.second('2024-06-15 14:30:45')

┌────┐
│ 45  │
└────┘
```

## SQLの構文

```sql
SECOND(<datetime>)
```

## SQLの例

```sql
SELECT SECOND('2024-06-15 14:30:45');

┌────┐
│ 45  │
└────┘
```
