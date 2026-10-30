---
title: SHOW_GRANTS (Lakehouse v1)
description: SHOW_GRANTS — 사용자, 역할 또는 특정 개체에 명시적으로 부여된 권한을 나열합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/show-grants.md
---

사용자, 역할 또는 특정 개체에 명시적으로 부여된 권한을 나열합니다.

## SQL 구문

```sql
SHOW_GRANTS('role', '<role_name>')
SHOW_GRANTS('user', '<user_name>')
SHOW_GRANTS('stage', '<stage_name>')
SHOW_GRANTS('udf', '<udf_name>')
SHOW_GRANTS('table', '<table_name>', '<catalog_name>', '<db_name>')
SHOW_GRANTS('database', '<db_name>', '<catalog_name>')
```

## `enable_expand_roles` 설정 구성

`enable_expand_roles` 설정은 SHOW_GRANTS 함수가 권한을 표시할 때 역할 상속을 확장할지 여부를 제어합니다.

- `enable_expand_roles=1`(기본값):

    - SHOW_GRANTS는 상속된 권한을 재귀적으로 확장합니다. 즉, 어떤 역할에 다른 역할이 부여되어 있으면 상속된 모든 권한을 표시합니다.
    - 사용자도 할당된 역할을 통해 부여된 모든 권한을 확인할 수 있습니다.

- `enable_expand_roles=0`:

    - SHOW_GRANTS는 지정한 역할 또는 사용자에게 직접 할당된 권한만 표시합니다.
    - 다만 결과에는 역할 상속을 나타내는 GRANT ROLE 문이 계속 포함됩니다.

예를 들어 역할 `a`는 `t1`에 대한 `SELECT` 권한을, 역할 `b`는 `t2`에 대한 `SELECT` 권한을 가지고 있다고 하겠습니다.

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

역할 `b`를 역할 `a`에 부여한 다음 역할 `a`의 권한을 다시 확인하면, `t2`에 대한 `SELECT` 권한이 이제 역할 `a`에 포함된 것을 볼 수 있습니다.

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

`enable_expand_roles`를 `0`으로 설정하고 역할 `a`의 권한을 다시 확인하면, 결과에는 역할 `b`에서 상속된 구체적인 권한을 나열하는 대신 `GRANT ROLE` 문이 표시됩니다.

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

## SQL 예제

이 예제는 사용자, 역할 및 특정 개체에 부여된 권한을 나열하는 방법을 보여 줍니다.

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
