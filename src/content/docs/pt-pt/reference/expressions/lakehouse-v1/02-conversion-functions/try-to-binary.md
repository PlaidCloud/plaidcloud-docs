---
title: TRY_TO_BINARY (Lakehouse v1)
description: TRY_TO_BINARY — converte uma expressão num valor binário, devolvendo NULL em caso de falha em vez de gerar um erro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-to-binary.md
---

Uma versão melhorada de [TO_BINARY](../to-binary/) que converte uma expressão de entrada num valor binário, devolvendo `NULL` se a conversão falhar, em vez de gerar um erro.

Ver também: [TO_BINARY](../to-binary/)

## Sintaxe do Analyze

```python
func.try_to_binary( <expr> )
```

## Exemplos do Analyze

```python
func.try_to_binary('Databend')

┌───────────────────────────────────────┐
│ func.try_to_binary('Databend')        │
├───────────────────────────────────────┤
│  4461746162656E64                     │
└───────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TRY_TO_BINARY( <expr> )
```

## Exemplos

Este exemplo converte com êxito os dados JSON em binário:

```sql
SELECT TRY_TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant_success;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

Este exemplo demonstra que a função não consegue converter quando a entrada é `NULL`:

```sql
SELECT TRY_TO_BINARY(PARSE_JSON(NULL)) AS binary_variant_invalid_json;

┌─────────────────────────────┐
│ binary_variant_invalid_json │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
