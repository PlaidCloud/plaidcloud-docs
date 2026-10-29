---
title: SAFE_DIVIDE (Lakehouse v1)
description: SAFE_DIVIDE — fonction PlaidCloud qui divise deux nombres et renvoie la valeur de votre choix au lieu d'échouer lorsque le dénominateur est nul.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/safe-divide.md
---

Fonction PlaidCloud, disponible sur tous les moteurs lakehouse. Divise le premier nombre par le second. Lorsque le dénominateur est nul, ou que l'un des deux côtés est NULL, le résultat est la troisième valeur ; passez `None` pour obtenir NULL. Les trois arguments sont obligatoires sur Lakehouse v1. Les deux côtés sont d'abord convertis en `DECIMAL(38, 10)`, de sorte que les colonnes entières se divisent sans troncature.

## Syntaxe Analyze

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)
```

## Exemples Analyze

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

## Équivalent SQL

Il n'existe aucune fonction SQL de ce nom. L'expression est compilée en :

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```
