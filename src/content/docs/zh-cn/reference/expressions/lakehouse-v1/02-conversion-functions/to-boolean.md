---
title: TO_BOOLEAN (Lakehouse v1)
description: TO_BOOLEAN：将值转换为 BOOLEAN 数据类型。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-boolean.md
---

将值转换为 BOOLEAN 数据类型。

## Analyze 语法

```python
func.to_boolean( <expr> )
```

## Analyze 示例

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL 语法

```sql
TO_BOOLEAN( <expr> )
```

## SQL 示例

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```
