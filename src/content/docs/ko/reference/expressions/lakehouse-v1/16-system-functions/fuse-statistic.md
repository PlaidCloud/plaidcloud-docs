---
title: FUSE_STATISTIC (Lakehouse v1)
description: FUSE_STATISTIC — 테이블에 있는 각 열의 고유 값 추정 개수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-statistic.md
---

테이블에 있는 각 열의 고유 값 추정 개수를 반환합니다.


## SQL 구문

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## SQL 예제

이 함수는 `ANALYZE TABLE <table_name>`과 함께 사용하여 테이블의 통계 정보를 생성하고 확인하는 경우가 가장 많습니다. 자세한 설명과 예제는 OPTIMIZE TABLE을 참조하십시오.
