---
title: JSON_OBJECT_INSERT (Lakehouse v1)
description: JSON_OBJECT_INSERT — inserta o actualiza un par clave-valor en un objeto JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-insert.md
---

Inserta o actualiza un par clave-valor en un objeto JSON.

## Sintaxis SQL

```sql
JSON_OBJECT_INSERT(<json_object>, <key>, <value>[, <update_flag>])
```

| Parámetro           | Descripción                                                                                                                                                                                                                                          |   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `<json_object>`     | El objeto JSON de entrada.                                                                                                                                                                                                                           |   |
| `<key>`             | La clave que se insertará o actualizará.                                                                                                                                                                                                             |   |
| `<value>`           | El valor que se asignará a la clave.                                                                                                                                                                                                                 |   |
| `<update_flag>` | Un indicador booleano que controla si se reemplaza el valor cuando la clave especificada ya existe en el objeto JSON. Si es `true`, la función reemplaza el valor cuando la clave ya existe. Si es `false` (o se omite), se produce un error cuando la clave existe. |   |

## Tipo de retorno

Devuelve el objeto JSON actualizado.

## Ejemplos de SQL

Este ejemplo muestra cómo insertar una nueva clave 'c' con el valor 3 en el objeto JSON existente:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'c', 3);

┌────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'c', 3) │
├────────────────────────────────────────────────────────────┤
│ {"a":1,"b":2,"c":3,"d":4}                                  │
└────────────────────────────────────────────────────────────┘
```

Este ejemplo muestra cómo actualizar el valor de la clave existente 'a' de 1 a 10 con el indicador de actualización establecido en `true`, lo que permite reemplazar el valor de la clave:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10, true);

┌───────────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 10, TRUE) │
├───────────────────────────────────────────────────────────────────┤
│ {"a":10,"b":2,"d":4}                                              │
└───────────────────────────────────────────────────────────────────┘
```

Este ejemplo muestra el error que se produce al intentar insertar un valor para la clave existente 'a' sin establecer el indicador de actualización en `true`:

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10);

error: APIError: ResponseError with 1006: ObjectDuplicateKey while evaluating function `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)` in expr `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)`
```
