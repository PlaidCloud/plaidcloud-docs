---
title: JSON_OBJECT_DELETE (Lakehouse v1)
description: JSON_OBJECT_DELETE — JSON 객체에서 지정한 키를 삭제하고 수정된 객체를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-delete.md
---

JSON 객체에서 지정한 키를 삭제하고 수정된 객체를 반환합니다. 지정한 키가 객체에 없으면 무시됩니다.

## SQL Syntax

```sql
json_object_delete(<json_object>, <key1> [, <key2>, ...])
```

## 매개변수

| 매개변수 | 설명 |
|-----------|-------------|
| json_object | 키를 삭제할 JSON 객체(VARIANT 타입)입니다. |
| key1, key2, ... | 객체에서 삭제할 키를 나타내는 하나 이상의 문자열 리터럴입니다. |

## 반환 타입

지정한 키가 제거된, 수정된 JSON 객체를 담은 VARIANT를 반환합니다.

## SQL Examples

키 하나 삭제:
```sql
SELECT json_object_delete('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"b":2,"c":3}
```

여러 키 삭제:
```sql
SELECT json_object_delete('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"b":2,"d":4}
```

존재하지 않는 키 삭제(해당 키는 무시됨):
```sql
SELECT json_object_delete('{"a":1,"b":2}'::VARIANT, 'x');
-- Result: {"a":1,"b":2}
```
