---
title: AND
---

Conditional AND operator.  Checks whether both conditions are true.

## Analyze Syntax

```python
and_(<expr1>[, <expr2> ...])
```

## Analyze Examples
```
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

