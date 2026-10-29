---
title: RESULT_SCAN (Lakehouse v1)
description: RESULT_SCAN — 같은 세션에서 이전 명령의 결과 집합을 테이블처럼 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/04-result-scan.md
---

같은 세션에서 이전 명령의 결과 집합을 테이블처럼 반환합니다.


## SQL 구문

```sql
RESULT_SCAN( { '<query_id>' | LAST_QUERY_ID() } )
```

## SQL 예제

간단한 테이블을 만듭니다.

```sql
CREATE TABLE t1(a int);
```

몇 가지 값을 삽입합니다.

```sql
INSERT INTO t1(a) VALUES (1), (2), (3);
```

### `result_scan`


```bash
SELECT * FROM t1 ORDER BY a;
┌───────┐
│   a   │
├───────┤
│   1   │
├───────┤
│   2   │
├───────┤
│   3   │
└───────┘
```


```bash
SELECT * FROM RESULT_SCAN(LAST_QUERY_ID()) ORDER BY a;
┌───────┐
│   a   │
├───────┤
│   1   │
├───────┤
│   2   │
├───────┤
│   3   │
└───────┘
```
