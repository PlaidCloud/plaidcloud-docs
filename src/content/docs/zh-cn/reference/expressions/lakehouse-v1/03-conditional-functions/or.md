---
title: OR（Lakehouse v1）
description: OR——条件 OR 运算符。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/or.md
---

条件 OR 运算符。检查两个条件中是否有任一条件为真。

## Analyze 语法

```python
or_(<expr1>[, <expr2> ...])
```

## Analyze 示例

```python
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL 语法

```sql
<expr1> OR <expr2>
```

## SQL 示例
```sql
SELECT * FROM table WHERE
    table.color = 'green'
    OR table.shape = 'circle'  
    OR table.price >= 1.25;
```
