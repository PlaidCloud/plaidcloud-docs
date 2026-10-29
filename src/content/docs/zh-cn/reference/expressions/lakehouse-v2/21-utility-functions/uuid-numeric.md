---
title: UUID_NUMERIC (Lakehouse v2)
description: UUID_NUMERIC：以 128 位 LARGEINT 值的形式返回随机 UUID。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-numeric.md
---

以 128 位 LARGEINT 值的形式返回随机 UUID。

## Analyze 语法

```python
func.uuid_numeric()
```

## Analyze 示例

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL 语法

```sql
UUID_NUMERIC()
```

## SQL 示例

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
