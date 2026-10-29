---
title: AND (Lakehouse v1)
description: AND — warunkowy operator AND.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/and.md
---

Warunkowy operator AND. Sprawdza, czy oba warunki są spełnione.


## Składnia Analyze

```python
and_(<expr1>[, <expr2> ...])
```

## Przykłady Analyze

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## Składnia SQL

```sql
<expr1> AND <expr2>
```

## Przykłady SQL

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
