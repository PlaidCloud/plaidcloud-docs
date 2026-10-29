---
title: EXISTS (Lakehouse v1)
description: EXISTS — la condition exists s'utilise avec une sous-requête et est considérée comme « remplie ».
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/exists.md
---

La condition exists s'utilise avec une sous-requête et est considérée comme « remplie » si la sous-requête renvoie au moins une ligne.

## Syntaxe SQL

```sql
WHERE EXISTS ( <subquery> );
```

## Exemples SQL
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
