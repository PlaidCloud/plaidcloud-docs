---
title: NOT LIKE (Lakehouse v1)
description: NOT LIKE vérifie l'absence de correspondance avec un motif SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-like.md
---

Vérifie l'absence de correspondance avec un motif SQL. Renvoie 1 (TRUE) ou 0 (FALSE). Si expr ou pat est NULL, le résultat est NULL.

## Syntaxe Analyze

```python
<column>.not_like(<pattern>)
```

## Exemples Analyze

```python
my_clothes.not_like('%pants)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants XL  │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## Syntaxe SQL

```sql
<expr> NOT LIKE <pattern>
```

## Exemples SQL

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' AND name not like '%64' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
