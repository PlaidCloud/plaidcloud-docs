---
title: 변환 함수 (Lakehouse v1)
description: "Lakehouse v1 SQL 변환 함수: CAST, TRY_CAST, 구문 분석 및 서식 도우미로 형식 간에 값을 캐스팅합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/index.md
---

이 섹션에서는 PlaidCloud Lakehouse의 변환 함수에 대한 레퍼런스 정보를 제공합니다.

## 함수

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
- [TO_STRING (변환, Lakehouse v1)](to-string/)
- [TO_TEXT](to-text/)
- [TO_UINT16](to-uint16/)
- [TO_UINT32](to-uint32/)
- [TO_UINT64](to-uint64/)
- [TO_UINT8](to-uint8/)
- [TO_VARCHAR](to-varchar/)
- [TO_VARIANT](to-variant/)
- [TRY_CAST](try-cast/)
- [TRY_TO_BINARY](try-to-binary/)

값을 한 형식에서 다른 형식으로 변환할 때는 다음 사항에 유의하십시오.

- 부동 소수점, 십진수 또는 문자열을 정수나 소수부가 있는 십진수로 변환하면 PlaidCloud Lakehouse는 값을 가장 가까운 정수로 반올림합니다. 이는 숫자 캐스팅 동작을 제어하는 설정 `numeric_cast_option`(기본값은 'rounding')에 따라 결정됩니다. `numeric_cast_option`을 'truncating'으로 명시적으로 설정하면 PlaidCloud Lakehouse는 소수 부분을 잘라 내어 소수값을 버립니다.

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

    아래 표는 숫자 캐스팅 작업을 요약하여 서로 다른 소스 숫자 데이터 형식과 대상 숫자 데이터 형식 간에 가능한 캐스팅을 보여 줍니다. 문자열을 정수로 캐스팅하려면 소스 문자열에 정수 값이 있어야 한다는 요구 사항도 함께 명시되어 있습니다.

    | 소스 형식 | 대상 형식 |
    |----------------|-------------|
    | String         | Decimal     |
    | Float          | Decimal     |
    | Decimal        | Decimal     |
    | Float          | Int         |
    | Decimal        | Int         |
    | String (Int)   | Int         |


- PlaidCloud Lakehouse는 식을 다양한 날짜 및 시간 형식으로 변환하는 여러 함수도 제공합니다. 자세한 내용은 [날짜 및 시간 함수](../05-datetime-functions)를 참조하십시오.
