---
title: MAP_INSERT (Lakehouse v1)
description: MAP_INSERT — 입력 MAP에 새 키-값 쌍을 삽입한(기존 키는 새 값으로 갱신한) 새 MAP을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-insert.md
---

입력 MAP에 새 키-값 쌍을 삽입한(기존 키는 새 값으로 갱신한) 새 MAP을 반환합니다.

## SQL 구문

```sql
MAP_INSERT( <map>, <key>, <value> [, <updateFlag> ] )
```

## 인수

| 인수      | 설명                                                                                  |
|----------------|----------------------------------------------------------------------------------------------|
| `<map>`        | 입력 MAP입니다.                                                                               |
| `<key>`        | MAP에 삽입할 새 키입니다.                                                          |
| `<value>`      | MAP에 삽입할 새 값입니다.                                                        |
| `<updateFlag>` | 기존 키를 덮어쓸 수 있는지 나타내는 Boolean 플래그입니다. 기본값은 FALSE입니다. |

## 반환 형식

Map.

## SQL 예제

```sql
SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'd', 4);
┌─────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'd', 4) │
├─────────────────────────────────────────┤
│ {'a':1,'b':2,'c':3,'d':4}               │
└─────────────────────────────────────────┘

SELECT MAP_INSERT({'a':1,'b':2,'c':3}, 'a', 5, true);
┌───────────────────────────────────────────────┐
│ map_insert({'a':1,'b':2,'c':3}, 'a', 5, TRUE) │
├───────────────────────────────────────────────┤
│ {'a':5,'b':2,'c':3}                           │
└───────────────────────────────────────────────┘
```
