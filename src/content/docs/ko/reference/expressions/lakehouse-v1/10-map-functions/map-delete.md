---
title: MAP_DELETE (Lakehouse v1)
description: MAP_DELETE — 하나 이상의 키를 제거한 기존 MAP을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-delete.md
---

하나 이상의 키를 제거한 기존 MAP을 반환합니다.

## SQL 구문

```sql
MAP_DELETE( <map>, <key1> [, <key2>, ... ] )
MAP_DELETE( <map>, <array> )
```

## 인수

| 인수 | 설명                                            |
|-----------|--------------------------------------------------------|
| `<map>`   | 제거할 KEY가 들어 있는 MAP입니다.               |
| `<keyN>`  | 반환되는 MAP에서 제외할 KEY입니다.          |
| `<array>` | 반환되는 MAP에서 제외할 KEY의 배열입니다. |

:::note
- 키 식의 형식과 MAP에 있는 키의 형식이 같아야 합니다.
- MAP에서 찾을 수 없는 키 값은 무시됩니다.
:::

## 반환 형식

Map.

## SQL 예제

```sql
SELECT MAP_DELETE({'a':1,'b':2,'c':3}, 'a', 'c');
┌───────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, 'a', 'c') │
├───────────────────────────────────────────┤
│ {'b':2}                                   │
└───────────────────────────────────────────┘

SELECT MAP_DELETE({'a':1,'b':2,'c':3}, ['a', 'b']);
┌─────────────────────────────────────────────┐
│ map_delete({'a':1,'b':2,'c':3}, ['a', 'b']) │
├─────────────────────────────────────────────┤
│ {'c':3}                                     │
└─────────────────────────────────────────────┘
```
