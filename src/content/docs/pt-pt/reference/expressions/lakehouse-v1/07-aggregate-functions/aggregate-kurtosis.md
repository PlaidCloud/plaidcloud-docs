---
title: KURTOSIS (Lakehouse v1)
description: KURTOSIS — devolve a curtose em excesso (achatamento face à distribuição normal) de todos os valores de entrada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-kurtosis.md
---

Função de agregação.

A função `KURTOSIS()` devolve a curtose em excesso de todos os valores de entrada.

## Sintaxe do Analyze

```python
func.kurtosis(<expr>)
```

## Exemplos do Analyze

```python
func.kurtosis(table.price).alias('excess_kurtosis')

|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```

## Sintaxe SQL

```sql
KURTOSIS(<expr>)
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
CREATE TABLE stock_prices (
  id INT,
  stock_symbol VARCHAR,
  price FLOAT
);

INSERT INTO stock_prices (id, stock_symbol, price)
VALUES (1, 'AAPL', 150),
       (2, 'AAPL', 152),
       (3, 'AAPL', 148),
       (4, 'AAPL', 160),
       (5, 'AAPL', 155);
```

**Exemplo de consulta: calcular a curtose em excesso dos preços das ações da Apple**

```sql
SELECT KURTOSIS(price) AS excess_kurtosis
FROM stock_prices
WHERE stock_symbol = 'AAPL';
```

**Resultado**

```sql
|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```
