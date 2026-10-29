---
title: RPAD (Lakehouse v2)
description: RPAD — preenche uma cadeia à direita até um comprimento especificado com uma cadeia de preenchimento.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

Preenche uma cadeia à direita até um comprimento especificado com uma cadeia de preenchimento.

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

## Exemplos SQL

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
