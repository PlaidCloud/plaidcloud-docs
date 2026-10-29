---
title: TRUNCATE (Lakehouse v1)
description: TRUNCATE — devolve o número x, truncado a d casas decimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

Devolve o número `x`, truncado a `d` casas decimais. Se `d` for 0, o resultado não tem vírgula decimal nem parte fracionária. `d` pode ser negativo, o que faz com que `d` dígitos à esquerda da vírgula decimal do valor `x` passem a zero. O valor absoluto máximo de `d` é 30; os dígitos além de 30 (ou -30) são truncados.

## Sintaxe do Analyze

```python
func.truncate( <x, d> )
```

## Exemplos do Analyze

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
TRUNCATE( <x, d> )
```

## Exemplos SQL

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
