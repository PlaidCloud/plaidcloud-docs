---
title: SPACE (Lakehouse v2)
description: SPACE — Retorna uma string formada por um número especificado de espaços.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/space.md
---

Retorna uma string formada por um número especificado de espaços.

## Sintaxe do Analyze

```python
func.space(<n>)
```

## Exemplos do Analyze

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## Sintaxe SQL

```sql
SPACE(<n>)
```

## Exemplos de SQL

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```
