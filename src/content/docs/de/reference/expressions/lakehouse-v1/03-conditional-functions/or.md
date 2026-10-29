---
title: OR (Lakehouse v1)
description: OR – bedingter OR-Operator.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/or.md
---

Bedingter OR-Operator. Prüft, ob eine der beiden Bedingungen wahr ist.

## Analyze-Syntax

```python
or_(<expr1>[, <expr2> ...])
```

## Analyze-Beispiele

```python
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL-Syntax

```sql
<expr1> OR <expr2>
```

## SQL-Beispiele
```sql
SELECT * FROM table WHERE
    table.color = 'green'
    OR table.shape = 'circle'  
    OR table.price >= 1.25;
```
