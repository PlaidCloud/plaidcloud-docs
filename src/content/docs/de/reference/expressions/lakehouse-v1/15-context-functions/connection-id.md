---
title: CONNECTION_ID (Lakehouse v1)
description: CONNECTION_ID gibt die Verbindungs-ID der aktuellen Verbindung zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/connection-id.md
---

Gibt die Verbindungs-ID der aktuellen Verbindung zurück.

## Analyze-Syntax

```python
func.connection_id()
```

## Analyze-Beispiele

```python
func.connection_id()

┌──────────────────────────────────────┐
│       func.connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```

## SQL-Syntax

```sql
CONNECTION_ID()
```

## SQL-Beispiele

```sql
SELECT CONNECTION_ID();

┌──────────────────────────────────────┐
│            connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```
