---
title: SAFE_DIVIDE (Lakehouse v1)
description: SAFE_DIVIDE — uma função do PlaidCloud que divide dois números e retorna um valor à sua escolha, em vez de falhar, quando o denominador é zero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/safe-divide.md
---

Uma função do PlaidCloud, disponível em todos os mecanismos de lakehouse. Divide o primeiro número pelo segundo. Quando o denominador é zero, ou qualquer um dos lados é NULL, o resultado é o terceiro valor; passe `None` para obter NULL. Os três argumentos são obrigatórios no Lakehouse v1. Os dois lados são convertidos primeiro para `DECIMAL(38, 10)`, de modo que colunas de inteiros sejam divididas sem truncamento.

## Sintaxe do Analyze

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)
```

## Exemplos do Analyze

```python
func.safe_divide(table.revenue, table.units, 0)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | 0           |
| 100     | NULL  | 0           |
```

```python
func.safe_divide(table.revenue, table.units, None)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | NULL        |
```

## Equivalente em SQL

Não existe uma função SQL com este nome. A expressão é compilada para:

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```
