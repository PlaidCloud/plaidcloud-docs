---
title: LIST_STAGE (Lakehouse v1)
description: LIST_STAGE — 스테이지의 파일을 나열합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/03-list-stage.md
---

스테이지의 파일을 나열합니다. 이를 통해 확장자를 기준으로 스테이지의 파일을 필터링하고 각 파일에 대한 포괄적인 세부 정보를 얻을 수 있습니다. 이 함수는 DDL 명령 LIST STAGE FILES와 비슷하지만, 모든 파일 정보 대신 파일 이름, 크기, MD5 해시, 마지막 수정 타임스탬프, 작성자와 같은 특정 파일 정보를 SELECT 문으로 유연하게 가져올 수 있습니다.

## SQL 구문

```sql
LIST_STAGE(
  LOCATION => '{ internalStage | externalStage | userStage }'
  [ PATTERN => '<regex_pattern>']
)
```

여기서:

### Internalstage

```sql
internalStage ::= @<internal_stage_name>[/<path>]
```

### Externalstage

```sql
externalStage ::= @<external_stage_name>[/<path>]
```

### Userstage

```sql
userStage ::= @~[/<path>]
```

### PATTERN

COPY INTO table을 참조하십시오.


## SQL 예제

```sql
SELECT * FROM list_stage(location => '@my_stage/', pattern => '.*[.]log');
┌────────────────┬──────┬────────────────────────────────────┬───────────────────────────────┬─────────┐
│      name      │ size │                md5                 │         last_modified         │ creator │
├────────────────┼──────┼────────────────────────────────────┼───────────────────────────────┼─────────┤
│ 2023/meta.log  │  475 │ "4208ff530b252236e14b3cd797abdfbd" │ 2023-04-19 20:23:24.000 +0000 │ NULL    │
│ 2023/query.log │ 1348 │ "1c6654b207472c277fc8c6207c035e18" │ 2023-04-19 20:23:24.000 +0000 │ NULL    │
└────────────────┴──────┴────────────────────────────────────┴───────────────────────────────┴─────────┘

-- Equivalent to the following statement:
LIST @my_stage PATTERN = '.log';
```
