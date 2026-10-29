---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 — zwraca 128-bitowy skrót xxHash3 wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-128.md
---

Zwraca 128-bitowy skrót xxHash3 wartości.

## Składnia Analyze

```python
func.xx_hash3_128(<expr>[, ...])
```

## Przykłady Analyze

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Składnia SQL

```sql
XX_HASH3_128(<expr>[, ...])
```

## Przykłady SQL

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
