---
title: "GROUP_CONCAT (Cadeia, Lakehouse v2)"
description: GROUP_CONCAT — concatena os valores de um grupo numa única cadeia com um separador.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/group-concat.md
---

Concatena os valores de um grupo numa única cadeia com um separador.

## Sintaxe do Analyze

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Exemplos do Analyze

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## Sintaxe SQL

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## Exemplos SQL

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
