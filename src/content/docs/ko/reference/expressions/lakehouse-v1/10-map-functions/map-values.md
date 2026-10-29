---
title: MAP_VALUES (Lakehouse v1)
description: MAP_VALUES — MAP의 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-values.md
---

MAP의 값을 반환합니다.

## SQL 구문

```sql
MAP_VALUES( <map> )
```

## 인수

| 인수 | 설명    |
|-----------|----------------|
| `<map>`   | 입력 MAP입니다. |

## 반환 형식

Array.

## SQL 예제

```sql
SELECT MAP_VALUES({'a':1,'b':2,'c':3});

┌─────────────────────────────────┐
│ map_values({'a':1,'b':2,'c':3}) │
├─────────────────────────────────┤
│ [1,2,3]                         │
└─────────────────────────────────┘
```
