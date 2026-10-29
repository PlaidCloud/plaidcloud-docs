---
title: JSON_OBJECT_INSERT (Lakehouse v1)
description: JSON_OBJECT_INSERT — JSON 객체에 키-값 쌍을 삽입하거나 업데이트합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-insert.md
---

JSON 객체에 키-값 쌍을 삽입하거나 업데이트합니다.

## SQL Syntax

```sql
JSON_OBJECT_INSERT(<json_object>, <key>, <value>[, <update_flag>])
```

| 매개변수           | 설명                                                                                                                                                                                                                                          |   |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `<json_object>`     | 입력 JSON 객체입니다.                                                                                                                                                                                                                               |   |
| `<key>`             | 삽입하거나 업데이트할 키입니다.                                                                                                                                                                                                                   |   |
| `<value>`           | 키에 할당할 값입니다.                                                                                                                                                                                                                      |   |
| `<update_flag>` | 지정한 키가 JSON 객체에 이미 있을 때 값을 교체할지 제어하는 불리언 플래그입니다. `true`이면 키가 이미 있는 경우 값을 교체합니다. `false`이거나 생략하면 키가 있을 때 오류가 발생합니다. |   |

## 반환 타입

업데이트된 JSON 객체를 반환합니다.

## SQL Examples

이 예제는 기존 JSON 객체에 값이 3인 새 키 'c'를 삽입하는 방법을 보여줍니다.

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'c', 3);

┌────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'c', 3) │
├────────────────────────────────────────────────────────────┤
│ {"a":1,"b":2,"c":3,"d":4}                                  │
└────────────────────────────────────────────────────────────┘
```

이 예제는 업데이트 플래그를 `true`로 설정해 키의 값을 교체할 수 있게 하여, 기존 키 'a'의 값을 1에서 10으로 업데이트하는 방법을 보여줍니다.

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10, true);

┌───────────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 10, TRUE) │
├───────────────────────────────────────────────────────────────────┤
│ {"a":10,"b":2,"d":4}                                              │
└───────────────────────────────────────────────────────────────────┘
```

이 예제는 업데이트 플래그를 `true`로 지정하지 않고 기존 키 'a'에 값을 삽입하려 할 때 발생하는 오류를 보여줍니다.

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10);

error: APIError: ResponseError with 1006: ObjectDuplicateKey while evaluating function `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)` in expr `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)`
```
