---
title: DICT_MAPPING (Lakehouse v2)
description: DICT_MAPPING — 딕셔너리 테이블에서 지정한 키에 매핑된 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/09-dictionary-functions/dict-mapping.md
---

딕셔너리 테이블에서 지정한 키에 매핑된 값을 반환합니다.

## Analyze 구문

```python
func.dict_mapping(<dict_table>, <key_column>, <key_value>)
```

## Analyze 예제

```python
func.dict_mapping('city_dict', get_column(table, 'city_id'))

┌────────────┐
│ 'New York'  │
└────────────┘
```

## SQL 구문

```sql
DICT_MAPPING(<dict_table>, <key_column>, <key_value>)
```

## SQL 예제

```sql
SELECT DICT_MAPPING('city_dict', city_id) FROM orders;

┌──────────┐
│ New York  │
└──────────┘
```
