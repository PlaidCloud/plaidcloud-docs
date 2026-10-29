---
title: SKEWNESS (Lakehouse v1)
description: "SKEWNESS : renvoie le coefficient d'asymétrie (asymétrie de la distribution) de toutes les valeurs d'entrée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-skewness.md
---

Fonction d'agrégation.

La fonction `SKEWNESS()` renvoie le coefficient d'asymétrie de toutes les valeurs d'entrée.

## Syntaxe Analyze

```python
func.skewness(<expr>)
```

## Exemples Analyze

```python
func.skewness(table.temperature).alias('temperature_skewness')

| temperature_skewness |
|----------------------|
|      0.68            |
```

## Syntaxe SQL

```sql
SKEWNESS(<expr>)
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

**Exemple de requête : calculer l'asymétrie des données de température**

```sql
SELECT SKEWNESS(temperature) AS temperature_skewness
FROM temperature_data;
```

**Résultat**
```sql
| temperature_skewness |
|----------------------|
|      0.68            |
```
