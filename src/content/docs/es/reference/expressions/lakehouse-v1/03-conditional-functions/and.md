---
title: AND (Lakehouse v1)
description: AND — operador AND condicional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/and.md
---

Operador AND condicional. Comprueba si ambas condiciones son verdaderas.

## Sintaxis de Analyze

```python
and_(<expr1>[, <expr2> ...])
```

## Ejemplos de Analyze

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## Sintaxis de SQL

```sql
<expr1> AND <expr2>
```

## Ejemplos de SQL

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
