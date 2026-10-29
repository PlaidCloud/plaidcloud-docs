---
title: ARRAY_TO_STRING (Lakehouse v1)
description: ARRAY_TO_STRING：使用指定的分隔符，将数组的元素连接成单个字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-to-string.md
---

使用指定的分隔符，将数组的元素连接成单个字符串。

## Analyze 语法

```python
func.array_to_string( <array>, '<separator>' )
```

## Analyze 示例

```python
func.array_to_string(['apple', 'banana', 'cherry'], ', ') 

┌────────────────────────────────────────────────────────────┐
│ func.array_to_string(['apple', 'banana', 'cherry'], ', ')  │
├────────────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                      │
└────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## SQL 示例

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```
