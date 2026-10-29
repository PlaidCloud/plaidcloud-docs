---
title: UCASE (Lakehouse v2)
description: UCASE — converte uma string para maiúsculas. Alias de `UPPER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ucase.md
---

Converte uma string para maiúsculas. Alias de `UPPER`.

## Sintaxe do Analyze

```python
func.ucase(<str>)
```

## Exemplos do Analyze

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## Sintaxe SQL

```sql
UCASE(<str>)
```

## Exemplos de SQL

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
