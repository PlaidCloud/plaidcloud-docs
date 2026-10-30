---
title: EXISTS (Lakehouse v1)
description: EXISTS — exists 조건은 서브쿼리와 함께 사용하며, 서브쿼리가 하나 이상의 행을 반환하면 "충족된" 것으로 간주합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/exists.md
---

exists 조건은 서브쿼리와 함께 사용하며, 서브쿼리가 하나 이상의 행을 반환하면 "충족된" 것으로 간주합니다.

## SQL 구문

```sql
WHERE EXISTS ( <subquery> );
```

## SQL 예제
```sql
SELECT number FROM numbers(5) AS A WHERE exists (SELECT * FROM numbers(3) WHERE number=1); 
┌────────┐
│ number │
├────────┤
│      0 │
│      1 │
│      2 │
│      3 │
│      4 │
└────────┘
```
