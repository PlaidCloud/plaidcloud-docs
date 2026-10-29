---
title: EXISTS (Lakehouse v1)
description: EXISTS — a condição exists é utilizada em combinação com uma subconsulta e considera-se satisfeita se a subconsulta devolver pelo menos uma linha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/exists.md
---

A condição exists é utilizada em combinação com uma subconsulta e considera-se "satisfeita" se a subconsulta devolver pelo menos uma linha.

## Sintaxe SQL

```sql
WHERE EXISTS ( <subquery> );
```

## Exemplos de SQL
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
