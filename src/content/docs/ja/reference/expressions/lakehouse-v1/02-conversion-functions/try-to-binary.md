---
title: TRY_TO_BINARY (Lakehouse v1)
description: TRY_TO_BINARY — 式をバイナリ値に変換します。失敗した場合は、エラーを発生させずにNULLを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-to-binary.md
---

入力された式をバイナリ値に変換する[TO_BINARY](../to-binary/)の拡張版です。変換に失敗した場合は、エラーを発生させずに`NULL`を返します。

関連項目：[TO_BINARY](../to-binary/)

## Analyzeの構文

```python
func.try_to_binary( <expr> )
```

## Analyzeの例

```python
func.try_to_binary('Databend')

┌───────────────────────────────────────┐
│ func.try_to_binary('Databend')        │
├───────────────────────────────────────┤
│  4461746162656E64                     │
└───────────────────────────────────────┘
```

## SQLの構文

```sql
TRY_TO_BINARY( <expr> )
```

## 例

この例では、JSONデータを正常にバイナリに変換します。

```sql
SELECT TRY_TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant_success;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

この例では、入力が`NULL`の場合、関数が変換に失敗することを示します。

```sql
SELECT TRY_TO_BINARY(PARSE_JSON(NULL)) AS binary_variant_invalid_json;

┌─────────────────────────────┐
│ binary_variant_invalid_json │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
