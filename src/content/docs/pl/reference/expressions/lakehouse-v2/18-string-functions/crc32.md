---
title: CRC32 (Lakehouse v2)
description: CRC32 — zwraca sumę kontrolną CRC-32 ciągu jako liczbę całkowitą bez znaku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/crc32.md
---

Zwraca sumę kontrolną CRC-32 ciągu jako liczbę całkowitą bez znaku.

## Składnia Analyze

```python
func.crc32(<str>)
```

## Przykłady Analyze

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## Składnia SQL

```sql
CRC32(<str>)
```

## Przykłady SQL

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
