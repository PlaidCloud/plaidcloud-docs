---
title: CURRENT_ROLE (Lakehouse v2)
description: CURRENT_ROLE — devolve o papel ativo atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-role.md
---

Devolve o papel ativo atual.

## Sintaxe do Analyze

```python
func.current_role()
```

## Exemplos do Analyze

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## Sintaxe SQL

```sql
CURRENT_ROLE()
```

## Exemplos SQL

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
