---
title: SHOW_GRANTS (Lakehouse v1)
description: SHOW_GRANTS enumera los privilegios concedidos explícitamente a un usuario, a un rol o sobre un objeto específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/show-grants.md
---

Enumera los privilegios concedidos explícitamente a un usuario, a un rol o sobre un objeto específico.

## Sintaxis de SQL

```sql
SHOW_GRANTS('role', '<role_name>')
SHOW_GRANTS('user', '<user_name>')
SHOW_GRANTS('stage', '<stage_name>')
SHOW_GRANTS('udf', '<udf_name>')
SHOW_GRANTS('table', '<table_name>', '<catalog_name>', '<db_name>')
SHOW_GRANTS('database', '<db_name>', '<catalog_name>')
```

## Configuración de `enable_expand_roles`

La configuración `enable_expand_roles` controla si la función SHOW_GRANTS expande la herencia de roles al mostrar los privilegios.

- `enable_expand_roles=1` (predeterminado):

    - SHOW_GRANTS expande de forma recursiva los privilegios heredados; es decir, si a un rol se le ha concedido otro rol, muestra todos los privilegios heredados.
    - Los usuarios también verán todos los privilegios concedidos a través de los roles que tienen asignados.

- `enable_expand_roles=0`:

    - SHOW_GRANTS solo muestra los privilegios asignados directamente al rol o usuario especificado.
    - Sin embargo, el resultado seguirá incluyendo sentencias GRANT ROLE para indicar la herencia de roles.

Por ejemplo, el rol `a` tiene el privilegio `SELECT` sobre `t1` y el rol `b` tiene el privilegio `SELECT` sobre `t2`:

```sql
SELECT grants FROM show_grants('role', 'a') ORDER BY object_id;

┌──────────────────────────────────────────────────────┐
│                        grants                        │
├──────────────────────────────────────────────────────┤
│ GRANT SELECT ON 'default'.'default'.'t1' TO ROLE `a` │
└──────────────────────────────────────────────────────┘

SELECT grants FROM show_grants('role', 'b') ORDER BY object_id;

┌──────────────────────────────────────────────────────┐
│                        grants                        │
├──────────────────────────────────────────────────────┤
│ GRANT SELECT ON 'default'.'default'.'t2' TO ROLE `b` │
└──────────────────────────────────────────────────────┘
```

Si concede el rol `b` al rol `a` y vuelve a consultar los privilegios del rol `a`, verá que el privilegio `SELECT` sobre `t2` ahora está incluido en el rol `a`:

```sql
GRANT ROLE b TO ROLE a;
```

```sql
SELECT grants FROM show_grants('role', 'a') ORDER BY object_id;

┌──────────────────────────────────────────────────────┐
│                        grants                        │
├──────────────────────────────────────────────────────┤
│ GRANT SELECT ON 'default'.'default'.'t1' TO ROLE `a` │
│ GRANT SELECT ON 'default'.'default'.'t2' TO ROLE `a` │
└──────────────────────────────────────────────────────┘
```

Si establece `enable_expand_roles` en `0` y vuelve a consultar los privilegios del rol `a`, el resultado mostrará la sentencia `GRANT ROLE` en lugar de enumerar los privilegios específicos heredados del rol `b`:

```sql
SET enable_expand_roles=0;
```

```sql
SELECT grants FROM show_grants('role', 'a') ORDER BY object_id;

┌──────────────────────────────────────────────────────┐
│                        grants                        │
├──────────────────────────────────────────────────────┤
│ GRANT SELECT ON 'default'.'default'.'t1' TO ROLE `a` │
│ GRANT ROLE b to ROLE `a`                             │
│ GRANT ROLE public to ROLE `a`                        │
└──────────────────────────────────────────────────────┘
```

## Ejemplos de SQL

Este ejemplo ilustra cómo enumerar los privilegios concedidos a un usuario, a un rol y sobre un objeto específico.

```sql
-- Create a new user
CREATE USER 'user1' IDENTIFIED BY 'password';

-- Create a new role
CREATE ROLE analyst;

-- Grant the analyst role to the user
GRANT ROLE analyst TO 'user1';

-- Create a stage
CREATE STAGE my_stage;

-- Grant privileges on the stage to the role
GRANT READ ON STAGE my_stage TO ROLE analyst;

-- List privileges granted to the user
SELECT * FROM SHOW_GRANTS('user', 'user1');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ privileges │ object_name │     object_id    │ grant_to │  name  │                    grants                   │
├────────────┼─────────────┼──────────────────┼──────────┼────────┼─────────────────────────────────────────────┤
│ Read       │ my_stage    │             NULL │ USER     │ user1  │ GRANT Read ON STAGE my_stage TO 'user1'@'%' │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- List privileges granted to the role
SELECT * FROM SHOW_GRANTS('role', 'analyst');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ privileges │ object_name │     object_id    │ grant_to │   name  │                     grants                     │
├────────────┼─────────────┼──────────────────┼──────────┼─────────┼────────────────────────────────────────────────┤
│ Read       │ my_stage    │             NULL │ ROLE     │ analyst │ GRANT Read ON STAGE my_stage TO ROLE `analyst` │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- List privileges granted on the stage
SELECT * FROM SHOW_GRANTS('stage', 'my_stage');

┌─────────────────────────────────────────────────────────────────────────────────────┐
│ privileges │ object_name │     object_id    │ grant_to │   name  │      grants      │
├────────────┼─────────────┼──────────────────┼──────────┼─────────┼──────────────────┤
│ Read       │ my_stage    │             NULL │ ROLE     │ analyst │                  │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
