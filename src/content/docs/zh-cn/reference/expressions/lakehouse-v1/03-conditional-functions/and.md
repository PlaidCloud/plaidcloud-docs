---
title: AND (Lakehouse v1)
description: AND：条件 AND 运算符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/and.md
---

条件 AND 运算符。检查两个条件是否都为真。

## Analyze 语法

```python
and_(<expr1>[, <expr2> ...])
```

## Analyze 示例

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL 语法

```sql
<expr1> AND <expr2>
```

## SQL 示例

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
