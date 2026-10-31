---
title: JSON_OBJECT_DELETE (Lakehouse v1)
description: JSON_OBJECT_DELETE — elimina las claves especificadas de un objeto JSON y devuelve el objeto modificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-delete.md
---

Elimina las claves especificadas de un objeto JSON y devuelve el objeto modificado. Si una clave especificada no existe en el objeto, se ignora.

## Sintaxis SQL

```sql
json_object_delete(<json_object>, <key1> [, <key2>, ...])
```

## Parámetros

| Parámetro | Descripción |
|-----------|-------------|
| json_object | Un objeto JSON (tipo VARIANT) del que se eliminarán claves. |
| key1, key2, ... | Uno o más literales de cadena que representan las claves que se eliminarán del objeto. |

## Tipo de retorno

Devuelve un VARIANT que contiene el objeto JSON modificado, sin las claves especificadas.

## Ejemplos de SQL

Eliminar una sola clave:
```sql
SELECT json_object_delete('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"b":2,"c":3}
```

Eliminar varias claves:
```sql
SELECT json_object_delete('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"b":2,"d":4}
```

Eliminar una clave inexistente (la clave se ignora):
```sql
SELECT json_object_delete('{"a":1,"b":2}'::VARIANT, 'x');
-- Result: {"a":1,"b":2}
```
