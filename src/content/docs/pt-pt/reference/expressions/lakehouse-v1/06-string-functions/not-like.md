---
title: NOT LIKE (Lakehouse v1)
description: NOT LIKE — ausência de correspondência de padrões através de um padrão SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-like.md
---

Ausência de correspondência de padrões através de um padrão SQL. Devolve 1 (TRUE) ou 0 (FALSE). Se expr ou pat for NULL, o resultado é NULL.

## Sintaxe do Analyze

```python
<column>.not_like(<pattern>)
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
<expr> NOT LIKE <pattern>
```

## Exemplos SQL

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
