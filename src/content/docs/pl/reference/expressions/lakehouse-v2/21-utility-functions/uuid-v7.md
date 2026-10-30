---
title: UUID_V7 (Lakehouse v2)
description: UUID_V7 — zwraca uporządkowany w czasie ciąg UUID v7. Wartości UUID v7 można sortować według czasu utworzenia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7.md
---

Zwraca uporządkowany w czasie ciąg UUID v7. Wartości UUID v7 można sortować według czasu utworzenia.

## Składnia Analyze

```python
func.uuid_v7()
```

## Przykłady Analyze

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## Składnia SQL

```sql
UUID_V7()
```

## Przykłady SQL

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```
