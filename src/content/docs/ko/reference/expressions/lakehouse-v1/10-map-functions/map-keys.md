---
title: MAP_KEYS (Lakehouse v1)
description: MAP_KEYS — MAP의 키를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-keys.md
---

MAP의 키를 반환합니다.

## SQL 구문

```sql
MAP_KEYS( <map> )
```

## 인수

| 인수 | 설명    |
|-----------|----------------|
| `<map>`   | 입력 MAP입니다. |

## 반환 형식

Array.

## SQL 예제

```sql
SELECT MAP_KEYS({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_keys({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ ['a','b','c']                 │
└───────────────────────────────┘
```
