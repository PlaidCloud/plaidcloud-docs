---
title: ASCII (Lakehouse v2)
description: ASCII — devolve o código ASCII do primeiro caráter de uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

Devolve o código ASCII do primeiro caráter de uma cadeia.

## Sintaxe do Analyze

```python
func.ascii(<str>)
```

## Exemplos do Analyze

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## Sintaxe SQL

```sql
ASCII(<str>)
```

## Exemplos SQL

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
