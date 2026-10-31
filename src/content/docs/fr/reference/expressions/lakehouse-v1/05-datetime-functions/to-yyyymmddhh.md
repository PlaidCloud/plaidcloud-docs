---
title: TO_YYYYMMDDHH (Lakehouse v1)
description: TO_YYYYMMDDHH met en forme une date ou un timestamp en chaîne au format « YYYYMMDDHH ».
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhh.md
---

Met en forme une date ou un timestamp en chaîne au format « YYYYMMDDHH » (année, mois, jour, heure).

## Syntaxe Analyze

```python
func.to_yyyymmddhh(<expr>)
```

## Exemples Analyze

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_YYYYMMDDHH(<expr>)
```

## Arguments

| Arguments | Description   |
|-----------|---------------|
| `<expr>`  | date/datetime |

## Type de retour

Renvoie un entier non signé sur 64 bits (UInt64) au format « YYYYMMDDHH ».

## Exemples SQL

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```
