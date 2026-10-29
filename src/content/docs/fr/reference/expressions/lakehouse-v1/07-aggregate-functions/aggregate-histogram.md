---
title: HISTOGRAM (Lakehouse v1)
description: "HISTOGRAM : génère un histogramme de distribution des données selon une stratégie de regroupement en buckets de hauteur égale."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-histogram.md
---

Génère un histogramme de distribution des données selon une stratégie de regroupement en buckets de « hauteur égale ».

## Syntaxe Analyze

```python
func.histogram(<expr>)
```

## Exemples Analyze
Consultez l'exemple SQL pour plus de détails.

## Syntaxe SQL

```sql
HISTOGRAM(<expr>)

-- The following two forms are equivalent:
HISTOGRAM(<max_num_buckets>)(<expr>)
HISTOGRAM(<expr> [, <max_num_buckets>])
```

| Paramètre         | Description                                                                         |
|-------------------|-------------------------------------------------------------------------------------|
| `expr`            | Le type de données de `expr` doit pouvoir être trié.                                |
| `max_num_buckets` | Entier positif facultatif indiquant le nombre maximal de buckets. La valeur par défaut est 128. |

## Type de retour

Renvoie soit une chaîne vide, soit un objet JSON ayant la structure suivante :

- **buckets** : liste des buckets avec des informations détaillées :
  - **lower** : borne inférieure du bucket.
  - **upper** : borne supérieure du bucket.
  - **count** : nombre d'éléments dans le bucket.
  - **pre_sum** : nombre cumulé d'éléments jusqu'au bucket courant.
  - **ndv** : nombre de valeurs distinctes dans le bucket.

## Exemples SQL

Cet exemple montre comment la fonction HISTOGRAM analyse la distribution des valeurs de `c_int` dans la table `histagg`, en renvoyant les limites des buckets, le nombre de valeurs distinctes, le nombre d'éléments et les nombres cumulés :

```sql
CREATE TABLE histagg (
  c_id INT,
  c_tinyint TINYINT,
  c_smallint SMALLINT,
  c_int INT
);

INSERT INTO histagg VALUES
  (1, 10, 20, 30),
  (1, 11, 21, 33),
  (1, 11, 12, 13),
  (2, 21, 22, 23),
  (2, 31, 32, 33),
  (2, 10, 20, 30);

SELECT HISTOGRAM(c_int) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                              histogram(c_int)                                                                                                             │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"13","ndv":1,"count":1,"pre_sum":0},{"lower":"23","upper":"23","ndv":1,"count":1,"pre_sum":1},{"lower":"30","upper":"30","ndv":1,"count":2,"pre_sum":2},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Le résultat est renvoyé sous la forme d'un tableau JSON :

```json
[
  {
    "lower": "13",
    "upper": "13",
    "ndv": 1,
    "count": 1,
    "pre_sum": 0
  },
  {
    "lower": "23",
    "upper": "23",
    "ndv": 1,
    "count": 1,
    "pre_sum": 1
  },
  {
    "lower": "30",
    "upper": "30",
    "ndv": 1,
    "count": 2,
    "pre_sum": 2
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```

Cet exemple montre comment `HISTOGRAM(2)` regroupe les valeurs de c_int en deux buckets :

```sql
SELECT HISTOGRAM(2)(c_int) FROM histagg;
-- Or
SELECT HISTOGRAM(c_int, 2) FROM histagg;

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                  histogram(2)(c_int)                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ [{"lower":"13","upper":"30","ndv":3,"count":4,"pre_sum":0},{"lower":"33","upper":"33","ndv":1,"count":2,"pre_sum":4}] │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

Le résultat est renvoyé sous la forme d'un tableau JSON :

```json
[
  {
    "lower": "13",
    "upper": "30",
    "ndv": 3,
    "count": 4,
    "pre_sum": 0
  },
  {
    "lower": "33",
    "upper": "33",
    "ndv": 1,
    "count": 2,
    "pre_sum": 4
  }
]
```
