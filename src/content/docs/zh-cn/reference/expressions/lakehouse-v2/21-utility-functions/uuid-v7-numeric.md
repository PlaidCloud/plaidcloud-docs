---
title: UUID_V7_NUMERIC (Lakehouse v2)
description: UUID_V7_NUMERIC：以 128 位 LARGEINT 值的形式返回按时间排序的 UUID v7。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7-numeric.md
---

以 128 位 LARGEINT 值的形式返回按时间排序的 UUID v7。UUID v7 值可按创建时间排序。

## Analyze 语法

```python
func.uuid_v7_numeric()
```

## Analyze 示例

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## SQL 语法

```sql
UUID_V7_NUMERIC()
```

## SQL 示例

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```
