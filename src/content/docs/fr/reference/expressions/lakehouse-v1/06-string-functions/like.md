---
title: LIKE (Lakehouse v1)
description: LIKE effectue une correspondance de motif à l'aide d'un motif SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/like.md
---

Effectue une correspondance de motif à l'aide d'un motif SQL. Renvoie 1 (TRUE) ou 0 (FALSE). Si expr ou pat est NULL, le résultat est NULL.

## Syntaxe Analyze

```python
<column>.like('plaid%')
```

## Exemples Analyze

```python
my_clothes.like('plaid%)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## Syntaxe SQL

```sql
<expr> LIKE <pattern>
```

## Exemples SQL

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint64 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
