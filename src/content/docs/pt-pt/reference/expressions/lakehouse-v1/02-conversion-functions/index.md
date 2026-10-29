---
title: Funções de conversão (Lakehouse v1)
description: "Funções SQL de conversão do Lakehouse v1: converter valores entre tipos com CAST, TRY_CAST e auxiliares de análise e formatação."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/index.md
---

Esta secção apresenta informação de referência sobre as funções de conversão do PlaidCloud Lakehouse.

## Funções

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
- [TO_STRING (Conversão, Lakehouse v1)](to-string/)
- [TO_TEXT](to-text/)
- [TO_UINT16](to-uint16/)
- [TO_UINT32](to-uint32/)
- [TO_UINT64](to-uint64/)
- [TO_UINT8](to-uint8/)
- [TO_VARCHAR](to-varchar/)
- [TO_VARIANT](to-variant/)
- [TRY_CAST](try-cast/)
- [TRY_TO_BINARY](try-to-binary/)

Tenha em atenção o seguinte ao converter um valor de um tipo para outro:

- Ao converter números de vírgula flutuante, números decimais ou cadeias de caracteres em números inteiros ou decimais com parte fracionária, o PlaidCloud Lakehouse arredonda os valores para o número inteiro mais próximo. Isto é determinado pela definição `numeric_cast_option` (por predefinição, 'rounding'), que controla o comportamento das operações de conversão numérica. Quando `numeric_cast_option` é definida explicitamente como 'truncating', o PlaidCloud Lakehouse trunca a parte decimal, descartando quaisquer valores fracionários.

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

    A tabela abaixo apresenta um resumo das operações de conversão numérica, destacando as possibilidades de conversão entre diferentes tipos de dados numéricos de origem e de destino. Tenha em atenção que especifica o requisito para a conversão de String em Integer, em que a cadeia de caracteres de origem tem de conter um valor inteiro.

    | Tipo de origem | Tipo de destino |
    |----------------|-------------|
    | String         | Decimal     |
    | Float          | Decimal     |
    | Decimal        | Decimal     |
    | Float          | Int         |
    | Decimal        | Int         |
    | String (Int)   | Int         |


- O PlaidCloud Lakehouse também disponibiliza várias funções para converter expressões em diferentes formatos de data e hora. Para mais informações, consulte [Funções de data e hora](../05-datetime-functions).
