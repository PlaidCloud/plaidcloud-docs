---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE — fonction PlaidCloud qui divise deux nombres et renvoie la valeur de votre choix au lieu d'échouer lorsque le dénominateur est égal à zéro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/safe-divide.md
---

Fonction PlaidCloud, disponible sur tous les moteurs lakehouse. Divise le premier nombre par le second. Lorsque le dénominateur est égal à zéro, ou que l'un des deux côtés est NULL, le résultat est NULL, sauf si une troisième valeur est fournie : dans ce cas, c'est cette valeur qui est renvoyée. Les deux côtés sont d'abord convertis en `DECIMAL(38, 10)`, ce qui permet aux colonnes d'entiers de se diviser sans troncature.

## Syntaxe Analyze

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
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

Il n'existe pas de fonction SQL de ce nom. L'expression est compilée en :

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

Sans le troisième argument, il n'y a pas de COALESCE, et un dénominateur égal à zéro donne NULL :

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
