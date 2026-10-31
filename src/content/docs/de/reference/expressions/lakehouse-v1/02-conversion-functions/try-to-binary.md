---
title: TRY_TO_BINARY (Lakehouse v1)
description: TRY_TO_BINARY – wandelt einen Ausdruck in einen Binärwert um und gibt bei einem Fehler NULL zurück, statt einen Fehler auszulösen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-to-binary.md
---

Eine erweiterte Version von [TO_BINARY](../to-binary/), die einen Eingabeausdruck in einen Binärwert umwandelt und `NULL` zurückgibt, wenn die Umwandlung fehlschlägt, statt einen Fehler auszulösen.

Siehe auch: [TO_BINARY](../to-binary/)

## Analyze-Syntax

```python
func.try_to_binary( <expr> )
```

## Analyze-Beispiele

```python
func.try_to_binary('Databend')

┌───────────────────────────────────────┐
│ func.try_to_binary('Databend')        │
├───────────────────────────────────────┤
│  4461746162656E64                     │
└───────────────────────────────────────┘
```

## SQL-Syntax

```sql
TRY_TO_BINARY( <expr> )
```

## Beispiele

Dieses Beispiel wandelt die JSON-Daten erfolgreich in Binärdaten um:

```sql
SELECT TRY_TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant_success;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

Dieses Beispiel zeigt, dass die Funktion die Umwandlung nicht durchführt, wenn die Eingabe `NULL` ist:

```sql
SELECT TRY_TO_BINARY(PARSE_JSON(NULL)) AS binary_variant_invalid_json;

┌─────────────────────────────┐
│ binary_variant_invalid_json │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
