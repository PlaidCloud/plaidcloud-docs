---
title: TRY_TO_BINARY (Lakehouse v1)
description: TRY_TO_BINARY — convierte una expresión en un valor binario y devuelve NULL en caso de error en lugar de generar un error.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-to-binary.md
---

Una versión mejorada de [TO_BINARY](../to-binary/) que convierte una expresión de entrada en un valor binario y devuelve `NULL` si la conversión falla, en lugar de generar un error.

Consulte también: [TO_BINARY](../to-binary/)

## Sintaxis de Analyze

```python
func.try_to_binary( <expr> )
```

## Ejemplos de Analyze

```python
func.try_to_binary('Databend')

┌───────────────────────────────────────┐
│ func.try_to_binary('Databend')        │
├───────────────────────────────────────┤
│  4461746162656E64                     │
└───────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TRY_TO_BINARY( <expr> )
```

## Ejemplos

Este ejemplo convierte correctamente los datos JSON a binario:

```sql
SELECT TRY_TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant_success;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

Este ejemplo muestra que la función no convierte cuando la entrada es `NULL`:

```sql
SELECT TRY_TO_BINARY(PARSE_JSON(NULL)) AS binary_variant_invalid_json;

┌─────────────────────────────┐
│ binary_variant_invalid_json │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
