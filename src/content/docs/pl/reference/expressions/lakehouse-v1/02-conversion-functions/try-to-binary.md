---
title: TRY_TO_BINARY (Lakehouse v1)
description: TRY_TO_BINARY — konwertuje wyrażenie na wartość binarną, zwracając NULL w razie niepowodzenia zamiast zgłaszać błąd.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-to-binary.md
---

Rozszerzona wersja funkcji [TO_BINARY](../to-binary/), która konwertuje wyrażenie wejściowe na wartość binarną i zwraca `NULL`, jeśli konwersja się nie powiedzie, zamiast zgłaszać błąd.

Zobacz także: [TO_BINARY](../to-binary/)

## Składnia Analyze

```python
func.try_to_binary( <expr> )
```

## Przykłady Analyze

```python
func.try_to_binary('Databend')

┌───────────────────────────────────────┐
│ func.try_to_binary('Databend')        │
├───────────────────────────────────────┤
│  4461746162656E64                     │
└───────────────────────────────────────┘
```

## Składnia SQL

```sql
TRY_TO_BINARY( <expr> )
```

## Przykłady

Ten przykład pomyślnie konwertuje dane JSON na dane binarne:

```sql
SELECT TRY_TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant_success;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

Ten przykład pokazuje, że funkcja nie wykonuje konwersji, gdy dane wejściowe mają wartość `NULL`:

```sql
SELECT TRY_TO_BINARY(PARSE_JSON(NULL)) AS binary_variant_invalid_json;

┌─────────────────────────────┐
│ binary_variant_invalid_json │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
