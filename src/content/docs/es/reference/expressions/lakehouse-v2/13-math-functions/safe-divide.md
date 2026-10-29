---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE — una función de PlaidCloud que divide dos números y devuelve un valor de su elección en lugar de fallar cuando el denominador es cero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/safe-divide.md
---

Una función de PlaidCloud, disponible en todos los motores de lakehouse. Divide el primer número entre el segundo. Cuando el denominador es cero, o cualquiera de los dos lados es NULL, el resultado es NULL, a menos que se indique un tercer valor; en ese caso, se devuelve dicho valor. Ambos lados se convierten primero a `DECIMAL(38, 10)`, de modo que las columnas de enteros se dividen sin truncamiento.

## Sintaxis de Analyze

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
```

## Ejemplos de Analyze

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

## Equivalente en SQL

No existe ninguna función SQL con este nombre. La expresión se compila como:

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

Sin el tercer argumento no hay COALESCE, y un denominador igual a cero da como resultado NULL:

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
