---
title: SPACE (Lakehouse v2)
description: SPACE：返回由指定数量的空格组成的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/space.md
---

返回由指定数量的空格组成的字符串。

## Analyze 语法

```python
func.space(<n>)
```

## Analyze 示例

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## SQL 语法

```sql
SPACE(<n>)
```

## SQL 示例

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```
