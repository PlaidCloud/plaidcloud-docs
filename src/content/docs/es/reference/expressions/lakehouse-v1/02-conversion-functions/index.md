---
title: Funciones de conversión (Lakehouse v1)
description: "Funciones de conversión SQL de Lakehouse v1: convierta valores entre tipos con CAST, TRY_CAST y funciones auxiliares de análisis y formato."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/index.md
---

Esta sección ofrece información de referencia sobre las funciones de conversión de PlaidCloud Lakehouse.

## Funciones

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
- [TO_STRING (Conversion, Lakehouse v1)](to-string/)
- [TO_TEXT](to-text/)
- [TO_UINT16](to-uint16/)
- [TO_UINT32](to-uint32/)
- [TO_UINT64](to-uint64/)
- [TO_UINT8](to-uint8/)
- [TO_VARCHAR](to-varchar/)
- [TO_VARIANT](to-variant/)
- [TRY_CAST](try-cast/)
- [TRY_TO_BINARY](try-to-binary/)

Tenga en cuenta lo siguiente al convertir un valor de un tipo a otro:

- Al convertir desde números de punto flotante, números decimales o cadenas a enteros o a números decimales con parte fraccionaria, PlaidCloud Lakehouse redondea los valores al entero más cercano. Esto lo determina la configuración `numeric_cast_option` (por defecto 'rounding'), que controla el comportamiento de las conversiones numéricas. Cuando `numeric_cast_option` se establece explícitamente en 'truncating', PlaidCloud Lakehouse trunca la parte decimal y descarta cualquier valor fraccionario.

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

    La siguiente tabla resume las conversiones numéricas y destaca las posibilidades de conversión entre distintos tipos de datos numéricos de origen y de destino. Tenga en cuenta que especifica el requisito para convertir de cadena a entero: la cadena de origen debe contener un valor entero.

    | Tipo de origen | Tipo de destino |
    |----------------|-----------------|
    | Cadena         | Decimal         |
    | Flotante       | Decimal         |
    | Decimal        | Decimal         |
    | Flotante       | Entero          |
    | Decimal        | Entero          |
    | Cadena (entero)| Entero          |


- PlaidCloud Lakehouse también ofrece diversas funciones para convertir expresiones a distintos formatos de fecha y hora. Para obtener más información, consulte [Funciones de fecha y hora](../05-datetime-functions).
