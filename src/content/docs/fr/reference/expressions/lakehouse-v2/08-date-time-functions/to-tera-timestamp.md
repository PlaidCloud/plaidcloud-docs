---
title: TO_TERA_TIMESTAMP (Lakehouse v2)
description: "Utilisez la fonction de date/heure TO_TERA_TIMESTAMP dans PlaidCloud Lakehouse. Convertit une valeur VARCHAR en valeur DATETIME selon une chaîne de format Teradata."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-tera-timestamp.md
---

Convertit une valeur VARCHAR en valeur DATETIME selon une chaîne de format Teradata.

## Syntaxe Analyze

```python
func.to_tera_timestamp(<str>, <format>)
```

## Exemples Analyze

```python
func.to_tera_timestamp('20240615143000', 'YYYYMMDDHH24MISS')

┌───────────────────────┐
│ '2024-06-15 14:30:00'  │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TO_TERA_TIMESTAMP(<str>, <format>)
```

## Exemples SQL

```sql
SELECT TO_TERA_TIMESTAMP('20240615143000', 'YYYYMMDDHH24MISS');

┌─────────────────────┐
│ 2024-06-15 14:30:00  │
└─────────────────────┘
```
