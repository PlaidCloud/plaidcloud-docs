---
title: MAKEDATE (Lakehouse v2)
description: MAKEDATE：根据年份和一年中的第几天创建日期。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/makedate.md
---

根据年份和一年中的第几天创建日期。

## Analyze 语法

```python
func.makedate(<year>, <dayofyear>)
```

## Analyze 示例

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## SQL 语法

```sql
MAKEDATE(<year>, <dayofyear>)
```

## SQL 示例

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
