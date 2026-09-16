---
title: Conversion Functions (Lakehouse v1)
description: "Lakehouse v1 SQL conversion functions: cast values between types — CAST, TRY_CAST, parse, and format helpers."
---

This section provides reference information for the conversion functions in PlaidCloud Lakehouse.

## Functions

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

Please note the following when converting a value from one type to another:

- When converting from floating-point, decimal numbers, or strings to integers or decimal numbers with fractional parts, PlaidCloud Lakehouse rounds the values to the nearest integer. This is determined by the setting `numeric_cast_option` (defaults to 'rounding') which controls the behavior of numeric casting operations. When `numeric_cast_option` is explicitly set to 'truncating', PlaidCloud Lakehouse will truncate the decimal part, discarding any fractional values.

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

    The table below presents a summary of numeric casting operations, highlighting the casting possibilities between different source and target numeric data types. Please note that, it specifies the requirement for String to Integer casting, where the source string must contain an integer value.

    | Source Type    | Target Type |
    |----------------|-------------|
    | String         | Decimal     |
    | Float          | Decimal     |
    | Decimal        | Decimal     |
    | Float          | Int         |
    | Decimal        | Int         |
    | String (Int)   | Int         |


- PlaidCloud Lakehouse also offers a variety of functions for converting expressions into different date and time formats. For more information, see [Date & Time Functions](../05-datetime-functions).
