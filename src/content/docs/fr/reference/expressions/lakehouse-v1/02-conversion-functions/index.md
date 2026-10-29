---
title: Fonctions de conversion (Lakehouse v1)
description: "Fonctions de conversion SQL de Lakehouse v1 : convertir des valeurs d'un type à un autre avec CAST, TRY_CAST et des utilitaires d'analyse et de formatage."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/index.md
---

Cette section fournit des informations de référence sur les fonctions de conversion de PlaidCloud Lakehouse.

## Fonctions

- [BUILD_BITMAP](build-bitmap/)
- [CAST, ::](cast/)
- [TO_BINARY](to-binary/)
- [TO_BITMAP](to-bitmap/)
- [TO_BOOLEAN](to-boolean/)
- [TO_FLOAT32](to-float32/)
- [TO_FLOAT64](to-float64/)
- [TO_HEX](to-hex/)
- [TO_INT16](to-int16/)
- [TO_INT32](to-int32/)
- [TO_INT64](to-int64/)
- [TO_INT8](to-int8/)
- [TO_STRING (conversion, Lakehouse v1)](to-string/)
- [TO_TEXT](to-text/)
- [TO_UINT16](to-uint16/)
- [TO_UINT32](to-uint32/)
- [TO_UINT64](to-uint64/)
- [TO_UINT8](to-uint8/)
- [TO_VARCHAR](to-varchar/)
- [TO_VARIANT](to-variant/)
- [TRY_CAST](try-cast/)
- [TRY_TO_BINARY](try-to-binary/)

À noter lors de la conversion d'une valeur d'un type à un autre :

- Lors de la conversion de nombres à virgule flottante, de nombres décimaux ou de chaînes en entiers ou en nombres décimaux avec partie fractionnaire, PlaidCloud Lakehouse arrondit les valeurs à l'entier le plus proche. Ce comportement est déterminé par le paramètre `numeric_cast_option` (par défaut 'rounding'), qui contrôle le comportement des conversions numériques. Lorsque `numeric_cast_option` est explicitement défini sur 'truncating', PlaidCloud Lakehouse tronque la partie décimale et écarte toute valeur fractionnaire.

    ```sql
    SELECT CAST('0.6' AS DECIMAL(10, 0)), CAST(0.6 AS DECIMAL(10, 0)), CAST(1.5 AS INT);

    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │ cast('0.6' as decimal(10, 0)) │ cast(0.6 as decimal(10, 0)) │ cast(1.5 as int32) │
    ├───────────────────────────────┼─────────────────────────────┼────────────────────┤
    │                             1 │                           1 │                  2 │
    └──────────────────────────────────────────────────────────────────────────────────┘

    SET numeric_cast_option = 'truncating';

    SELECT CAST('0.6' AS DECIMAL(10, 0)), CAST(0.6 AS DECIMAL(10, 0)), CAST(1.5 AS INT);

    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │ cast('0.6' as decimal(10, 0)) │ cast(0.6 as decimal(10, 0)) │ cast(1.5 as int32) │
    ├───────────────────────────────┼─────────────────────────────┼────────────────────┤
    │                             0 │                           0 │                  1 │
    └──────────────────────────────────────────────────────────────────────────────────┘
    ```

    Le tableau ci-dessous résume les conversions numériques et indique les possibilités de conversion entre les différents types de données numériques source et cible. À noter qu'il précise l'exigence pour la conversion d'une chaîne en entier : la chaîne source doit contenir une valeur entière.

    | Type de source | Type cible  |
    |----------------|-------------|
    | Chaîne         | Décimal     |
    | Flottant       | Décimal     |
    | Décimal        | Décimal     |
    | Flottant       | Entier      |
    | Décimal        | Entier      |
    | Chaîne (entier) | Entier     |


- PlaidCloud Lakehouse propose également diverses fonctions pour convertir des expressions en différents formats de date et d'heure. Pour plus d'informations, consultez [Fonctions de date et d'heure](../05-datetime-functions).
