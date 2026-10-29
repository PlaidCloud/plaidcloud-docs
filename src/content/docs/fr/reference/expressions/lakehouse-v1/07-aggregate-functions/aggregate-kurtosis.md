---
title: KURTOSIS (Lakehouse v1)
description: "KURTOSIS : renvoie le kurtosis en excès (aplatissement par rapport à une loi normale) de toutes les valeurs d'entrée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-kurtosis.md
---

Fonction d'agrégation.

La fonction `KURTOSIS()` renvoie le kurtosis en excès de toutes les valeurs d'entrée.

## Syntaxe Analyze

```python
func.kurtosis(<expr>)
```

## Exemples Analyze

```python
func.kurtosis(table.price).alias('excess_kurtosis')

|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```

## Syntaxe SQL

```sql
KURTOSIS(<expr>)
```

## Arguments

| Arguments | Description                     |
|-----------| -----------                     |
| `<expr>`  | Toute expression numérique        |

## Type de retour

Float64 nullable.

## Exemples SQL

**Créer une table et insérer des données d'exemple**
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

**Exemple de requête : calculer le kurtosis en excès du cours de l'action Apple**

```sql
SELECT KURTOSIS(price) AS excess_kurtosis
FROM stock_prices
WHERE stock_symbol = 'AAPL';
```

**Résultat**

```sql
|     excess_kurtosis     |
|-------------------------|
| 0.06818181325581445     |
```
