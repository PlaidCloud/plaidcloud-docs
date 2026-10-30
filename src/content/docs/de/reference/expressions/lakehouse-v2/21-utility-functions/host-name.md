---
title: HOST_NAME (Lakehouse v2)
description: HOST_NAME — Gibt den Hostnamen des aktuellen Backend-Knotens zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/host-name.md
---

Gibt den Hostnamen des aktuellen Backend-Knotens zurück.

## Analyze-Syntax

```python
func.host_name()
```

## Analyze-Beispiele

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## SQL-Syntax

```sql
HOST_NAME()
```

## SQL-Beispiele

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
