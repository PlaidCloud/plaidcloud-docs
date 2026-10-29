---
title: NOW (Lakehouse v1)
description: NOW – gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/now.md
---

Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.

## Analyze-Syntax

```python
func.now()
```

## Analyze-Beispiele

```python
┌─────────────────────────────────────────────────────────┐
│  func.current_timestamp()  │         func.now()         │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
NOW()
```

## Rückgabetyp

TIMESTAMP

## Aliase

- [CURRENT_TIMESTAMP](../current-timestamp)

## SQL-Beispiele

Dieses Beispiel gibt das aktuelle Datum und die aktuelle Uhrzeit zurück:

```sql
SELECT CURRENT_TIMESTAMP(), NOW();

┌─────────────────────────────────────────────────────────┐
│     current_timestamp()    │            now()           │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```
