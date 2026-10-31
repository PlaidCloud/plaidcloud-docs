---
title: TRY_TO_BINARY (Lakehouse v1)
description: TRY_TO_BINARY：将表达式转换为二进制值，失败时返回 NULL，而不是引发错误。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-to-binary.md
---

[TO_BINARY](../to-binary/) 的增强版本，将输入表达式转换为二进制值，转换失败时返回 `NULL`，而不是引发错误。

另请参阅：[TO_BINARY](../to-binary/)

## Analyze 语法

```python
func.try_to_binary( <expr> )
```

## Analyze 示例

```python
func.try_to_binary('Databend')

┌───────────────────────────────────────┐
│ func.try_to_binary('Databend')        │
├───────────────────────────────────────┤
│  4461746162656E64                     │
└───────────────────────────────────────┘
```

## SQL 语法

```sql
TRY_TO_BINARY( <expr> )
```

## 示例

此示例成功将 JSON 数据转换为二进制：

```sql
SELECT TRY_TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant_success;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

此示例演示当输入为 `NULL` 时，函数转换失败：

```sql
SELECT TRY_TO_BINARY(PARSE_JSON(NULL)) AS binary_variant_invalid_json;

┌─────────────────────────────┐
│ binary_variant_invalid_json │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
