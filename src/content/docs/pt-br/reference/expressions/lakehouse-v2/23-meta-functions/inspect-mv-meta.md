---
title: INSPECT_MV_META (Lakehouse v2)
description: INSPECT_MV_META — retorna metadados de uma visão materializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-mv-meta.md
---

Retorna metadados de uma visão materializada.

## Sintaxe do Analyze

```python
func.inspect_mv_meta(<db>, <mv>)
```

## Exemplos do Analyze

```python
func.inspect_mv_meta('mydb', 'my_mv')

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```

## Sintaxe SQL

```sql
INSPECT_MV_META(<db>, <mv>)
```

## Exemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_MV_META('mydb', 'my_mv'));

┌───────────────┐
│ (mv metadata)  │
└───────────────┘
```
