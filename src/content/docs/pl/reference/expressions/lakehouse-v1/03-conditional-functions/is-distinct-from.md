---
title: "IS [ NOT ] DISTINCT FROM (Lakehouse v1)"
description: IS [ NOT ] DISTINCT FROM — porównuje, czy dwa wyrażenia są równe (lub nierówne), uwzględniając wartości puste, czyli traktuje NULL jako znane wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-distinct-from.md
---

Porównuje, czy dwa wyrażenia są równe (lub nierówne), uwzględniając wartości puste, czyli traktuje NULL jako znane wartości przy porównywaniu równości.

## Składnia SQL

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## Przykłady SQL

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
