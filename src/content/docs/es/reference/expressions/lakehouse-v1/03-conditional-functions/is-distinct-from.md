---
title: "IS [ NOT ] DISTINCT FROM (Lakehouse v1)"
description: "IS [ NOT ] DISTINCT FROM — compara si dos expresiones son iguales (o distintas) teniendo en cuenta la nulabilidad, es decir, trata los NULL como valores conocidos."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-distinct-from.md
---

Compara si dos expresiones son iguales (o distintas) teniendo en cuenta la nulabilidad, es decir, trata los NULL como valores conocidos al comparar la igualdad.

## Sintaxis de SQL

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## Ejemplos de SQL

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
