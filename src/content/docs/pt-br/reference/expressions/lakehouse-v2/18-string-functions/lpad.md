---
title: LPAD (Lakehouse v2)
description: LPAD — preenche uma string à esquerda até um comprimento especificado usando uma string de preenchimento.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

Preenche uma string à esquerda até um comprimento especificado usando uma string de preenchimento.

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

## Exemplos de SQL

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
