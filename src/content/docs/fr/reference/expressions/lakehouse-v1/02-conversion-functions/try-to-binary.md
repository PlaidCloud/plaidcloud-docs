---
title: TRY_TO_BINARY (Lakehouse v1)
description: "TRY_TO_BINARY : convertit une expression en valeur binaire et renvoie NULL en cas d'échec au lieu de lever une erreur."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-to-binary.md
---

Version améliorée de [TO_BINARY](../to-binary/) qui convertit une expression d'entrée en valeur binaire et renvoie `NULL` si la conversion échoue, au lieu de lever une erreur.

Voir aussi : [TO_BINARY](../to-binary/)

## Syntaxe Analyze

```python
func.try_to_binary( <expr> )
```

## Exemples Analyze

```python
func.try_to_binary('Databend')

┌───────────────────────────────────────┐
│ func.try_to_binary('Databend')        │
├───────────────────────────────────────┤
│  4461746162656E64                     │
└───────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TRY_TO_BINARY( <expr> )
```

## Exemples

Cet exemple convertit avec succès les données JSON en binaire :

```sql
SELECT TRY_TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant_success;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

Cet exemple montre que la fonction échoue à convertir lorsque l'entrée est `NULL` :

```sql
SELECT TRY_TO_BINARY(PARSE_JSON(NULL)) AS binary_variant_invalid_json;

┌─────────────────────────────┐
│ binary_variant_invalid_json │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
