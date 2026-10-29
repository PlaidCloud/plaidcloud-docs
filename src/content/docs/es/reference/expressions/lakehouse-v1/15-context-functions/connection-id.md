---
title: CONNECTION_ID (Lakehouse v1)
description: CONNECTION_ID devuelve el ID de la conexión actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/connection-id.md
---

Devuelve el ID de la conexión actual.

## Sintaxis de Analyze

```python
func.connection_id()
```

## Ejemplos de Analyze

```python
func.connection_id()

┌──────────────────────────────────────┐
│       func.connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
CONNECTION_ID()
```

## Ejemplos de SQL

```sql
SELECT CONNECTION_ID();

┌──────────────────────────────────────┐
│            connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```
