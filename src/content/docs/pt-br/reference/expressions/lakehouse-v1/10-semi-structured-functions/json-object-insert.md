---
title: JSON_OBJECT_INSERT (Lakehouse v1)
description: JSON_OBJECT_INSERT — insere ou atualiza um par chave-valor em um objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-insert.md
---

Insere ou atualiza um par chave-valor em um objeto JSON.

## Sintaxe SQL

```sql
JSON_OBJECT_INSERT(<json_object>, <key>, <value>[, <update_flag>])
```

| Parâmetro           | Descrição                                                                                                                                                                                                                                            |   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `<json_object>`     | O objeto JSON de entrada.                                                                                                                                                                                                                            |   |
| `<key>`             | A chave a ser inserida ou atualizada.                                                                                                                                                                                                                |   |
| `<value>`           | O valor a ser atribuído à chave.                                                                                                                                                                                                                     |   |
| `<update_flag>` | Um sinalizador booleano que controla se o valor será substituído quando a chave especificada já existir no objeto JSON. Se `true`, a função substitui o valor quando a chave já existe. Se `false` (ou omitido), ocorre um erro quando a chave existe. |   |

## Tipo de retorno

Retorna o objeto JSON atualizado.

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

Este exemplo mostra como atualizar o valor da chave existente 'a' de 1 para 10 usando o sinalizador de atualização definido como `true`, o que permite substituir o valor da chave:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10, true);

┌───────────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 10, TRUE) │
├───────────────────────────────────────────────────────────────────┤
│ {"a":10,"b":2,"d":4}                                              │
└───────────────────────────────────────────────────────────────────┘
```

Este exemplo demonstra o erro que ocorre ao tentar inserir um valor para a chave existente 'a' sem definir o sinalizador de atualização como `true`:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10);

error: APIError: ResponseError with 1006: ObjectDuplicateKey while evaluating function `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)` in expr `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)`
```
