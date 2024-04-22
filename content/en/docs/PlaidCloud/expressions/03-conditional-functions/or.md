---
title: OR
---

Conditional OR operator.  Checks whether either condition is true.

## Analyze Syntax

```python
or_(<expr1>[, <expr2> ...])
```

## Analyze Examples
```
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## SQL Syntax

```sql
<expr1> OR <expr2>
```

## SQL Examples
