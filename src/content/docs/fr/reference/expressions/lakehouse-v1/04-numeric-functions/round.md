---
title: ROUND (Lakehouse v1)
description: ROUND — arrondit l'argument x à d décimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/round.md
---

Arrondit l'argument x à d décimales. L'algorithme d'arrondi dépend du type de données de x. d vaut 0 par défaut s'il n'est pas spécifié. d peut être négatif pour mettre à zéro d chiffres à gauche de la virgule de la valeur x. La valeur absolue maximale de d est 30 ; tout chiffre au-delà de 30 (ou -30) est tronqué.

Lorsque vous utilisez le résultat de cette fonction dans des calculs, tenez compte des éventuels problèmes de précision : son type de données de retour est DOUBLE, ce qui peut affecter l'exactitude du résultat final :

```sql
SELECT ROUND(4/7, 4) - ROUND(3/7, 4); -- Result: 0.14280000000000004
SELECT ROUND(4/7, 4)::DECIMAL(8,4) - ROUND(3/7, 4)::DECIMAL(8,4); -- Result: 0.1428
```

## Syntaxe Analyze

```python
func.round( <x, d> )
```

## Exemples Analyze

```python
func.round(0.123, 2)

┌──────────────────────┐
│ func.round(0.123, 2) │
├──────────────────────┤
│                 0.12 │
└──────────────────────┘
```

## Syntaxe SQL

```sql
ROUND( <x, d> )
```

## Exemples SQL

```sql
SELECT ROUND(0.123, 2);

┌─────────────────┐
│ round(0.123, 2) │
├─────────────────┤
│ 0.12            │
└─────────────────┘
```
