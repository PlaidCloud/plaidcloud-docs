---
title: CATALOG (Lakehouse v2)
description: CATALOG — gibt den Namen des aktuellen Katalogs zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/catalog.md
---

Gibt den Namen des aktuellen Katalogs zurück.

## Analyze-Syntax

```python
func.catalog()
```

## Analyze-Beispiele

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## SQL-Syntax

```sql
CATALOG()
```

## SQL-Beispiele

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
