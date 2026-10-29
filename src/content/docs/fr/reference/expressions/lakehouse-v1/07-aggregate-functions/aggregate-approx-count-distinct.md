---
title: APPROX_COUNT_DISTINCT (Lakehouse v1)
description: "APPROX_COUNT_DISTINCT : estime le nombre de valeurs distinctes d'un jeu de données avec l'algorithme HyperLogLog."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-approx-count-distinct.md
---

Estime le nombre de valeurs distinctes d'un jeu de données avec l'algorithme [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog). 

L'algorithme HyperLogLog fournit une approximation du nombre d'éléments uniques en consommant peu de mémoire et de temps. Envisagez d'utiliser cette fonction avec de grands jeux de données lorsqu'un résultat estimé est acceptable. Au prix d'une certaine précision, c'est une méthode rapide et efficace pour obtenir un nombre de valeurs distinctes.

Pour obtenir un résultat exact, utilisez [COUNT_DISTINCT](../aggregate-count-distinct). Consultez les [exemples](#exemples-sql) pour plus d'explications.

## Syntaxe Analyze

```python
func.approx_count_distinct(<expr>)
```

## Exemples Analyze

```python
func.approx_count_distinct(table.user_id).alias('approx_distinct_user_count')

| approx_distinct_user_count |
|----------------------------|
|             4              |
```

## Syntaxe SQL

```sql
APPROX_COUNT_DISTINCT(<expr>)
```

## Type de retour

Entier.

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_name VARCHAR
);

INSERT INTO user_events (id, user_id, event_name)
VALUES (1, 1, 'Login'),
       (2, 2, 'Login'),
       (3, 3, 'Login'),
       (4, 1, 'Logout'),
       (5, 2, 'Logout'),
       (6, 4, 'Login'),
       (7, 1, 'Login');
```

**Exemple de requête : estimer le nombre d'ID utilisateur distincts**
```sql
SELECT APPROX_COUNT_DISTINCT(user_id) AS approx_distinct_user_count
FROM user_events;
```

**Résultat**
```sql
| approx_distinct_user_count |
|----------------------------|
|             4              |
```
