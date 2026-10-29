---
title: NOT LIKE (Lakehouse v1)
description: NOT LIKE — no coincidencia de patrones mediante un patrón SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-like.md
---

No coincidencia de patrones mediante un patrón SQL. Devuelve 1 (TRUE) o 0 (FALSE). Si expr o pat es NULL, el resultado es NULL.

## Sintaxis de Analyze

```python
<column>.not_like(<pattern>)
```

## Ejemplos de Analyze

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

## Sintaxis SQL

```sql
<expr> NOT LIKE <pattern>
```

## Ejemplos de SQL

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
