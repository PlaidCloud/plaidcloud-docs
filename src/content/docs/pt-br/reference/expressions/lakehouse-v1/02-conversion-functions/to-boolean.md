---
title: TO_BOOLEAN (Lakehouse v1)
description: TO_BOOLEAN converte um valor para o tipo de dados BOOLEAN.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-boolean.md
---

Converte um valor para o tipo de dados BOOLEAN.

## Sintaxe do Analyze

```python
func.to_boolean( <expr> )
```

## Exemplos do Analyze

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## Sintaxe SQL

```sql
TO_BOOLEAN( <expr> )
```

## Exemplos de SQL

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```
