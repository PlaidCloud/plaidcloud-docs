---
title: INSPECT_ALL_PIPES (Lakehouse v2)
description: INSPECT_ALL_PIPES — devolve informação sobre todos os objetos pipe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-all-pipes.md
---

Devolve informação sobre todos os objetos pipe.

## Sintaxe do Analyze

```python
func.inspect_all_pipes()
```

## Exemplos do Analyze

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## Sintaxe SQL

```sql
INSPECT_ALL_PIPES()
```

## Exemplos SQL

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```
