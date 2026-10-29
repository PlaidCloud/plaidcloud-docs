---
title: 转换函数 (Lakehouse v1)
description: "Lakehouse v1 SQL 转换函数：在类型之间转换值，包括 CAST、TRY_CAST 以及解析和格式化辅助函数。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/index.md
---

本节提供 PlaidCloud Lakehouse 中转换函数的参考信息。

## 函数

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
- [TO_STRING（转换，Lakehouse v1）](to-string/)
- [TO_TEXT](to-text/)
- [TO_UINT16](to-uint16/)
- [TO_UINT32](to-uint32/)
- [TO_UINT64](to-uint64/)
- [TO_UINT8](to-uint8/)
- [TO_VARCHAR](to-varchar/)
- [TO_VARIANT](to-variant/)
- [TRY_CAST](try-cast/)
- [TRY_TO_BINARY](try-to-binary/)

请注意，将值从一种类型转换为另一种类型时：

- 将浮点数、十进制数或字符串转换为整数或带小数部分的十进制数时，PlaidCloud Lakehouse 会将值四舍五入为最接近的整数。这由设置 `numeric_cast_option`（默认为 'rounding'）决定，该设置控制数值转换操作的行为。当 `numeric_cast_option` 显式设置为 'truncating' 时，PlaidCloud Lakehouse 会截断小数部分，丢弃所有小数值。

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

    下表汇总了数值转换操作，列出了不同源数值数据类型与目标数值数据类型之间可进行的转换。请注意，其中规定了 String 转换为 Integer 的要求：源字符串必须包含整数值。

    | 源类型    | 目标类型 |
    |----------------|-------------|
    | String         | Decimal     |
    | Float          | Decimal     |
    | Decimal        | Decimal     |
    | Float          | Int         |
    | Decimal        | Int         |
    | String (Int)   | Int         |


- PlaidCloud Lakehouse 还提供多种函数，用于将表达式转换为不同的日期和时间格式。有关详细信息，请参阅[日期和时间函数](../05-datetime-functions)。
