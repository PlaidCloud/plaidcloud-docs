---
title: JSON_OBJECT_PICK (Lakehouse v1)
description: JSON_OBJECT_PICK — 지정한 키만 포함하는 새 JSON 객체를 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-pick.md
---

입력 JSON 객체에서 지정한 키만 포함하는 새 JSON 객체를 만듭니다. 지정한 키가 입력 객체에 없으면 결과에서 생략됩니다.

## SQL Syntax

```sql
json_object_pick(<json_object>, <key1> [, <key2>, ...])
```

## 매개변수

| 매개변수 | 설명 |
|-----------|-------------|
| json_object | 키를 선택할 JSON 객체(VARIANT 타입)입니다. |
| key1, key2, ... | 결과 객체에 포함할 키를 나타내는 하나 이상의 문자열 리터럴입니다. |

## 반환 타입

지정한 키와 그에 대응하는 값만 담은 새 JSON 객체를 포함하는 VARIANT를 반환합니다.

## SQL Examples

키 하나 선택:
```sql
SELECT json_object_pick('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"a":1}
```

여러 키 선택:
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'b');
-- Result: {"a":1,"b":2}
```

존재하지 않는 키와 함께 선택(존재하지 않는 키는 무시됨):
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"a":1}
```
