---
title: AND (Lakehouse v1)
description: AND — 条件のAND演算子です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/and.md
---

条件のAND演算子です。両方の条件がtrueであるかどうかを確認します。

## Analyzeの構文

```python
and_(<expr1>[, <expr2> ...])
```

## Analyzeの例

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQLの構文

```sql
<expr1> AND <expr2>
```

## SQLの例

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
