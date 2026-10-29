---
title: INSPECT_RELATED_MV (Lakehouse v2)
description: INSPECT_RELATED_MV — Retorna as visões materializadas relacionadas a uma tabela.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-related-mv.md
---

Retorna as visões materializadas relacionadas a uma tabela.

## Sintaxe do Analyze

```python
func.inspect_related_mv(<db>, <table>)
```

## Exemplos do Analyze

```python
func.inspect_related_mv('mydb', 'my_table')

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```

## Sintaxe SQL

```sql
INSPECT_RELATED_MV(<db>, <table>)
```

## Exemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_RELATED_MV('mydb', 'my_table'));

┌───────────────┐
│ (related mvs)  │
└───────────────┘
```
