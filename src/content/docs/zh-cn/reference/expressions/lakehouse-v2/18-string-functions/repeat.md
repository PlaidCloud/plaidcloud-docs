---
title: REPEAT (Lakehouse v2)
description: REPEAT：将字符串重复指定的次数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/repeat.md
---

将字符串重复指定的次数。

## Analyze 语法

```python
func.repeat(<str>, <n>)
```

## Analyze 示例

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## SQL 语法

```sql
REPEAT(<str>, <n>)
```

## SQL 示例

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
