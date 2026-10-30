---
title: PARSE_JSON (Lakehouse v1)
description: Interpreta uma cadeia JSON de entrada, produzindo um valor VARIANT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/parse-json.md
---

`parse_json` e `try_parse_json` interpretam uma cadeia de entrada como um documento JSON, produzindo um valor VARIANT.

`try_parse_json` devolve um valor NULL se ocorrer um erro durante a análise.

## Sintaxe do Analyze

```python
func.parse_json(<json_string>)

or

func.try_parse_json(<json_string>)
```

## Exemplos do Analyze

```python
func.parse_json('[-1, 12, 289, 2188, false]')

┌───────────────────────────────────────────────┐
│ func.parse_json('[-1, 12, 289, 2188, false]') │
├───────────────────────────────────────────────┤
│ [-1,12,289,2188,false]                        │
└───────────────────────────────────────────────┘

func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ')

┌──────────────────────────────────────────────────────────────┐
│ func.try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├──────────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                                 │
└──────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
PARSE_JSON(<expr>)
TRY_PARSE_JSON(<expr>)
```

## Argumentos

| Argumentos | Descrição                                                                           |
|-----------|--------------------------------------------------------------------------------------|
| `<expr>`  | Uma expressão do tipo cadeia (por exemplo, VARCHAR) que contém informação JSON válida. |

## Tipo de retorno

VARIANT

## Exemplos de SQL

```sql
SELECT parse_json('[-1, 12, 289, 2188, false]');
┌──────────────────────────────────────────┐
│ parse_json('[-1, 12, 289, 2188, false]') │
├──────────────────────────────────────────┤
│ [-1,12,289,2188,false]                   │
└──────────────────────────────────────────┘

SELECT try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ');
┌─────────────────────────────────────────────────────────┐
│ try_parse_json('{ "x" : "abc", "y" : false, "z": 10} ') │
├─────────────────────────────────────────────────────────┤
│ {"x":"abc","y":false,"z":10}                            │
└─────────────────────────────────────────────────────────┘
```
