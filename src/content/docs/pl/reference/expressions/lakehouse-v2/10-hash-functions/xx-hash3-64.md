---
title: XX_HASH3_64 (Lakehouse v2)
description: XX_HASH3_64 — zwraca 64-bitowy skrót xxHash3 wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-64.md
---

Zwraca 64-bitowy skrót xxHash3 wartości.

## Składnia Analyze

```python
func.xx_hash3_64(<expr>[, ...])
```

## Przykłady Analyze

```python
func.xx_hash3_64('hello')

┌──────────┐
│ (bigint)  │
└──────────┘
```

## Składnia SQL

```sql
XX_HASH3_64(<expr>[, ...])
```

## Przykłady SQL

```sql
SELECT XX_HASH3_64('hello');

┌──────────────────────┐
│ -7685981735718036227  │
└──────────────────────┘
```
