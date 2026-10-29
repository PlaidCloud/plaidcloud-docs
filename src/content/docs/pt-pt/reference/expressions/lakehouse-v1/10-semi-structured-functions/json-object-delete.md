---
title: JSON_OBJECT_DELETE (Lakehouse v1)
description: JSON_OBJECT_DELETE — elimina chaves especificadas de um objeto JSON e devolve o objeto modificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-delete.md
---

Elimina chaves especificadas de um objeto JSON e devolve o objeto modificado. Se uma chave especificada não existir no objeto, é ignorada.

## Sintaxe SQL

```sql
json_object_delete(<json_object>, <key1> [, <key2>, ...])
```

## Parâmetros

| Parâmetro | Descrição |
|-----------|-------------|
| json_object | Um objeto JSON (tipo VARIANT) do qual eliminar chaves. |
| key1, key2, ... | Um ou mais literais de cadeia que representam as chaves a eliminar do objeto. |

## Tipo de retorno

Devolve um VARIANT que contém o objeto JSON modificado, sem as chaves especificadas.

## Exemplos de SQL

Eliminar uma única chave:
```sql
SELECT json_object_delete('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"b":2,"c":3}
```

Eliminar várias chaves:
```sql
SELECT json_object_delete('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"b":2,"d":4}
```

Eliminar uma chave inexistente (a chave é ignorada):
```sql
SELECT json_object_delete('{"a":1,"b":2}'::VARIANT, 'x');
-- Result: {"a":1,"b":2}
```
