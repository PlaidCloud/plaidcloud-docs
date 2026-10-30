---
title: "IS [ NOT ] DISTINCT FROM (Lakehouse v1)"
description: IS [ NOT ] DISTINCT FROM — compara se duas expressões são iguais (ou diferentes) considerando a nulidade, ou seja, trata NULLs como valores conhecidos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-distinct-from.md
---

Compara se duas expressões são iguais (ou diferentes) considerando a nulidade, ou seja, trata NULLs como valores conhecidos na comparação de igualdade.

## Sintaxe SQL

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## Exemplos de SQL

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
