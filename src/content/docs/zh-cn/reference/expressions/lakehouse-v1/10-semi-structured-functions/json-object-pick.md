---
title: JSON_OBJECT_PICK（Lakehouse v1）
description: JSON_OBJECT_PICK — 创建仅包含指定键的新 JSON 对象。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-pick.md
---

从输入 JSON 对象中创建仅包含指定键的新 JSON 对象。如果指定的键在输入对象中不存在，则从结果中省略。

## SQL 语法

```sql
json_object_pick(<json_object>, <key1> [, <key2>, ...])
```

## 参数

| 参数 | 说明 |
|------|------|
| json_object | 要从中选取键的 JSON 对象（VARIANT 类型）。 |
| key1, key2, ... | 一个或多个字符串字面量，表示要包含在结果对象中的键。 |

## 返回类型

返回一个 VARIANT，其中包含仅有指定键及其对应值的新 JSON 对象。

## SQL 示例

选取单个键：
```sql
SELECT json_object_pick('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"a":1}
```

选取多个键：
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'b');
-- Result: {"a":1,"b":2}
```

选取不存在的键（不存在的键被忽略）：
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"a":1}
```
