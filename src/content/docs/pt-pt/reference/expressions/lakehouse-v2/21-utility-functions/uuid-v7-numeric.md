---
title: UUID_V7_NUMERIC (Lakehouse v2)
description: UUID_V7_NUMERIC — devolve um UUID v7 ordenado por tempo como valor LARGEINT de 128 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7-numeric.md
---

Devolve um UUID v7 ordenado por tempo como valor LARGEINT de 128 bits. Os valores UUID v7 podem ser ordenados pela hora de criação.

## Sintaxe do Analyze

```python
func.uuid_v7_numeric()
```

## Exemplos do Analyze

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## Sintaxe SQL

```sql
UUID_V7_NUMERIC()
```

## Exemplos SQL

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```
