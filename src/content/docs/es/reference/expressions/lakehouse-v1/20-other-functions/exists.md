---
title: EXISTS (Lakehouse v1)
description: EXISTS es una condición que se usa junto con una subconsulta y se considera cumplida si la subconsulta devuelve al menos una fila.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/exists.md
---

La condición exists se usa junto con una subconsulta y se considera "cumplida" si la subconsulta devuelve al menos una fila.

## Sintaxis de SQL

```sql
WHERE EXISTS ( <subquery> );
```

## Ejemplos de SQL
```sql
SELECT number FROM numbers(5) AS A WHERE exists (SELECT * FROM numbers(3) WHERE number=1); 
┌────────┐
│ number │
├────────┤
│      0 │
│      1 │
│      2 │
│      3 │
│      4 │
└────────┘
```
