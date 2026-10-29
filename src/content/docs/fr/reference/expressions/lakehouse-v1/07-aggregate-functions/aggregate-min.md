---
title: MIN (Lakehouse v1)
description: "MIN : renvoie la valeur minimale d'un ensemble de valeurs."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-min.md
---

Fonction d'agrégation.

La fonction MIN() renvoie la valeur minimale d'un ensemble de valeurs.

## Syntaxe Analyze

```python
func.min(<column>)
```

## Exemples Analyze

```python
table.station_id, func.min(table.price).alias('min_price')

| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```

## Syntaxe SQL

```sql
MIN(<expr>)
```

## Arguments

| Arguments | Description    |
|-----------|----------------|
| `<expr>`  | Toute expression |

## Type de retour

La valeur minimale, dans le type de cette valeur.

## Exemples SQL

---
title: MIN
---

Fonction d'agrégation.

La fonction MIN() renvoie la valeur minimale d'un ensemble de valeurs.

## Syntaxe SQL

```sql
MIN(expression)
```

## Arguments

| Arguments   | Description |
| ----------- | ----------- |
| expression  | Toute expression |

## Type de retour

La valeur minimale, dans le type de cette valeur.

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE gas_prices (
  id INT,
  station_id INT,
  price FLOAT
);

INSERT INTO gas_prices (id, station_id, price)
VALUES (1, 1, 3.50),
       (2, 1, 3.45),
       (3, 1, 3.55),
       (4, 2, 3.40),
       (5, 2, 3.35);
```

**Exemple de requête : trouver le prix minimal de l'essence pour la station 1**
```sql
SELECT station_id, MIN(price) AS min_price
FROM gas_prices
WHERE station_id = 1
GROUP BY station_id;
```

**Résultat**
```sql
| station_id | min_price |
|------------|-----------|
|     1      |   3.45    |
```
