---
title: MAP_CONTAINS_KEY (Lakehouse v1)
description: MAP_CONTAINS_KEY — 지정한 MAP에 지정한 키가 포함되어 있는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-contains-key.md
---

지정한 MAP에 지정한 키가 포함되어 있는지 확인합니다.

## SQL 구문

```sql
MAP_CONTAINS_KEY( <map>, <key> )
```

## 인수

| 인수 | 설명             |
|-----------|-------------------------|
| `<map>`   | 검색할 MAP입니다. |
| `<key>`   | 찾을 키입니다.        |

## 반환 형식

Boolean.

## SQL 예제

```sql
SELECT MAP_CONTAINS_KEY({'a':1,'b':2,'c':3}, 'c');
┌────────────────────────────────────────────┐
│ map_contains_key({'a':1,'b':2,'c':3}, 'c') │
├────────────────────────────────────────────┤
│ true                                       │
└────────────────────────────────────────────┘

SELECT MAP_CONTAINS_KEY({'a':1,'b':2,'c':3}, 'x');
┌────────────────────────────────────────────┐
│ map_contains_key({'a':1,'b':2,'c':3}, 'x') │
├────────────────────────────────────────────┤
│ false                                      │
└────────────────────────────────────────────┘
```
