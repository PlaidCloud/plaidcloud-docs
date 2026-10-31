---
title: UUID_V7 (Lakehouse v2)
description: UUID_V7 — gibt eine zeitlich geordnete UUID v7 als Zeichenfolge zurück. UUID-v7-Werte lassen sich nach Erstellungszeitpunkt sortieren.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7.md
---

Gibt eine zeitlich geordnete UUID v7 als Zeichenfolge zurück. UUID-v7-Werte lassen sich nach Erstellungszeitpunkt sortieren.

## Analyze-Syntax

```python
func.uuid_v7()
```

## Analyze-Beispiele

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## SQL-Syntax

```sql
UUID_V7()
```

## SQL-Beispiele

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```
