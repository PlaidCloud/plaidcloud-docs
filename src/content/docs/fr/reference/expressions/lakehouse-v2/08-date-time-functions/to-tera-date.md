---
title: TO_TERA_DATE (Lakehouse v2)
description: TO_TERA_DATE — convertit une valeur VARCHAR en valeur DATE selon une chaîne de format Teradata.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-date.md
---

Convertit une valeur VARCHAR en valeur DATE selon une chaîne de format Teradata.

## Syntaxe Analyze

```python
func.to_tera_date(<str>, <format>)
```

## Exemples Analyze

```python
func.to_tera_date('20240615', 'YYYYMMDD')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Syntaxe SQL

```sql
TO_TERA_DATE(<str>, <format>)
```

## Exemples SQL

```sql
SELECT TO_TERA_DATE('20240615', 'YYYYMMDD');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
