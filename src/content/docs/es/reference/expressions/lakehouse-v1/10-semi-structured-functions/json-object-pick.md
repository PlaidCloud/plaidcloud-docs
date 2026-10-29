---
title: JSON_OBJECT_PICK (Lakehouse v1)
description: JSON_OBJECT_PICK — crea un nuevo objeto JSON que contiene solo las claves especificadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-pick.md
---

Crea un nuevo objeto JSON que contiene solo las claves especificadas del objeto JSON de entrada. Si una clave especificada no existe en el objeto de entrada, se omite del resultado.

## Sintaxis SQL

```sql
json_object_pick(<json_object>, <key1> [, <key2>, ...])
```

## Parámetros

| Parámetro | Descripción |
|-----------|-------------|
| json_object | Un objeto JSON (tipo VARIANT) del que se seleccionarán claves. |
| key1, key2, ... | Uno o más literales de cadena que representan las claves que se incluirán en el objeto resultante. |

## Tipo de retorno

Devuelve un VARIANT que contiene un nuevo objeto JSON con solo las claves especificadas y sus valores correspondientes.

## Ejemplos de SQL

Seleccionar una sola clave:
```sql
SELECT json_object_pick('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"a":1}
```

Seleccionar varias claves:
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'b');
-- Result: {"a":1,"b":2}
```

Seleccionar con una clave inexistente (las claves inexistentes se ignoran):
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"a":1}
```
