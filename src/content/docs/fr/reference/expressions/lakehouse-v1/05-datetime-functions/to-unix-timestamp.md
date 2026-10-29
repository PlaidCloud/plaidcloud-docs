---
title: TO_UNIX_TIMESTAMP (Lakehouse v1)
description: TO_UNIX_TIMESTAMP convertit un timestamp au format date/heure en timestamp Unix.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-unix-timestamp.md
---

Convertit un timestamp au format date/heure en timestamp Unix. Un timestamp Unix représente le nombre de secondes écoulées depuis le 1er janvier 1970 à 00:00:00 UTC.

## Syntaxe Analyze

```python
func.to_unix_timestamp(<expr>)
```

## Exemples Analyze

```python
func.to_unix_timestamp('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_unix_timestamp('2023-11-12 09:38:18.165575')           │
│                          UInt32                                │
├────────────────────────────────────────────────────────────────┤
│                                                     1699781898 │
└────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_UNIX_TIMESTAMP(<expr>)
```

## Arguments

| Arguments   | Description         |
| ----------- | ------------------- |
| `<expr>`    | Timestamp           |

Pour plus d'informations sur le type de données timestamp, consultez Date & Time.

## Type de retour

`BIGINT`

## Exemples SQL

```sql
SELECT
  to_unix_timestamp('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_unix_timestamp('2023-11-12 09:38:18.165575') │
│                      UInt32                     │
├─────────────────────────────────────────────────┤
│                                      1699781898 │
└─────────────────────────────────────────────────┘
```
