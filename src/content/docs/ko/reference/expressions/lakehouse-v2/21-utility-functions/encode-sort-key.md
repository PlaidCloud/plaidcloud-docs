---
title: ENCODE_SORT_KEY (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 ENCODE_SORT_KEY 유틸리티 함수를 사용합니다. 정렬 순서를 유지하는 바이너리 정렬 키로 값을 인코딩하며, 복합 정렬 키에 유용합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/encode-sort-key.md
---

정렬 순서를 유지하는 바이너리 정렬 키로 값을 인코딩합니다. 복합 정렬 키에 유용합니다.

## Analyze 구문

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Analyze 예제

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## SQL 구문

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## SQL 예제

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```
