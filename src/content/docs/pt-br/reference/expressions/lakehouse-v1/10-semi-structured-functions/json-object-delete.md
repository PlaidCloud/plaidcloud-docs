---
title: JSON_OBJECT_DELETE (Lakehouse v1)
description: JSON_OBJECT_DELETE — exclui chaves especificadas de um objeto JSON e retorna o objeto modificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-delete.md
---

Exclui chaves especificadas de um objeto JSON e retorna o objeto modificado. Se uma chave especificada não existir no objeto, ela é ignorada.

## Sintaxe SQL

```sql
json_object_delete(<json_object>, <key1> [, <key2>, ...])
```

## Parâmetros

| Parâmetro | Descrição |
|-----------|-----------|
| json_object | Um objeto JSON (tipo VARIANT) do qual excluir chaves. |
| key1, key2, ... | Um ou mais literais de string que representam as chaves a serem excluídas do objeto. |

## Tipo de retorno

Retorna um VARIANT contendo o objeto JSON modificado, sem as chaves especificadas.

## Exemplos de SQL

Excluir uma única chave:
```sql
SELECT json_object_delete('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"b":2,"c":3}
```

Excluir várias chaves:
```sql
SELECT json_object_delete('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"b":2,"d":4}
```

Excluir uma chave inexistente (a chave é ignorada):
```sql
SELECT json_object_delete('{"a":1,"b":2}'::VARIANT, 'x');
-- Result: {"a":1,"b":2}
```
