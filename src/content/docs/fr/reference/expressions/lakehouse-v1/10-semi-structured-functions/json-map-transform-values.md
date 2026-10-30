---
title: JSON_MAP_TRANSFORM_VALUES (Lakehouse v1)
description: JSON_MAP_TRANSFORM_VALUES — applique une transformation à chaque valeur d'un objet JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-values.md
---

Applique une transformation à chaque valeur d'un objet JSON à l'aide d'une expression lambda.

## Syntaxe SQL

```sql
JSON_MAP_TRANSFORM_VALUES(<json_object>, (<key>, <value>) -> <value_transformation>)
```

## Type de retour

Renvoie un objet JSON ayant les mêmes clés que l'objet JSON en entrée, mais dont les valeurs sont modifiées selon la transformation lambda spécifiée.

## Exemples SQL

Cet exemple ajoute « - Special Offer » à la description de chaque produit :

```sql
SELECT JSON_MAP_TRANSFORM_VALUES('{"product1":"laptop", "product2":"phone"}'::VARIANT, (k, v) -> CONCAT(v, ' - Special Offer')) AS promo_descriptions;

┌──────────────────────────────────────────────────────────────────────────┐
│                            promo_descriptions                            │
├──────────────────────────────────────────────────────────────────────────┤
│ {"product1":"laptop - Special Offer","product2":"phone - Special Offer"} │
└──────────────────────────────────────────────────────────────────────────┘
```
