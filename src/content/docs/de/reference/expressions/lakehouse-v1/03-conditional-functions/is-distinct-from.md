---
title: "IS [ NOT ] DISTINCT FROM (Lakehouse v1)"
description: IS [ NOT ] DISTINCT FROM – vergleicht, ob zwei Ausdrücke gleich (oder ungleich) sind, und berücksichtigt dabei NULL-Werte, indem es sie wie bekannte Werte behandelt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-distinct-from.md
---

Vergleicht, ob zwei Ausdrücke gleich (oder ungleich) sind, und berücksichtigt dabei NULL-Werte, indem es NULL beim Gleichheitsvergleich wie einen bekannten Wert behandelt.

## SQL-Syntax

```sql
<expr1> IS [ NOT ] DISTINCT FROM <expr2>
```

## SQL-Beispiele

```sql
SELECT NULL IS DISTINCT FROM NULL;

┌────────────────────────────┐
│ null is distinct from null │
├────────────────────────────┤
│ false                      │
└────────────────────────────┘
```
