---
title: TO_DATETIME_NTZ (Lakehouse v2)
description: TO_DATETIME_NTZ — convertit une valeur en DATETIME sans fuseau horaire (NTZ).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-datetime-ntz.md
---

Convertit une valeur en DATETIME sans fuseau horaire (NTZ). Le résultat n'est pas affecté par les paramètres de fuseau horaire de la session.

## Syntaxe Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')
```

## Exemples Analyze

```python
func.to_datetime_ntz('2024-06-15 14:30:00')

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```

## Syntaxe SQL

```sql
TO_DATETIME_NTZ(<expr>)
```

## Exemples SQL

```sql
SELECT TO_DATETIME_NTZ('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15 14:30:00 │
└─────────────────────┘
```
