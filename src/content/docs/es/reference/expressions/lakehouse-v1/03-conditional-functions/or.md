---
title: OR (Lakehouse v1)
description: OR — operador OR condicional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/or.md
---

Operador OR condicional. Comprueba si se cumple alguna de las condiciones.

## Sintaxis de Analyze

```python
or_(<expr1>[, <expr2> ...])
```

## Ejemplos de Analyze

```python
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## Sintaxis de SQL

```sql
<expr1> OR <expr2>
```

## Ejemplos de SQL
```sql
SELECT * FROM table WHERE
    table.color = 'green'
    OR table.shape = 'circle'  
    OR table.price >= 1.25;
```
