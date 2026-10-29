---
title: AND (Lakehouse v1)
description: "AND : opérateur ET conditionnel."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/and.md
---

Opérateur ET conditionnel.  Vérifie si les deux conditions sont vraies.

## Syntaxe Analyze

```python
and_(<expr1>[, <expr2> ...])
```

## Exemples Analyze

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## Syntaxe SQL

```sql
<expr1> AND <expr2>
```

## Exemples SQL

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
