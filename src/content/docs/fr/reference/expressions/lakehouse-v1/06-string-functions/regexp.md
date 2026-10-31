---
title: REGEXP (Lakehouse v1)
description: REGEXP renvoie true si la chaîne <expr> correspond à l'expression régulière définie par le <pattern>, false sinon.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp.md
---

Renvoie `true` si la chaîne `<expr>` correspond à l'expression régulière définie par le `<pattern>`, `false` sinon.

## Syntaxe Analyze

```python
<column>.regexp_match(<pattern>)
```

## Exemples Analyze

```python

With an input table of:
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
│ shoes           │
└─────────────────┘

my_clothes.regexp_match('p*')
┌───────────────────────────────┐
│ my_clothes.regexp_match('p*') │
├───────────────────────────────┤
│ true                          │
│ true                          │
│ true                          │
│ false                         │
└───────────────────────────────┘
```

## Syntaxe SQL

```sql
<expr> REGEXP <pattern>
```

## Alias

- [RLIKE](../rlike)

## Exemples SQL

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```
