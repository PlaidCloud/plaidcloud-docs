---
title: Funkcje konwersji (Lakehouse v1)
description: "Funkcje konwersji SQL w Lakehouse v1: rzutowanie wartości między typami — CAST, TRY_CAST oraz funkcje analizy i formatowania."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/index.md
---

Ta sekcja zawiera informacje referencyjne o funkcjach konwersji w PlaidCloud Lakehouse.

## Funkcje

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
- [TO_STRING (konwersja, Lakehouse v1)](to-string/)
- [TO_TEXT](to-text/)
- [TO_UINT16](to-uint16/)
- [TO_UINT32](to-uint32/)
- [TO_UINT64](to-uint64/)
- [TO_UINT8](to-uint8/)
- [TO_VARCHAR](to-varchar/)
- [TO_VARIANT](to-variant/)
- [TRY_CAST](try-cast/)
- [TRY_TO_BINARY](try-to-binary/)

Uwaga: przy konwersji wartości z jednego typu na inny należy pamiętać o następujących kwestiach:

- Podczas konwersji z liczb zmiennoprzecinkowych, liczb dziesiętnych lub ciągów znaków na liczby całkowite albo liczby dziesiętne z częścią ułamkową PlaidCloud Lakehouse zaokrągla wartości do najbliższej liczby całkowitej. Określa to ustawienie `numeric_cast_option` (domyślnie 'rounding'), które steruje zachowaniem numerycznych operacji rzutowania. Gdy `numeric_cast_option` zostanie jawnie ustawione na 'truncating', PlaidCloud Lakehouse obcina część dziesiętną, odrzucając wszelkie wartości ułamkowe.

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

    Poniższa tabela podsumowuje numeryczne operacje rzutowania i wskazuje możliwości rzutowania między różnymi źródłowymi i docelowymi numerycznymi typami danych. Uwaga: określa ona wymaganie dla rzutowania ze String na Integer — źródłowy ciąg znaków musi zawierać wartość całkowitą.

    | Typ źródła     | Typ docelowy |
    |----------------|-------------|
    | String         | Decimal     |
    | Float          | Decimal     |
    | Decimal        | Decimal     |
    | Float          | Int         |
    | Decimal        | Int         |
    | String (Int)   | Int         |



- PlaidCloud Lakehouse oferuje również różne funkcje do konwersji wyrażeń na różne formaty daty i godziny. Więcej informacji znajdziesz w [funkcjach daty i godziny](../05-datetime-functions).
