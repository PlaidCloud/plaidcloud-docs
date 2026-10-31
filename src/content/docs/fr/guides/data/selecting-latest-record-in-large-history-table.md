---
title: Sélectionner le dernier enregistrement d'une grande table d'historique des versions
description: Apprenez à sélectionner efficacement le dernier enregistrement dans de grandes tables d'historique de PlaidCloud grâce à des techniques de requête optimisées.
sidebar:
  label: Sélectionner le dernier enregistrement d'une grande table d'historique des versions
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## Problème

Vous disposez d'une table qui contient de nombreuses versions de chaque enregistrement, mais vous devez utiliser la dernière version.

## Discussion

Ce problème pourrait être résolu en sélectionnant l'ID et la date de mise à jour maximale (MAX) dans une table temporaire, puis en réalisant une jointure INNER JOIN de cette table temporaire avec la table d'historique pour obtenir le résultat. Malheureusement, cela exige deux étapes et le stockage d'une table intermédiaire qui n'a d'autre fonction que de trouver la dernière mise à jour.

La solution la plus élégante, qui réalise cette opération en une seule requête, utilise une fonction de fenêtrage avec un tri et un filtre.

## Solution

### La table d'historique des versions

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### Configuration de l'étape
À l'aide d'une étape d'extraction, créez une expression de fonction de fenêtrage dans une colonne nommée `Rank`, comme ceci :

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

Dans l'onglet de filtre de l'étape Extract, définissez un filtre comme celui-ci :

```python
table.Rank == 1
```

### Le résultat

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

Cette approche est très efficace et permet de sélectionner le dernier enregistrement d'une table d'historique multiversion en une seule étape. Elle fonctionne en classant chaque enregistrement au sein du groupe `employee_id` selon `update_date`, puis en ne retenant que le premier enregistrement.

Si plusieurs colonnes composent la clé unique d'une ligne, vous pouvez les ajouter à l'argument `partition_by` sous forme de liste, comme ceci :

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

Si vous avez besoin de tris sur plusieurs colonnes, vous pouvez également les appliquer avec une liste de colonnes, comme ceci :

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
