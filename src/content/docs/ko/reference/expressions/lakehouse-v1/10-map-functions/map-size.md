---
title: MAP_SIZE (Lakehouse v1)
description: MAP_SIZE — MAP의 크기를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-size.md
---

MAP의 크기를 반환합니다.

## SQL 구문

```sql
MAP_SIZE( <map> )
```

## 인수

| 인수 | 설명    |
|-----------|----------------|
| `<map>`   | 입력 MAP입니다. |

## 반환 형식

UInt64.

## SQL 예제

```sql
SELECT MAP_SIZE({'a':1,'b':2,'c':3});

┌───────────────────────────────┐
│ map_size({'a':1,'b':2,'c':3}) │
├───────────────────────────────┤
│ 3                             │
└───────────────────────────────┘
```
