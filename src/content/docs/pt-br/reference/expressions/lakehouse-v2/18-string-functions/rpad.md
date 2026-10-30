---
title: RPAD (Lakehouse v2)
description: RPAD — preenche uma string à direita até um comprimento especificado usando uma string de preenchimento.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

Preenche uma string à direita até um comprimento especificado usando uma string de preenchimento.

## Sintaxe do Analyze

```python
func.rpad(<str>, <len>, <pad>)
```

## Exemplos do Analyze

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## Sintaxe SQL

```sql
RPAD(<str>, <len>, <pad>)
```

## Exemplos de SQL

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
