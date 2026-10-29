---
title: AND (Lakehouse v1)
description: AND – bedingter AND-Operator.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/and.md
---

Bedingter AND-Operator.  Prüft, ob beide Bedingungen wahr sind.

## Analyze-Syntax

```python
and_(<expr1>[, <expr2> ...])
```

## Analyze-Beispiele

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL-Syntax

```sql
<expr1> AND <expr2>
```

## SQL-Beispiele

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
