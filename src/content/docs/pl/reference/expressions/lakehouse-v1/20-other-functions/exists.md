---
title: EXISTS (Lakehouse v1)
description: EXISTS — warunek exists jest używany razem z podzapytaniem i uznaje się go za „spełniony”.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/exists.md
---

Warunek exists jest używany razem z podzapytaniem i uznaje się go za „spełniony”, jeśli podzapytanie zwraca co najmniej jeden wiersz.

## Składnia SQL

```sql
WHERE EXISTS ( <subquery> );
```

## Przykłady SQL
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
