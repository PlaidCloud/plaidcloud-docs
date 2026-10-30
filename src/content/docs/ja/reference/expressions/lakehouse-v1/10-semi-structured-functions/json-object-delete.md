---
title: JSON_OBJECT_DELETE (Lakehouse v1)
description: JSON_OBJECT_DELETE — JSONオブジェクトから指定したキーを削除し、変更後のオブジェクトを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-delete.md
---

JSONオブジェクトから指定したキーを削除し、変更後のオブジェクトを返します。指定したキーがオブジェクトに存在しない場合は無視されます。

## SQL構文

```sql
json_object_delete(<json_object>, <key1> [, <key2>, ...])
```

## パラメーター

| パラメーター | 説明 |
|-----------|-------------|
| json_object | キーを削除する対象のJSONオブジェクト（VARIANT型）です。 |
| key1, key2, ... | オブジェクトから削除するキーを表す、1つ以上の文字列リテラルです。 |

## 戻り値の型

指定したキーを削除した、変更後のJSONオブジェクトを含むVARIANTを返します。

## SQLの例

1つのキーを削除する場合：
```sql
SELECT json_object_delete('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"b":2,"c":3}
```

複数のキーを削除する場合：
```sql
SELECT json_object_delete('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"b":2,"d":4}
```

存在しないキーを削除する場合（キーは無視されます）：
```sql
SELECT json_object_delete('{"a":1,"b":2}'::VARIANT, 'x');
-- Result: {"a":1,"b":2}
```
