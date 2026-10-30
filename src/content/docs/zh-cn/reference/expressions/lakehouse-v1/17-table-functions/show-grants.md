---
title: SHOW_GRANTS (Lakehouse v1)
description: SHOW_GRANTS：列出显式授予用户、角色或特定对象的权限。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/show-grants.md
---

列出显式授予用户、角色或特定对象的权限。

## SQL 语法

```sql
SHOW_GRANTS('role', '<role_name>')
SHOW_GRANTS('user', '<user_name>')
SHOW_GRANTS('stage', '<stage_name>')
SHOW_GRANTS('udf', '<udf_name>')
SHOW_GRANTS('table', '<table_name>', '<catalog_name>', '<db_name>')
SHOW_GRANTS('database', '<db_name>', '<catalog_name>')
```

## 配置 `enable_expand_roles` 设置

`enable_expand_roles` 设置控制 SHOW_GRANTS 函数在显示权限时是否展开角色继承。

- `enable_expand_roles=1`（默认）：

    - SHOW_GRANTS 会递归展开继承的权限，也就是说，如果某个角色被授予了另一个角色，则会显示所有继承的权限。
    - 用户还会看到通过其所分配角色授予的所有权限。

- `enable_expand_roles=0`：

    - SHOW_GRANTS 只显示直接分配给指定角色或用户的权限。
    - 但结果仍会包含 GRANT ROLE 语句，以表明角色继承关系。

例如，角色 `a` 对 `t1` 拥有 `SELECT` 权限，角色 `b` 对 `t2` 拥有 `SELECT` 权限：

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

如果将角色 `b` 授予角色 `a`，然后再次检查角色 `a` 的权限，可以看到对 `t2` 的 `SELECT` 权限现已包含在角色 `a` 中：

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

如果将 `enable_expand_roles` 设置为 `0`，然后再次检查角色 `a` 的权限，结果将显示 `GRANT ROLE` 语句，而不是列出从角色 `b` 继承的具体权限：

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

## SQL 示例

此示例说明如何列出授予用户、角色以及特定对象的权限。

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
