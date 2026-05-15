---
title: AND
description: AND — conditional AND operator. Includes detailed syntax, examples, and usage reference.
---

Conditional AND operator.  Checks whether both conditions are true.

## Analyze Syntax

```python
and_(<expr1>[, <expr2> ...])
```

## Analyze Examples

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL Syntax

```sql
<expr1> AND <expr2>
```

## SQL Examples

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
