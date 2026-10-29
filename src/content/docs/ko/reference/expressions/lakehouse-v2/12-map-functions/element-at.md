---
title: "ELEMENT_AT (맵, Lakehouse v2)"
description: ELEMENT_AT — 맵에서 지정한 키와 연결된 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/12-map-functions/element-at.md
---

맵에서 지정한 키와 연결된 값을 반환합니다.

## Analyze 구문

```python
func.element_at(get_column(table, 'map_col'), 'key')
```

## Analyze 예제

```python
func.element_at(MAP{'a':1,'b':2}, 'b')

┌───┐
│ 2 │
└───┘
```

## SQL 구문

```sql
ELEMENT_AT(<map_col>, 'key')
```

## SQL 예제

```sql
SELECT ELEMENT_AT(MAP{'a':1, 'b':2}, 'b');

┌───┐
│ 2 │
└───┘
```
