---
title: OR (Lakehouse v1)
description: OR — opérateur conditionnel OR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/or.md
---

Opérateur conditionnel OR. Vérifie si l'une ou l'autre des conditions est vraie.

## Syntaxe Analyze

```python
or_(<expr1>[, <expr2> ...])
```

## Exemples Analyze

```python
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## Syntaxe SQL

```sql
<expr1> OR <expr2>
```

## Exemples SQL
```sql
SELECT * FROM table WHERE
    table.color = 'green'
    OR table.shape = 'circle'  
    OR table.price >= 1.25;
```
