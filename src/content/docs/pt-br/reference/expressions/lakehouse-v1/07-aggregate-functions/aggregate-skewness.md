---
title: SKEWNESS (Lakehouse v1)
description: SKEWNESS — retorna a assimetria (da distribuição) de todos os valores de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-skewness.md
---

Função de agregação.

A função `SKEWNESS()` retorna a assimetria de todos os valores de entrada.

## Sintaxe do Analyze

```python
func.skewness(<expr>)
```

## Exemplos do Analyze

```python
func.skewness(table.temperature).alias('temperature_skewness')

| temperature_skewness |
|----------------------|
|      0.68            |
```

## Sintaxe SQL

```sql
SKEWNESS(<expr>)
```

## Argumentos

| Argumentos | Descrição                       |
|-----------| -----------                     |
| `<expr>`  | Qualquer expressão numérica     |

## Tipo de retorno

Float64 anulável.

## Exemplos de SQL

**Criar uma tabela e inserir dados de exemplo**
```sql
CREATE TABLE temperature_data (
                                  id INT,
                                  city_id INT,
                                  temperature FLOAT
);

INSERT INTO temperature_data (id, city_id, temperature)
VALUES (1, 1, 60),
       (2, 1, 65),
       (3, 1, 62),
       (4, 2, 70),
       (5, 2, 75);
```

**Demonstração de consulta: calcular a assimetria dos dados de temperatura**

```sql
SELECT SKEWNESS(temperature) AS temperature_skewness
FROM temperature_data;
```

**Resultado**
```sql
| temperature_skewness |
|----------------------|
|      0.68            |
```
