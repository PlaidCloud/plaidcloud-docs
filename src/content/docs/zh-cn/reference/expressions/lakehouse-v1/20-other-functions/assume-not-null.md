---
title: ASSUME_NOT_NULL (Lakehouse v1)
description: ASSUME_NOT_NULL：为 Nullable 类型生成等效的非 Nullable 值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/assume-not-null.md
---

为 Nullable 类型生成等效的非 `Nullable` 值。如果原始值为 `NULL`，则结果不确定。 

## Analyze 语法

```python
func.assume_not_null(<x>)
```

## Analyze 示例

```python
With a table like:

┌────────────────────┐
│        x  │   y    │
├────────────────────┤
│         1 │   NULL │
│         2 │      3 │
└────────────────────┘

func.assume_not_null(y)
┌─────────────────────────┐
│ func.assume_not_null(y) │
├─────────────────────────┤
│                       0 │
│                       3 │
└─────────────────────────┘
```

## SQL 语法

```sql
ASSUME_NOT_NULL(<x>)
```

## 别名

- [REMOVE_NULLABLE](../remove-nullable)

## 返回类型

对于非 `Nullable` 类型，返回原始数据类型；对于 `Nullable` 类型，返回其内嵌的非 `Nullable` 数据类型。

## SQL 示例

```sql
CREATE TABLE default.t_null ( x int,  y int null);

INSERT INTO default.t_null values (1, null), (2, 3);

SELECT ASSUME_NOT_NULL(y), REMOVE_NULLABLE(y) FROM t_null;

┌─────────────────────────────────────────┐
│ assume_not_null(y) │ remove_nullable(y) │
├────────────────────┼────────────────────┤
│                  0 │                  0 │
│                  3 │                  3 │
└─────────────────────────────────────────┘
```
