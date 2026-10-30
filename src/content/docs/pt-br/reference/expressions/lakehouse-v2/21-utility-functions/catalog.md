---
title: CATALOG (Lakehouse v2)
description: CATALOG — retorna o nome do catálogo atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/catalog.md
---

Retorna o nome do catálogo atual.

## Sintaxe do Analyze

```python
func.catalog()
```

## Exemplos do Analyze

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## Sintaxe SQL

```sql
CATALOG()
```

## Exemplos de SQL

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
