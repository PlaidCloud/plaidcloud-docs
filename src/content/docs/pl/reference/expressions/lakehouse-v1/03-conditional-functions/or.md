---
title: OR (Lakehouse v1)
description: OR — warunkowy operator OR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/or.md
---

Warunkowy operator OR. Sprawdza, czy którykolwiek z warunków jest spełniony.

## Składnia Analyze

```python
or_(<expr1>[, <expr2> ...])
```

## Przykłady Analyze

```python
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## Składnia SQL

```sql
<expr1> OR <expr2>
```

## Przykłady SQL
```sql
SELECT * FROM table WHERE
    table.color = 'green'
    OR table.shape = 'circle'  
    OR table.price >= 1.25;
```
