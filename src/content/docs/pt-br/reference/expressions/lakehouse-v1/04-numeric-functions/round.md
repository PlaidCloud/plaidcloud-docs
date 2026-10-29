---
title: ROUND (Lakehouse v1)
description: ROUND — arredonda o argumento x para d casas decimais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/round.md
---

Arredonda o argumento x para d casas decimais. O algoritmo de arredondamento depende do tipo de dados de x. d assume 0 como padrão se não for especificado. d pode ser negativo para fazer com que d dígitos à esquerda da vírgula decimal do valor x se tornem zero. O valor absoluto máximo de d é 30; qualquer dígito além de 30 (ou -30) é truncado.

Ao usar o resultado desta função em cálculos, fique atento a possíveis problemas de precisão, pois o tipo de dados de retorno é DOUBLE, o que pode afetar a exatidão final:

```sql
SELECT ROUND(4/7, 4) - ROUND(3/7, 4); -- Result: 0.14280000000000004
SELECT ROUND(4/7, 4)::DECIMAL(8,4) - ROUND(3/7, 4)::DECIMAL(8,4); -- Result: 0.1428
```

## Sintaxe do Analyze

```python
func.round( <x, d> )
```

## Exemplos do Analyze

```python
func.round(0.123, 2)

┌──────────────────────┐
│ func.round(0.123, 2) │
├──────────────────────┤
│                 0.12 │
└──────────────────────┘
```

## Sintaxe SQL

```sql
ROUND( <x, d> )
```

## Exemplos de SQL

```sql
SELECT ROUND(0.123, 2);

┌─────────────────┐
│ round(0.123, 2) │
├─────────────────┤
│ 0.12            │
└─────────────────┘
```
