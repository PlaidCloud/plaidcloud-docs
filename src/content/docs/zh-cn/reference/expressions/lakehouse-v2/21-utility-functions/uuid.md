---
title: UUID (Lakehouse v2)
description: UUID：返回随机 UUID 字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid.md
---

返回随机 UUID 字符串。

## Analyze 语法

```python
func.uuid()
```

## Analyze 示例

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## SQL 语法

```sql
UUID()
```

## SQL 示例

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```
