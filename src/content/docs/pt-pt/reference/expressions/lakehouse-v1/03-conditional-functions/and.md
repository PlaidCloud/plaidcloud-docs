---
title: AND (Lakehouse v1)
description: AND — operador AND condicional.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/and.md
---

Operador AND condicional. Verifica se ambas as condições são verdadeiras.

## Sintaxe do Analyze

```python
and_(<expr1>[, <expr2> ...])
```

## Exemplos do Analyze

```python
and_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## Sintaxe SQL

```sql
<expr1> AND <expr2>
```

## Exemplos SQL

```sql
SELECT * FROM table WHERE
    table.color = 'green'
    AND table.shape = 'circle'  
    AND table.price >= 1.25;
```
