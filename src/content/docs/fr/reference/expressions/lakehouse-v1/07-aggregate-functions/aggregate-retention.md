---
title: RETENTION (Lakehouse v1)
description: "RETENTION : fonction d'agrégation."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-retention.md
---

Fonction d'agrégation

La fonction RETENTION() prend en arguments un ensemble de 1 à 32 conditions de type UInt8 indiquant si une certaine condition a été remplie pour l'événement.

Toute condition peut être spécifiée en argument (comme dans WHERE).

Les conditions, à l'exception de la première, s'appliquent par paires : le résultat de la deuxième sera vrai si la première et la deuxième sont vraies, celui de la troisième si la première et la troisième sont vraies, etc.

## Syntaxe Analyze

```python
func.retention(<cond1> , <cond2> , ..., <cond32>)
```

## Exemples Analyze

```python
table.user_id, func.retention(table.event_type=='signup', table.event_type='login', table.event_type='purchase').alias('sales_amounts')

| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```

## Syntaxe SQL

```sql
RETENTION( <cond1> , <cond2> , ..., <cond32> );
```

## Arguments

| Arguments | Description                                 |
|-----------|---------------------------------------------|
| `<cond>`  | Une expression qui renvoie un résultat booléen |

## Type de retour

Le tableau de 1 ou de 0.

## Exemples SQL

**Créer une table et insérer des données d'exemple**
```sql
CREATE TABLE user_events (
  id INT,
  user_id INT,
  event_date DATE,
  event_type VARCHAR
);

INSERT INTO user_events (id, user_id, event_date, event_type)
VALUES (1, 1, '2022-01-01', 'signup'),
       (2, 1, '2022-01-02', 'login'),
       (3, 2, '2022-01-01', 'signup'),
       (4, 2, '2022-01-03', 'purchase'),
       (5, 3, '2022-01-01', 'signup'),
       (6, 3, '2022-01-02', 'login');
```

**Exemple de requête : calculer la rétention des utilisateurs selon les événements d'inscription, de connexion et d'achat**
```sql
SELECT
  user_id,
  RETENTION(event_type = 'signup', event_type = 'login', event_type = 'purchase') AS retention
FROM user_events
GROUP BY user_id;
```

**Résultat**
```sql
| user_id | retention |
|---------|-----------|
|   1     | [1, 1, 0] |
|   2     | [1, 0, 1] |
|   3     | [1, 1, 0] |
```
