---
title: TRY_TO_TIMESTAMP (Lakehouse v1)
description: TRY_TO_TIMESTAMP est une variante de TO_TIMESTAMP dans PlaidCloud Lakehouse qui renvoie NULL en cas d'échec de la conversion au lieu de lever une erreur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/try-to-timestamp.md
---

Variante de [TO_TIMESTAMP](../to-timestamp) dans PlaidCloud Lakehouse qui effectue la même conversion d'une expression en timestamp, mais gère les erreurs : elle renvoie NULL si la conversion échoue, au lieu de lever une erreur.

Voir aussi : [TO_TIMESTAMP](../to-timestamp)

## Syntaxe Analyze

```python
func.try_to_timestamp(<expr>)
```

## Exemples Analyze

```python
func.try_to_timestamp('2022-01-02 02:00:11'), func.try_to_datetime('2022-01-02 02:00:11'), func.try_to_timestamp('plaidcloud')
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ func.try_to_timestamp('2022-01-02 02:00:11') │ func.try_to_datetime('2022-01-02 02:00:11') │ func.try_to_timestamp('plaidcloud') │
│                Timestamp                │                Timestamp                         │                                     │
├─────────────────────────────────────────┼──────────────────────────────────────────────────┤─────────────────────────────────────│
│ 2022-01-02 02:00:11                     │ 2022-01-02 02:00:11                              │ NULL                                │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
-- Convert a string or integer to a timestamp
TRY_TO_TIMESTAMP(<expr>)

-- Convert a string to a timestamp using the given pattern
TRY_TO_TIMESTAMP(<expr, expr>)
```

## Alias

- [TRY_TO_DATETIME](../try-to-datetime)

## Exemples SQL

```sql
SELECT TRY_TO_TIMESTAMP('2022-01-02 02:00:11'), TRY_TO_DATETIME('2022-01-02 02:00:11');

┌──────────────────────────────────────────────────────────────────────────────────┐
│ try_to_timestamp('2022-01-02 02:00:11') │ try_to_datetime('2022-01-02 02:00:11') │
│                Timestamp                │                Timestamp               │
├─────────────────────────────────────────┼────────────────────────────────────────┤
│ 2022-01-02 02:00:11                     │ 2022-01-02 02:00:11                    │
└──────────────────────────────────────────────────────────────────────────────────┘

SELECT TRY_TO_TIMESTAMP('databend'), TRY_TO_DATETIME('databend');

┌────────────────────────────────────────────────────────────┐
│ try_to_timestamp('databend') │ try_to_datetime('databend') │
├──────────────────────────────┼─────────────────────────────┤
│ NULL                         │ NULL                        │
└────────────────────────────────────────────────────────────┘
```
