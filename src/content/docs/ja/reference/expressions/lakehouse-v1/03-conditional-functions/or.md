---
title: OR（Lakehouse v1）
description: OR — 条件の論理和（OR）演算子です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/or.md
---

条件の論理和（OR）演算子です。いずれかの条件が真かどうかを確認します。

## Analyze 構文

```python
or_(<expr1>[, <expr2> ...])
```

## Analyze の例

```python
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL 構文

```sql
<expr1> OR <expr2>
```

## SQL の例
```sql
SELECT * FROM table WHERE
    table.color = 'green'
    OR table.shape = 'circle'  
    OR table.price >= 1.25;
```
