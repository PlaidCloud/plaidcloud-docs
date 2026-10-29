---
title: DICT_GET (Lakehouse v1)
description: DICT_GET — 제공된 키 식을 사용하여 딕셔너리에서 지정한 속성의 값을 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-dictionary-functions/dict-get.md
---

제공된 키 식을 사용하여 딕셔너리에서 지정한 속성의 값을 가져옵니다.

## SQL 구문

```sql
DICT_GET([db_name.]<dict_name>, '<attr_name>', <key_expr>)
```

| 매개변수 | 설명 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict_name | 딕셔너리의 이름입니다. |
| attr_name | 값을 가져오려는 딕셔너리 속성의 이름입니다. |
| key_expr  | 딕셔너리에서 특정 항목을 찾는 데 사용하는 키 식입니다. 해당 데이터를 가져오기 위한 딕셔너리 기본 키의 값을 나타냅니다. |

## SQL 예제
