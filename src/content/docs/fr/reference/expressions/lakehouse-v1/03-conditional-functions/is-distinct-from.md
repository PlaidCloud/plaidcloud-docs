---
title: "IS [ NOT ] DISTINCT FROM (Lakehouse v1)"
description: IS [ NOT ] DISTINCT FROM — compare si deux expressions sont égales (ou différentes) en tenant compte de la nullabilité, c'est-à-dire en traitant les NULL comme des valeurs connues.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-distinct-from.md
---

Compare si deux expressions sont égales (ou différentes) en tenant compte de la nullabilité, c'est-à-dire en traitant les NULL comme des valeurs connues pour tester l'égalité.

## Syntaxe SQL

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## Exemples SQL

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
