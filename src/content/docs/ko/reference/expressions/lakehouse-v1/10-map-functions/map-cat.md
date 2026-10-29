---
title: MAP_CAT (Lakehouse v1)
description: MAP_CAT — 두 MAP을 연결한 결과를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-cat.md
---

두 MAP을 연결한 결과를 반환합니다.

## SQL 구문

```sql
MAP_CAT( <map1>, <map2> )
```

## 인수

| 인수 | 설명                     |
|-----------|---------------------------------|
| `<map1>`  | 원본 MAP입니다.                 |
| `<map2>`  | map1에 덧붙일 MAP입니다. |

:::note
- map1과 map2에 키가 같은 값이 있으면 출력 MAP에는 map2의 값이 들어갑니다.
- 인수 중 하나라도 NULL이면 오류를 보고하지 않고 NULL을 반환합니다.
:::

## 반환 형식

Map.

## SQL 예제

```sql
SELECT MAP_CAT({'a':1,'b':2,'c':3}, {'c':5,'d':6});
┌─────────────────────────────────────────────┐
│ map_cat({'a':1,'b':2,'c':3}, {'c':5,'d':6}) │
├─────────────────────────────────────────────┤
│ {'a':1,'b':2,'c':5,'d':6}                   │
└─────────────────────────────────────────────┘
```
