---
title: MAX (Lakehouse v1)
description: "MAX : renvoie la valeur maximale d'un ensemble de valeurs."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-max.md
---

Fonction d'agrégation.

La fonction MAX() renvoie la valeur maximale d'un ensemble de valeurs.

## Syntaxe Analyze

```python
func.max(<column>)
```

## Exemples Analyze

```python
table.city, func.max(table.temperature).alias('max_temperature')

|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```

## Syntaxe SQL

```sql
MAX(<expr>)
```

## Arguments

| Arguments | Description |
|-----------| ----------- |
| `<expr>`  | Toute expression |

## Type de retour

La valeur maximale, dans le type de cette valeur.

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE temperatures (
  id INT,
  city VARCHAR,
  temperature FLOAT
);

INSERT INTO temperatures (id, city, temperature)
VALUES (1, 'New York', 30),
       (2, 'New York', 28),
       (3, 'New York', 32),
       (4, 'Los Angeles', 25),
       (5, 'Los Angeles', 27);
```

**Exemple de requête : trouver la température maximale pour la ville de New York**

```sql
SELECT city, MAX(temperature) AS max_temperature
FROM temperatures
WHERE city = 'New York'
GROUP BY city;
```

**Résultat**
```sql
|    city    | max_temperature |
|------------|-----------------|
| New York   |       32        |
```
