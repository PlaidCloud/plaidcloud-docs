---
title: JSON_PATH_EXISTS (Lakehouse v1)
description: JSON_PATH_EXISTS — verifica se um caminho especificado existe nos dados JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-exists.md
---

Verifica se um caminho especificado existe nos dados JSON.

## Sintaxe do Analyze

```python
func.json_path_exists(<json_data>, <json_path_expression)
```

## Exemplos do Analyze

```python
func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)'), func.json_path_exists(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)')
┌─────────────────────────────┐
│       Item 1   │  Item 2    │
├────────────────┼────────────┤
│       True     │  False     │
└─────────────────────────────┘
```

## Sintaxe SQL

```sql
JSON_PATH_EXISTS(<json_data>, <json_path_expression>)
```

- json_data: especifica os dados JSON em que pretende pesquisar. Pode ser um objeto JSON ou uma matriz.

- json_path_expression: especifica o caminho, a partir da raiz dos dados JSON representada por `$`, que pretende verificar nos dados JSON. Pode também incluir condições na expressão, utilizando `@` para se referir ao nó ou elemento atual que está a ser avaliado, de modo a filtrar os resultados.

## Tipo de retorno

A função devolve:

- `true` se o caminho JSON especificado (e as condições, se existirem) existir nos dados JSON.
- `false` se o caminho JSON especificado (e as condições, se existirem) não existir nos dados JSON.
- NULL se json_data ou json_path_expression for NULL ou inválido.

## Exemplos de SQL

```sql
SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ == 1)');

----
true


SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), '$.a ? (@ > 1)');

----
false

SELECT JSON_PATH_EXISTS(NULL, '$.a');

----
NULL

SELECT JSON_PATH_EXISTS(parse_json('{"a": 1, "b": 2}'), NULL);

----
NULL
```
