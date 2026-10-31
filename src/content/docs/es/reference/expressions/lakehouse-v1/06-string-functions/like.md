---
title: LIKE (Lakehouse v1)
description: LIKE — coincidencia de patrones mediante un patrón SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/like.md
---

Coincidencia de patrones mediante un patrón SQL. Devuelve 1 (TRUE) o 0 (FALSE). Si expr o pat es NULL, el resultado es NULL.

## Sintaxis de Analyze

```python
<column>.like('plaid%')
```

## Ejemplos de Analyze

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

## Sintaxis SQL

```sql
<expr> LIKE <pattern>
```

## Ejemplos de SQL

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
