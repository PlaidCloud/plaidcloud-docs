---
title: JSON_OBJECT_PICK (Lakehouse v1)
description: JSON_OBJECT_PICK — cria um novo objeto JSON contendo somente as chaves especificadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-pick.md
---

Cria um novo objeto JSON contendo somente as chaves especificadas do objeto JSON de entrada. Se uma chave especificada não existir no objeto de entrada, ela é omitida do resultado.

## Sintaxe SQL

```sql
json_object_pick(<json_object>, <key1> [, <key2>, ...])
```

## Parâmetros

| Parâmetro | Descrição |
|-----------|-----------|
| json_object | Um objeto JSON (tipo VARIANT) do qual selecionar chaves. |
| key1, key2, ... | Um ou mais literais de string que representam as chaves a serem incluídas no objeto de resultado. |

## Tipo de retorno

Retorna um VARIANT contendo um novo objeto JSON somente com as chaves especificadas e seus valores correspondentes.

## Exemplos de SQL

Selecionar uma única chave:
```sql
SELECT json_object_pick('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"a":1}
```

Selecionar várias chaves:
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'b');
-- Result: {"a":1,"b":2}
```

Selecionar com uma chave inexistente (chaves inexistentes são ignoradas):
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"a":1}
```
