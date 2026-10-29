---
title: IF (Lakehouse v1)
description: IF — se <cond1> for TRUE, retorna <expr1>.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/if.md
---

Se `<cond1>` for TRUE, retorna `<expr1>`. Caso contrário, se `<cond2>` for TRUE, retorna `<expr2>`, e assim por diante.

## Sintaxe do Analyze

```python
func.if_(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## Exemplos do Analyze

```python
func.if_((1 > 2), 3, (4 < 5), 6, 7)

┌─────────────────────────────────────┐
│ func.if_((1 > 2), 3, (4 < 5), 6, 7) │
├─────────────────────────────────────┤
│                                   6 │
└─────────────────────────────────────┘
```

## Sintaxe SQL

```sql
IF(<cond1>, <expr1>, [<cond2>, <expr2> ...], <expr_else>)
```

## Exemplos de SQL

```sql
SELECT IF(1 > 2, 3, 4 < 5, 6, 7);

┌───────────────────────────────┐
│ if((1 > 2), 3, (4 < 5), 6, 7) │
├───────────────────────────────┤
│                             6 │
└───────────────────────────────┘
```
