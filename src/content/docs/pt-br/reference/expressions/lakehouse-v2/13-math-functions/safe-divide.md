---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE — uma função do PlaidCloud que divide dois números e retorna um valor à sua escolha, em vez de falhar, quando o denominador é zero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/safe-divide.md
---

Uma função do PlaidCloud, disponível em todos os mecanismos de lakehouse. Divide o primeiro número pelo segundo. Quando o denominador é zero, ou quando qualquer um dos lados é NULL, o resultado é NULL, a menos que um terceiro valor seja informado; nesse caso, esse valor é retornado. Os dois lados são convertidos primeiro para `DECIMAL(38, 10)`, de modo que colunas de inteiros sejam divididas sem truncamento.

## Sintaxe do Analyze

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
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

Não existe uma função SQL com esse nome. A expressão é compilada para:

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

Sem o terceiro argumento, não há COALESCE, e um denominador zero resulta em NULL:

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
