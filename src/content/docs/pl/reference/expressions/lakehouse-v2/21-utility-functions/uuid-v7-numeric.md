---
title: UUID_V7_NUMERIC (Lakehouse v2)
description: UUID_V7_NUMERIC — zwraca uporządkowany w czasie UUID v7 jako 128-bitową wartość LARGEINT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7-numeric.md
---

Zwraca uporządkowany w czasie UUID v7 jako 128-bitową wartość LARGEINT. Wartości UUID v7 można sortować według czasu utworzenia.

## Składnia Analyze

```python
func.uuid_v7_numeric()
```

## Przykłady Analyze

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## Składnia SQL

```sql
UUID_V7_NUMERIC()
```

## Przykłady SQL

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```
