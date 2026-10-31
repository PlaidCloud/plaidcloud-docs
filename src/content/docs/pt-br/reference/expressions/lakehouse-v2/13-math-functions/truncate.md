---
title: TRUNCATE (Lakehouse v2)
description: TRUNCATE — trunca um número para um número especificado de casas decimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/truncate.md
---

Trunca um número para um número especificado de casas decimais.

## Sintaxe do Analyze

```python
func.truncate(<x>, <d>)
```

## Exemplos do Analyze

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## Sintaxe SQL

```sql
TRUNCATE(<x>, <d>)
```

## Exemplos de SQL

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
