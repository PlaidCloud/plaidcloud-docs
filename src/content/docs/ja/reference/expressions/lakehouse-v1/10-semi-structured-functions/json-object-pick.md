---
title: JSON_OBJECT_PICK (Lakehouse v1)
description: JSON_OBJECT_PICK — 指定したキーだけを含む新しいJSONオブジェクトを作成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-object-pick.md
---

入力のJSONオブジェクトから指定したキーだけを含む、新しいJSONオブジェクトを作成します。指定したキーが入力オブジェクトに存在しない場合は、結果から除外されます。

## SQL構文

```sql
json_object_pick(<json_object>, <key1> [, <key2>, ...])
```

## パラメーター

| パラメーター | 説明 |
|-----------|-------------|
| json_object | キーを選択する対象のJSONオブジェクト（VARIANT型）です。 |
| key1, key2, ... | 結果のオブジェクトに含めるキーを表す、1つ以上の文字列リテラルです。 |

## 戻り値の型

指定したキーとそれに対応する値だけを含む、新しいJSONオブジェクトを含むVARIANTを返します。

## SQLの例

1つのキーを選択する場合：
```sql
SELECT json_object_pick('{"a":1,"b":2,"c":3}'::VARIANT, 'a');
-- Result: {"a":1}
```

複数のキーを選択する場合：
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'b');
-- Result: {"a":1,"b":2}
```

存在しないキーを指定して選択する場合（存在しないキーは無視されます）：
```sql
SELECT json_object_pick('{"a":1,"b":2,"d":4}'::VARIANT, 'a', 'c');
-- Result: {"a":1}
```
