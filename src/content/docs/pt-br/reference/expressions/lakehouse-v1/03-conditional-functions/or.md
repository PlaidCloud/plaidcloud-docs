---
title: OR (Lakehouse v1)
description: OR — operador condicional OR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/or.md
---

Operador condicional OR.  Verifica se pelo menos uma das condições é verdadeira.

## Sintaxe do Analyze

```python
or_(<expr1>[, <expr2> ...])
```

## Exemplos do Analyze

```python
or_(  
    table.color == 'green',  
    table.shape == 'circle',  
    table.price >= 1.25  
)
```

## Sintaxe SQL

```sql
<expr1> OR <expr2>
```

## Exemplos de SQL
```sql
SELECT * FROM table WHERE
    table.color = 'green'
    OR table.shape = 'circle'  
    OR table.price >= 1.25;
```
