---
title: LPAD (Lakehouse v2)
description: LPAD — preenche uma cadeia à esquerda até um comprimento especificado com uma cadeia de preenchimento.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

Preenche uma cadeia à esquerda até um comprimento especificado com uma cadeia de preenchimento.

## Sintaxe do Analyze

```python
func.lpad(<str>, <len>, <pad>)
```

## Exemplos do Analyze

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## Sintaxe SQL

```sql
LPAD(<str>, <len>, <pad>)
```

## Exemplos SQL

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
