---
title: TO_YYYYMM (Lakehouse v1)
description: TO_YYYYMM convertit une date ou une date avec heure (timestamp/datetime) en nombre UInt32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymm.md
---

Convertit une date ou une date avec heure (timestamp/datetime) en nombre UInt32 contenant l'année et le numéro du mois.

## Syntaxe Analyze

```python
func.to_yyyymm(<expr>)
```

## Exemples Analyze

```python
func.to_yyyymm('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_yyyymm('2023-11-12 09:38:18.165575') │
│                   UInt32                     │
├──────────────────────────────────────────────┤
│                                       202311 │
└──────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_YYYYMM(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`  | date/timestamp |

## Type de retour

`INT`, renvoyé au format `YYYYMM`.

## Exemples SQL

```sql
SELECT
  to_yyyymm('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_yyyymm('2023-11-12 09:38:18.165575') │
│                  UInt32                 │
├─────────────────────────────────────────┤
│                                  202311 │
└─────────────────────────────────────────┘
```
