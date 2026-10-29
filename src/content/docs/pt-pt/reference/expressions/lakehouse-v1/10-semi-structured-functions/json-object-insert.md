---
title: JSON_OBJECT_INSERT (Lakehouse v1)
description: JSON_OBJECT_INSERT — insere ou atualiza um par chave-valor num objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-insert.md
---

Insere ou atualiza um par chave-valor num objeto JSON.

## Sintaxe SQL

```sql
JSON_OBJECT_INSERT(<json_object>, <key>, <value>[, <update_flag>])
```

| Parâmetro           | Descrição                                                                                                                                                                                                                                            |   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `<json_object>`     | O objeto JSON de entrada.                                                                                                                                                                                                                            |   |
| `<key>`             | A chave a inserir ou atualizar.                                                                                                                                                                                                                      |   |
| `<value>`           | O valor a atribuir à chave.                                                                                                                                                                                                                          |   |
| `<update_flag>` | Um indicador booleano que controla se o valor é substituído quando a chave especificada já existe no objeto JSON. Se `true`, a função substitui o valor caso a chave já exista. Se `false` (ou omitido), ocorre um erro caso a chave exista. |   |

## Tipo de retorno

Devolve o objeto JSON atualizado.

## Exemplos de SQL

Este exemplo demonstra como inserir uma nova chave 'c' com o valor 3 no objeto JSON existente:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'c', 3);

┌────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'c', 3) │
├────────────────────────────────────────────────────────────┤
│ {"a":1,"b":2,"c":3,"d":4}                                  │
└────────────────────────────────────────────────────────────┘
```

Este exemplo mostra como atualizar o valor de uma chave existente 'a' de 1 para 10, com o indicador de atualização definido como `true`, o que permite substituir o valor da chave:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10, true);

┌───────────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 10, TRUE) │
├───────────────────────────────────────────────────────────────────┤
│ {"a":10,"b":2,"d":4}                                              │
└───────────────────────────────────────────────────────────────────┘
```

Este exemplo demonstra o erro que ocorre ao tentar inserir um valor para uma chave existente 'a' sem definir o indicador de atualização como `true`:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10);

error: APIError: ResponseError with 1006: ObjectDuplicateKey while evaluating function `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)` in expr `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)`
```
