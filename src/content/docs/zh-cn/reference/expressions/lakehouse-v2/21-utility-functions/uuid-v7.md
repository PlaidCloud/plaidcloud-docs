---
title: UUID_V7 (Lakehouse v2)
description: UUID_V7：返回按时间排序的 UUID v7 字符串。UUID v7 值可按创建时间排序。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7.md
---

返回按时间排序的 UUID v7 字符串。UUID v7 值可按创建时间排序。

## Analyze 语法

```python
func.uuid_v7()
```

## Analyze 示例

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## SQL 语法

```sql
UUID_V7()
```

## SQL 示例

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```
