---
title: IGNORE (Lakehouse v1)
description: IGNORE — insert ignore 문을 사용하면 오류를 일으키는 잘못된 데이터가 있는 행은 무시되고 유효한 데이터가 있는 행만 테이블에 삽입됩니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/ignore.md
---

insert ignore 문을 사용하면 오류를 일으키는 잘못된 데이터가 있는 행은 무시되고 유효한 데이터가 있는 행만 테이블에 삽입됩니다.

## SQL 구문

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
