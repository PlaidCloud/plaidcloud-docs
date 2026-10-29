---
title: JSON_PATH_MATCH (Lakehouse v1)
description: JSON_PATH_MATCH — verifica se uma expressão de caminho JSON especificada corresponde a determinadas condições.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-path-match.md
---

Verifica se uma expressão de caminho JSON especificada corresponde a determinadas condições dentro de dados JSON. Tenha em atenção que o operador `@@` é sinónimo desta função. Para obter mais informações, consulte Operadores JSON.


## Sintaxe do Analyze

```python
func.json_path_match(<json_data>, <json_path_expression)
```

## Exemplos do Analyze

```python
func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1')
┌──────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├──────────────────────────────────────────────────────────────────────────┤
│ true                                                                     │
└──────────────────────────────────────────────────────────────────────────┘

func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1')
┌────────────────────────────────────────────────────────────────────────────┐
│ func.json_path_match(func.parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├────────────────────────────────────────────────────────────────────────────┤
│ false                                                                      │
└────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
JSON_PATH_MATCH(<json_data>, <json_path_expression>)
```

- `json_data`: especifica os dados JSON que pretende examinar. Pode ser um objeto JSON ou uma matriz.
- `json_path_expression`: especifica as condições a verificar nos dados JSON. Esta expressão descreve o caminho ou os critérios específicos a corresponder, por exemplo, verificar se determinados valores de campos na estrutura JSON cumprem certas condições. O símbolo `$` representa a raiz dos dados JSON. É utilizado para iniciar a expressão de caminho e indica o objeto de nível superior na estrutura JSON.

## Tipo de retorno

A função devolve:

- `true` se a expressão de caminho JSON especificada corresponder às condições dentro dos dados JSON.
- `false` se a expressão de caminho JSON especificada não corresponder às condições dentro dos dados JSON.
- NULL se `json_data` ou `json_path_expression` for NULL ou inválido.

## Exemplos de SQL

```sql
-- Check if the value at JSON path $.a is equal to 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1');

┌────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.a == 1') │
├────────────────────────────────────────────────────────────────┤
│ true                                                           │
└────────────────────────────────────────────────────────────────┘

-- Check if the first element in the array at JSON path $.b is greater than 1
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1');

┌──────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[0] > 1') │
├──────────────────────────────────────────────────────────────────┤
│ false                                                            │
└──────────────────────────────────────────────────────────────────┘

-- Check if any element in the array at JSON path $.b
-- from the second one to the last are greater than or equal to 2
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2');

┌───────────────────────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), '$.b[1 to last] >= 2') │
├───────────────────────────────────────────────────────────────────────────┤
│ true                                                                      │
└───────────────────────────────────────────────────────────────────────────┘

-- NULL is returned if either the json_data or json_path_expression is NULL or invalid.
SELECT JSON_PATH_MATCH(parse_json('{"a":1,"b":[1,2,3]}'), NULL);

┌──────────────────────────────────────────────────────────┐
│ json_path_match(parse_json('{"a":1,"b":[1,2,3]}'), null) │
├──────────────────────────────────────────────────────────┤
│ NULL                                                     │
└──────────────────────────────────────────────────────────┘

SELECT JSON_PATH_MATCH(NULL, '$.a == 1');

┌───────────────────────────────────┐
│ json_path_match(null, '$.a == 1') │
├───────────────────────────────────┤
│ NULL                              │
└───────────────────────────────────┘
```
