---
title: Konvertierungsfunktionen (Lakehouse v1)
description: "SQL-Konvertierungsfunktionen in Lakehouse v1: Werte zwischen Typen umwandeln – CAST, TRY_CAST sowie Parse- und Formatierungshilfen."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/index.md
---

Dieser Abschnitt enthält Referenzinformationen zu den Konvertierungsfunktionen in PlaidCloud Lakehouse.

## Funktionen

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
- [TO_STRING (Konvertierung, Lakehouse v1)](to-string/)
- [TO_TEXT](to-text/)
- [TO_UINT16](to-uint16/)
- [TO_UINT32](to-uint32/)
- [TO_UINT64](to-uint64/)
- [TO_UINT8](to-uint8/)
- [TO_VARCHAR](to-varchar/)
- [TO_VARIANT](to-variant/)
- [TRY_CAST](try-cast/)
- [TRY_TO_BINARY](try-to-binary/)

Bitte beachten Sie Folgendes, wenn Sie einen Wert von einem Typ in einen anderen umwandeln:

- Bei der Umwandlung von Gleitkommazahlen, Dezimalzahlen oder Zeichenfolgen in Ganzzahlen oder Dezimalzahlen mit Nachkommastellen rundet PlaidCloud Lakehouse die Werte auf die nächste ganze Zahl. Das bestimmt die Einstellung `numeric_cast_option` (Standard: 'rounding'), die das Verhalten numerischer Umwandlungen steuert. Wenn `numeric_cast_option` ausdrücklich auf 'truncating' gesetzt wird, schneidet PlaidCloud Lakehouse den Dezimalanteil ab und verwirft alle Nachkommastellen.

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

    Die folgende Tabelle fasst die numerischen Umwandlungen zusammen und zeigt, welche Umwandlungen zwischen den verschiedenen numerischen Quell- und Zieldatentypen möglich sind. Beachten Sie, dass für die Umwandlung von Zeichenfolge in Ganzzahl die Quellzeichenfolge einen ganzzahligen Wert enthalten muss.

    | Quelltyp          | Zieltyp     |
    |-------------------|-------------|
    | Zeichenfolge      | Dezimalzahl |
    | Gleitkommazahl    | Dezimalzahl |
    | Dezimalzahl       | Dezimalzahl |
    | Gleitkommazahl    | Ganzzahl    |
    | Dezimalzahl       | Ganzzahl    |
    | Zeichenfolge (Ganzzahl) | Ganzzahl |


- PlaidCloud Lakehouse bietet außerdem eine Vielzahl von Funktionen, um Ausdrücke in verschiedene Datums- und Zeitformate umzuwandeln. Weitere Informationen finden Sie unter [Datums- und Zeitfunktionen](../05-datetime-functions).
