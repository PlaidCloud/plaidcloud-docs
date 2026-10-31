---
title: MAP_PICK (Lakehouse v1)
description: MAP_PICK — 기존 MAP에서 지정한 키-값 쌍을 포함하는 새 MAP을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-pick.md
---

기존 MAP에서 지정한 키-값 쌍을 포함하는 새 MAP을 반환합니다.

## SQL 구문

```sql
MAP_PICK( <map>, <key1> [, <key2>, ... ] )
MAP_PICK( <map>, <array> )
```

## 인수

| 인수 | 설명                                             |
|-----------|-------------------------------------------------------- |
| `<map>`   | 입력 MAP입니다.                                          |
| `<keyN>`  | 반환되는 MAP에 포함할 KEY입니다.          |
| `<array>` | 반환되는 MAP에 포함할 KEY의 배열입니다. |

:::note
- 키 식의 형식과 MAP에 있는 키의 형식이 같아야 합니다.
- MAP에서 찾을 수 없는 키 값은 무시됩니다.
:::

## 반환 형식

Map.

## SQL 예제

```sql
SELECT MAP_PICK({'a':1,'b':2,'c':3}, 'a', 'c');
┌─────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, 'a', 'c') │
├─────────────────────────────────────────┤
│ {'a':1,'c':3}                           │
└─────────────────────────────────────────┘

SELECT MAP_PICK({'a':1,'b':2,'c':3}, ['a', 'b']);
┌───────────────────────────────────────────┐
│ map_pick({'a':1,'b':2,'c':3}, ['a', 'b']) │
├───────────────────────────────────────────┤
│ {'a':1,'b':2}                             │
└───────────────────────────────────────────┘
```
