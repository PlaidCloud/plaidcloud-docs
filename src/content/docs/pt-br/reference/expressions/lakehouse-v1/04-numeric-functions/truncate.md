---
title: TRUNCATE (Lakehouse v1)
description: TRUNCATE — retorna o número x truncado em d casas decimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

Retorna o número `x` truncado em `d` casas decimais. Se `d` for 0, o resultado não tem vírgula decimal nem parte fracionária. `d` pode ser negativo para fazer com que `d` dígitos à esquerda da vírgula decimal do valor `x` se tornem zero. O valor absoluto máximo de `d` é 30; qualquer dígito além de 30 (ou -30) é truncado.

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

## Exemplos de SQL

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
