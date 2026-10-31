---
title: INSPECT_MV_RELATIONSHIPS (Lakehouse v2)
description: INSPECT_MV_RELATIONSHIPS — devolve as relações de dependência de uma vista materializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-relationships.md
---

Devolve as relações de dependência de uma vista materializada.

## Sintaxe do Analyze

```python
func.inspect_mv_relationships(<db>, <mv>)
```

## Exemplos do Analyze

```python
func.inspect_mv_relationships('mydb', 'my_mv')

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```

## Sintaxe SQL

```sql
INSPECT_MV_RELATIONSHIPS(<db>, <mv>)
```

## Exemplos SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_RELATIONSHIPS('mydb', 'my_mv'));

┌─────────────────┐
│ (relationships)  │
└─────────────────┘
```
