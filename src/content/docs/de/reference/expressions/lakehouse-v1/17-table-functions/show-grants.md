---
title: SHOW_GRANTS (Lakehouse v1)
description: SHOW_GRANTS listet Berechtigungen auf, die einem Benutzer, einer Rolle oder für ein bestimmtes Objekt ausdrücklich erteilt wurden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/show-grants.md
---

Listet Berechtigungen auf, die einem Benutzer, einer Rolle oder für ein bestimmtes Objekt ausdrücklich erteilt wurden.

## SQL-Syntax

```sql
SHOW_GRANTS('role', '<role_name>')
SHOW_GRANTS('user', '<user_name>')
SHOW_GRANTS('stage', '<stage_name>')
SHOW_GRANTS('udf', '<udf_name>')
SHOW_GRANTS('table', '<table_name>', '<catalog_name>', '<db_name>')
SHOW_GRANTS('database', '<db_name>', '<catalog_name>')
```

## Einstellung `enable_expand_roles` konfigurieren

Die Einstellung `enable_expand_roles` steuert, ob die Funktion SHOW_GRANTS bei der Anzeige der Berechtigungen die Rollenvererbung auflöst.

- `enable_expand_roles=1` (Standard):

    - SHOW_GRANTS löst vererbte Berechtigungen rekursiv auf. Wurde einer Rolle also eine andere Rolle erteilt, werden alle vererbten Berechtigungen angezeigt.
    - Benutzer sehen außerdem alle Berechtigungen, die ihnen über die zugewiesenen Rollen erteilt wurden.

- `enable_expand_roles=0`:

    - SHOW_GRANTS zeigt nur Berechtigungen an, die der angegebenen Rolle oder dem angegebenen Benutzer direkt zugewiesen sind.
    - Das Ergebnis enthält jedoch weiterhin GRANT-ROLE-Anweisungen, um die Rollenvererbung anzuzeigen.

Angenommen, Rolle `a` hat die Berechtigung `SELECT` für `t1` und Rolle `b` hat die Berechtigung `SELECT` für `t2`:

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

Wenn Sie Rolle `b` der Rolle `a` erteilen und die Berechtigungen der Rolle `a` erneut prüfen, sehen Sie, dass die Berechtigung `SELECT` für `t2` nun in Rolle `a` enthalten ist:

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

Wenn Sie `enable_expand_roles` auf `0` setzen und die Berechtigungen der Rolle `a` erneut prüfen, zeigt das Ergebnis die Anweisung `GRANT ROLE` an, statt die von Rolle `b` geerbten einzelnen Berechtigungen aufzulisten:

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

## SQL-Beispiele

Dieses Beispiel zeigt, wie Sie Berechtigungen auflisten, die einem Benutzer, einer Rolle und für ein bestimmtes Objekt erteilt wurden.

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
