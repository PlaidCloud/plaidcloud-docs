---
title: CONNECTION_ID (Lakehouse v1)
description: CONNECTION_ID — retorna o ID da conexão atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/connection-id.md
---

Retorna o ID da conexão atual.

## Sintaxe no Analyze

```python
func.connection_id()
```

## Exemplos no Analyze

```python
func.connection_id()

┌──────────────────────────────────────┐
│       func.connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```

## Sintaxe SQL

```sql
CONNECTION_ID()
```

## Exemplos de SQL

```sql
SELECT CONNECTION_ID();

┌──────────────────────────────────────┐
│            connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```
