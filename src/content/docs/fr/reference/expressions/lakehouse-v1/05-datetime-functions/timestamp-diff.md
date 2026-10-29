---
title: TIMESTAMP_DIFF (Lakehouse v1)
description: TIMESTAMP_DIFF — calcule la différence entre deux horodatages et renvoie le résultat sous forme d'INTERVAL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timestamp-diff.md
---

Calcule la différence entre deux horodatages et renvoie le résultat sous forme d'INTERVAL.

## Syntaxe Analyze

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Exemples Analyze

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## Type de retour

INTERVAL (au format `hours:minutes:seconds`).

## Exemples SQL

Cet exemple montre que l'écart entre le 1er février 2025 et le 1er janvier 2025 est de 744 heures, soit 31 jours :

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```
