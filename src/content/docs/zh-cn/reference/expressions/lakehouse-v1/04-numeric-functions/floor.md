---
title: FLOOR（Lakehouse v1）
description: FLOOR——将数字向下取整。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/floor.md
---

将数字向下取整。

## Analyze 语法

```python
func.floor( <x> )
```

## Analyze 示例

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## SQL 语法

```sql
FLOOR( <x> )
```

## SQL 示例

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```
