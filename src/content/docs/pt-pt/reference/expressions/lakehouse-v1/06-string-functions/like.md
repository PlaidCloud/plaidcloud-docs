---
title: LIKE (Lakehouse v1)
description: LIKE — correspondência de padrões através de um padrão SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/like.md
---

Correspondência de padrões através de um padrão SQL. Devolve 1 (TRUE) ou 0 (FALSE). Se expr ou pat for NULL, o resultado é NULL.

## Sintaxe do Analyze

```python
<column>.like('plaid%')
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
<expr> LIKE <pattern>
```

## Exemplos SQL

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
