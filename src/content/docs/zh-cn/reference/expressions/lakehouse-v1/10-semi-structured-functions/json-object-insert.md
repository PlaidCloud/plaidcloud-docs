---
title: JSON_OBJECT_INSERT（Lakehouse v1）
description: JSON_OBJECT_INSERT — 在 JSON 对象中插入或更新键值对。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-insert.md
---

在 JSON 对象中插入或更新键值对。

## SQL 语法

```sql
JSON_OBJECT_INSERT(<json_object>, <key>, <value>[, <update_flag>])
```

| 参数                | 说明 |   |
|---------------------|------|---|
| `<json_object>`     | 输入的 JSON 对象。 |   |
| `<key>`             | 要插入或更新的键。 |   |
| `<value>`           | 要赋给该键的值。 |   |
| `<update_flag>` | 布尔标志，控制当指定的键已存在于 JSON 对象中时是否替换其值。如果为 `true`，则在键已存在时替换其值。如果为 `false`（或省略），则在键已存在时报错。 |   |

## 返回类型

返回更新后的 JSON 对象。

## SQL 示例

此示例演示如何在现有 JSON 对象中插入值为 3 的新键 'c'：

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'c', 3);

┌────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'c', 3) │
├────────────────────────────────────────────────────────────┤
│ {"a":1,"b":2,"c":3,"d":4}                                  │
└────────────────────────────────────────────────────────────┘
```

此示例演示如何将更新标志设为 `true`，把现有键 'a' 的值从 1 更新为 10，从而允许替换该键的值：

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10, true);

┌───────────────────────────────────────────────────────────────────┐
│ json_object_insert('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 10, TRUE) │
├───────────────────────────────────────────────────────────────────┤
│ {"a":10,"b":2,"d":4}                                              │
└───────────────────────────────────────────────────────────────────┘
```

此示例演示在未将更新标志设为 `true` 的情况下，尝试为现有键 'a' 插入值时发生的错误：

```sql
SELECT JSON_OBJECT_INSERT('{"a":1,"b":2,"d":4}'::variant, 'a', 10);

error: APIError: ResponseError with 1006: ObjectDuplicateKey while evaluating function `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)` in expr `json_object_insert('{"a":1,"b":2,"d":4}', 'a', 10)`
```
